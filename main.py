import flask
from flask import request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
	number = request.form.get('number')
	print(number)
	return "Hello, " + number

app.run(port=8080)