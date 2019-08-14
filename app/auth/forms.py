from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('用户名', validators=[DataRequired()]))
    password = PasswordField(_l('密码', validators=[DataRequired()]))
    remember_me = BooleanField(_l('记住密码'))
    submit = SubmitField(_l('登录'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('用户名', validators=[DataRequired()]))
    email = StringField(_l('邮箱', validators=[DataRequired(), Email()]))
    password = PasswordField(_l('密码', validators=[DataRequired()]))
    password2 = PasswordField(_l('确认密码', validators=[DataRequired(), EqualTo('password')]))
    submit = SubmitField(_l('注册'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('用户名已经存在'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('邮箱已经注册'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('邮箱', validators=[DataRequired(), Email()]))
    submit = SubmitField(_l('重置密码'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('密码', validators=[DataRequired()]))
    password2 = PasswordField(_l('确认密码', validators=[DataRequired(), EqualTo(password)]))
    submit = SubmitField(_l('请求密码重置'))