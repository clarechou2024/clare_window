from flask import Blueprint,render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField
from wtforms.validators import DataRequired,Length
from .datasource import validateUser

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
    if request.method == "POST":
        if form.validate_on_submit():
            print("表單傳送過來")
            print("驗證了token")  #token就是密碼
            email = form.email.data
            password = form.password.data
            print(f'email:{email}')
            print(f'password:{password}')
            is_ok,username = validateUser(email,password)
            if is_ok:
                session['username'] = username    #寫一個cookies在裡面
                return redirect('/')
                # print(f"您好:{username}")
            else:
                print(f'密碼錯誤')
    else:
        print("這是第一次進入")

    return render_template('/auth/login.html.jinja',form=form)