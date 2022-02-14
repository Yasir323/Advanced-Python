import json
from flask import Flask, request, jsonify
from query_city_new import WeatherInfo

app = Flask(__name__)

@app.route("/query_weather", methods=["GET","POST"])
def query_weather():
	latitude=float(request.args.get('latitude')),
	longitude=float(request.args.get('longitude')),
	radius=int(request.args.get('radius'))
	weather = WeatherInfo()
	return jsonify(weather.get_weather(latitude, longitude, radius))

@app.route("/forecast", methods=["GET","POST"])
def forecast():
	try:
		name = request.form['name']
		weather = WeatherInfo()
		result = weather.get_forecast(name)
		if result:
			return json.loads(result)
		return jsonify([{"message":"City Not Found"}]), 200
	except:
		return jsonify([{"message":"Some error occured, recheck parameter and try again"}]), 200


@app.route("/isForecast", methods=["GET","POST"])
def is_forecast():
	try:
		name = request.form['name'] if 'name' in request.form else ""
		# name = request.form['name']
		weather = WeatherInfo()
		result = weather.is_forecast_present(name)
		if result and type(result) == str:
			return json.loads(result)
		if result and type(result) == dict:
			return result
		return jsonify([{"message":"City Not Found"}]), 200
	except Exception as e:
		print(e.args)
		return jsonify([{"message":"Some error occured, recheck parameter and try again"}]), 200


if __name__== "__main__":
	app.run(debug=True, host="127.0.0.1", port=6789)