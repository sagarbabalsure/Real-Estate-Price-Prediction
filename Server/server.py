from flask import *
import os
import utils
import json
template_dir = os.path.abspath('C:/Users/sagar/Desktop/Python/Real-Estate-Price-Prediction/Client')
static_dir = os.path.abspath('C:/Users/sagar/Desktop/Python/Real-Estate-Price-Prediction/Client')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/form',methods=['GET'])
def form():
	return render_template("form.html", locations=utils.get_location_names())

@app.route('/get_location_names')
def get_location_names():
	response = jsonify({
		'locations':utils.get_location_names()
		})
	response.headers.add("Access-Control-Allow-Origin","*")
	return response


@app.route("/predict_estimated_price",methods=['GET','POST'])
def predict_estimated_price():
	if request.method == 'POST':
		total_sqft = float(request.form['total_sqft'])
		bhk = int(request.form['bhk'])
		bath = int(request.form['bath'])
		location = request.form['location']
		
		response = jsonify({
			'estimated_price':utils.get_estimated_price(location,total_sqft,bhk,bath)
			})
		response.headers.add("Access-Control-Allow-Origin","*")
		result = response.json
		# print(result['estimated_price'])
		return render_template('form.html', price=result['estimated_price'])
	
	return render_template('form.html')

if __name__=="__main__":
	print("starting flask server...")
	app.run(debug=True)