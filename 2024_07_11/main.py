from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")   #/-->首頁
def index():
    return render_template("index.html.jinja")