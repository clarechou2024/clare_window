from flask import Blueprint,render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,StringField,SelectField,BooleanField,DateField,TextAreaField
from wtforms.validators import DataRequired,Length,Regexp,Optional,EqualTo
from .datasource import validateUser

auth_blueprint = Blueprint('auth',__name__)

class UserRegistrationForm(FlaskForm):
    uName = StringField('姓名:',validators=[DataRequired(),Length(min=2,max=10)])
    uGender = SelectField('性別'choices=[("男","男"),("女","女")])
    uPhone = StringField('行動電話',validators=[DataRequired(),Regexp(r'\d\d\d\d-\d\d\d-\d\d\d',message="格式不正確")])
    uEmail = EmailField('電子郵件:',validators=[DataRequired()])
    isGetEmail = BooleanField("接受促銷email",default=False)
    uBirthday = DateField("出生年月日",validators=[Optional()],format='%Y-%m-%d')
    uAboutMe = TextAreaField('自我介紹',validators=[Optional(),Length(max=200),description="最多200字"])
    uPass = PasswordField("密碼",validators=[DataRequired(),Length(min=4,max=20),EqualTo('uConfirmPass',message='驗證密碼不正確')])
    uConfirmPass = PasswordField("驗證密碼",validators=[DataRequired(),Length(min=4,max=20)])
    

@auth_blueprint.route('/auth/register',method=['GET','POST'])
def register():
    form = UserRegistrationForm()
    if request.method == "POST":
        print("使用者送出表單")
    else:
        print("第一次進入")

    return render_template('/auth/register.html.jinja',form=form)

class LoginForm(FlaskForm):
    email = EmailField('郵件信箱',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired(),Length(min=4,max=20)])


@auth_blueprint.route("/auth/",methods=['GET','POST'])
@auth_blueprint.route("/auth/login",methods=['GET','POST'])
def index(email:str | None = None):
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
            print (is_ok)
            if is_ok:
                # print(f"您好:{username}")
                session['username'] = username    #寫一個cookies在裡面
                return redirect('/')
            else:
                #print(f'密碼錯誤')
                form.email.errors.append("帳號或密碼錯誤")
                form.email.data = ""

    else:
        print("這是第一次進入")
        # if email is not None:
        #     form.email.data = email

    return render_template('/auth/login.html.jinja',form=form)


@auth_blueprint.route("/auth/logout")
def logout():
    session.pop('username')
    return redirect('/')