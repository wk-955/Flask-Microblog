# from datetime import datetime, timedelta
# import unittest
# from app import app, db
# from app.models import User, Post
#
# class UserModelCase(unittest.TestCase):
#     def setUp(self):
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
#         db.create_all()
#
#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#
#     def test_password_hashing(self):
#         u = User(username='susan')
#         u.set_password('cat')
#         self.assertFalse(u.check_password('dog'))
#         self.assertTrue(u.check_password('cat'))
#
#     def test_avatar(self):
#         u = User(username='john', email='john@example.com')
#         self.assertEqual(u.avatar(128), 'http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=monsterid&s=128&r=x')
#
#     def test_follow(self):
#         u1 = User(username='john', email='john@example.com')
#         u2 = User(username='susan', email='susan@example.com')
#         db.session.add(u1)
#         db.session.add(u2)
#         db.session.commit()
#         self.assertEqual(u1.followed.all(), [])
#         self.assertEqual(u1.followers.all(), [])
#
#         u1.follow(u2)
#         db.session.commit()
#         self.assertTrue(u1.is_following(u2))
#         self.assertEqual(u1.followed.count(), 1)
#         self.assertEqual(u1.followed.first().username, 'susan')
#         self.assertEqual(u2.followers.count(), 1)
#         self.assertEqual(u2.followers.first().username, 'john')
#         u1.unfollow(u2)
#         db.session.commit()
#         self.assertFalse(u1.is_following(u2))
#         self.assertEqual(u1.followed.count(), 0)
#         self.assertEqual(u2.followers.count(), 0)
#
#     def test_follow_posts(self):
#         # create four users
#         u1 = User(username='john', email='john@example.com')
#         u2 = User(username='susan', email='susan@example.com')
#         u3 = User(username='mary', email='mary@example.com')
#         u4 = User(username='david', email='david@example.com')
#         db.session.add_all([u1, u2, u3, u4])
#
#         # create four posts
#         now = datetime.utcnow()
#         p1 = Post(body="post from john", author=u1,
#                   timestamp=now + timedelta(seconds=1))
#         p2 = Post(body="post from susan", author=u2,
#                   timestamp=now + timedelta(seconds=4))
#         p3 = Post(body="post from mary", author=u3,
#                   timestamp=now + timedelta(seconds=3))
#         p4 = Post(body="post from david", author=u4,
#                   timestamp=now + timedelta(seconds=2))
#         db.session.add_all([p1, p2, p3, p4])
#         db.session.commit()
#
#         # setup the followers
#         u1.follow(u2)  # john follows susan
#         u1.follow(u4)  # john follows david
#         u2.follow(u3)  # susan follows mary
#         u3.follow(u4)  # mary follows david
#         db.session.commit()
#
#         # check the followed posts of each user
#         f1 = u1.followed_posts().all()
#         f2 = u2.followed_posts().all()
#         f3 = u3.followed_posts().all()
#         f4 = u4.followed_posts().all()
#         self.assertEqual(f1, [p2, p4, p1])
#         self.assertEqual(f2, [p2, p3])
#         self.assertEqual(f3, [p3, p4])
#         self.assertEqual(f4, [p4])
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#



# from flask import Flask
# from flask_mail import Mail
#
# app = Flask(__name__)
#
# app.config['MAIL_SERVER'] = 'smtp.qq.com'
# app.config['MAIL_POST'] = 465
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USERNAME'] = '1127480498@qq.com'
# app.config['MAIL_PASSWORD'] = 'tqcwmbptaacsigaa'
#
# mail = Mail(app)

from flask import Flask, request
from flask_script import Manager, Shell
from flask_mail import Mail, Message
from threading import Thread


# app = Flask(__name__)
# app.config['MAIL_DEBUG'] = True             # 开启debug，便于调试看信息
# app.config['MAIL_SUPPRESS_SEND'] = False    # 发送邮件，为True则不发送
# app.config['MAIL_SERVER'] = 'smtp.qq.com'   # 邮箱服务器
# app.config['MAIL_PORT'] = 25               # 端口
# app.config['MAIL_USE_SSL'] = True           # 重要，qq邮箱需要使用SSL
# app.config['MAIL_USE_TLS'] = False          # 不需要使用TLS
# app.config['MAIL_USERNAME'] = '1127480498@qq.com'  # 填邮箱
# app.config['MAIL_PASSWORD'] = 'tqcwmbptaacsigaa'      # 填授权码
# app.config['MAIL_DEBUG'] = True
# # app.config['MAIL_DEFAULT_SENDER'] = 'xxx@qq.com'  # 填邮箱，默认发送者
#
#
# manager = Manager(app)
# mail = Mail(app)
#
#
# # 异步发送邮件
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
#
# @app.route('/')
# def index():
#     msg = Message(subject='Hello World',
#                   sender="1127480498@qq.com",  # 需要使用默认发送者则不用填
#                   recipients='2585765186@qq.com')
#     # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
#     msg.body = 'sended by flask-email'
#     msg.html = '<b>测试Flask发送邮件<b>'
#     thread = Thread(target=send_async_email, args=[app, msg])
#     thread.start()
#     return '<h1>邮件发送成功</h1>'
#
#
# if __name__ == '__main__':
#     manager.run()


from flask import Flask, render_template
from flask_mail import Mail, Message
from config import Config
import os
path = os.path.dirname(__file__)

mail = Mail()

app = Flask(__name__)
app.config.from_object(Config)

mail.init_app(app)

#发送文本
@app.route('/email_send_charactor/')
def email_send_charactor():
    message = Message(subject='hello flask-mail',recipients=['2585765186@qq.com'], body='flask-mail测试代码')
    try:
        mail.send(message)
        return '发送成功，请注意查收~'
    except Exception as e:
        print(e)
        return '发送失败'


# 发送一个html
@app.route('/email_send_html/')
def email_send_html():
    message = Message(subject='hello flask-mail',recipients=['2585765186@qq.com'])
    try:
        #发送渲染一个模板
        message.html = render_template('email/reset_password.html')
        mail.send(message)
        return '发送成功，请注意查收~'
    except Exception as e:
        print(e)
        return '发送失败'


# #发送附带附件的邮件
# @app.route('/email_send_attach/')
# def email_send_attach():
#     message = Message(subject='hello flask-mail',recipients=['1417766861@qq.com'],body='我是一个附件邮件')
#     try:
#         # message.attach邮件附件添加
#         # 方法attach(self,
#         #        filename=None,
#         #        content_type=None,
#         #        data=None,
#         #        disposition=None,
#         #        headers=None):
#
#         with open(filename,'rb') as fp:
#             message.attach("test.jpg", "image/jpg", fp.read())
#         mail.send(message)
#         return '发送成功，请注意查收~'
#     except Exception as e:
#         print(e)
#         return '发送失败'


if __name__ == '__main__':
    app.run(debug=True)