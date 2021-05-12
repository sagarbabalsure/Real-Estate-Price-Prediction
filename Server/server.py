from flask import *
app = Flask(__name__)

@app.route('/hello')
def hello():
	return "Hi i am sagar from real estate"

if __name__=="__main__":
	print("starting flask server...")
	app.run()