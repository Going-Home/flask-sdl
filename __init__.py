from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"

@app.route('/login')
def login_page():
	return render_template("login.html")

if __name__=="__main__":
	app.run()

