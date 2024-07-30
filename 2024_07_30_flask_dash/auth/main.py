from flask import Blueprint,render_template
# from flask_wtf import FlaskForm

auth_blueprint = Blueprint('auth',__name__)
# #設加密字串
# WTF_CSRF_SECRET_KEY = 'a random string'
@auth_blueprint.route("/auth/",methods=['GET','POST'])
@auth_blueprint.route("/auth/login",methods=['GET','POST'])
def index():
    return render_template('/auth/login.html.jinja')