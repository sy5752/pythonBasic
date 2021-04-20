from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/param', methods=['GET', 'POST'])
def param():
    if request.method == "POST" :
        name = request.form.get('name', "kimchulsu")
    if request.method == "GET" :
        name = request.args.get('name', "kimchulsu")
    return "param=" +name

#     temp = request.args.get('name')
#     return 'param=' + temp

@app.route('/forward.do')
def forward():
    title = "Good Morning"
    return render_template('forward.html',title=title)

if __name__ == '__main__' :
    app.run(debug = True)