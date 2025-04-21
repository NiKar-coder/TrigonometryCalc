from flask import Flask, render_template, request
import json
import math
app = Flask(__name__)

GLOBS = {
    "__builtins__": {},
    "tg": lambda x: math.tan(math.radians(x)),
    "sin": lambda x: math.sin(math.radians(x)),
    "ctg": lambda x: math.cos(math.radians(x)) / math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x))
}


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


def calculate(num, fc):
    for x, y in (",", "."), (" ", ""):
        num = num.replace(x, y)
    num = float(num)
    if fc == "arctg":
        ans = math.degrees(math.atan(num))
    elif fc == "arcsin":
        ans = math.degrees(math.asin(num))
    elif fc == "arcctg":
        ans = math.degrees(math.pi / 2 - math.atan(num))
    elif fc == "arcos":
        ans = math.degrees((math.acos(num)))
    else:
        ans = eval(str(num), GLOBS, {})
    return f'{round(ans, 4)}°'

if __name__ == '__main__':
    app.run(host='192.168.1.2', port='8080', debug=True)
