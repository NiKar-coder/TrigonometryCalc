from flask import Flask, render_template, request
import json
import math
app = Flask(__name__)


def get_functions():
    with open("functions.json", "rt", encoding="utf8") as f:
        functions = json.loads(f.read())
    return functions


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            input_ = request.form['input_']
            func = request.form['option']
            return render_template('index.html', res="true",
                                   result=calculate(input_, func),
                                   alert='false', functions=get_functions())
        except Exception:
            return render_template('index.html', res="false", alert="true",
                                   message="Something went wrong",
                                   functions=get_functions())
    else:
        return render_template('index.html', res="false", alert="false",
                               functions=get_functions())


@app.route('/help')
def help():
    return render_template('help.html', functions=get_functions())


@app.route('/about')
def about():
    return render_template('about.html')


def calculate(num_, fc):
    for x, y in (",", "."), (" ", ""):
        num_ = num_.replace(x, y)
    num = float(num_)
    if fc == "arctg":
        return f'{round(math.degrees(math.atan(num)), 4)}°'
    elif fc == "arcsin":
        return f'{round(math.degrees(math.asin(num)), 4)}°'
    elif fc == "arcctg":
        return f'{round(math.degrees(math.pi / 2 - math.atan(num)),4)}°'
    elif fc == "arcos":
        return f'{round(math.degrees((math.acos(num))), 4)}°'
    elif fc == "cos":
        return round(math.cos(math.radians(num)), 4)
    elif fc == "sin":
        return round(math.sin(math.radians(num)), 4)
    elif fc == "tg":
        return round(math.tan(math.radians(num)), 4)
    elif fc == "ctg":
        return round(math.cos(math.radians(num)) / math.sin(math.radians(num)), 4)

if __name__ == '__main__':
    app.run(host='192.168.1.2', port='8080', debug=True)
