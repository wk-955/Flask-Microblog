import json, random, hashlib, http.client
from flask_babel import _
from flask import current_app
from urllib import parse


def translate(q, fromLang, toLang):
    if 'APPID' not in current_app.config or not current_app.config['APPID']:
        return _('Error1:the translation service is not configured.')
    if 'BD_TRANSLATOR_KEY' not in current_app.config or not current_app.config['BD_TRANSLATOR_KEY']:
        return _('Error2:the translation service is not configured.')
    appid = current_app.config['APPID']
    secretKey = current_app.config['BD_TRANSLATOR_KEY']

    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)

    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+parse.quote(q)+'&from='+ fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        r = response.read().decode('utf-8')
        d = json.loads(r)
        l = d['trans_result']
        l1 = l[0]['dst']

        return l1
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
