from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hey there!"

@app.route("/lol")
def lol():
	return "lol"

@app.route("/huh")
def huh():
	return "cool!"

if __name__ == "__main__":
	app.debug = True
	app.run()
