from flask import Flask,render_template,request
import data

app = Flask(__name__)
@app.route("/")   #/-->首頁
def index():
    #print(list(map(lambda value:value[0],data.get_areas())))
    selected_area = request.args.get('area')
    areas =[tup[0]for tup in data.get_areas()]

    selected_area = '士林區' if selected_area is None else selected_area
    return render_template("index.html.jinja",areas= areas,show_area=selected_area)


    # if selected_area is None:
    #     return render_template("index.html.jinja",areas= areas,show_area='士林區')
    # else:
    #     return render_template("index.html.jinja",areas= areas,show_area=selected_area)
