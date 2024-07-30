from flask import Blueprint,render_template
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField
from wtforms.validators import DataRequired,Length

auth_blueprint = Blueprint('auth',__name__)
# #設加密字串
# WTF_CSRF_SECRET_KEY = 'a random string'


class LoginForm(FlaskForm):
    email = EmailField('郵件信箱',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired(),Length(min=4,max=20)])


@auth_blueprint.route("/auth/",methods=['GET','POST'])
@auth_blueprint.route("/auth/login",methods=['GET','POST'])
def index():
    form = LoginForm()
    return render_template('/auth/login.html.jinja',form=form)