from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin

import BangalorePricePrediction as tm

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': tm.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_area_names', methods=['GET'])
def get_area_names():
    response = jsonify({
        'area': tm.get_area_values()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_availability_names', methods=['GET'])
def get_availability_names():
    response = jsonify({
        'availability': tm.get_availability_values()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
#@cross_origin()
def predict():
    if request.method == "POST":
        sqft = float(request.form['sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        loc = request.form.get('loc')
        area = request.form.get('area')
        availability = request.form.get('avail')

        prediction = round(float(tm.predict_house_price(loc, area, availability, sqft, bhk, bath)), 2)

        return render_template('home.html', prediction_text="The house price is Rs. {} lakhs".format(prediction))

    return render_template("home.html")


if __name__ == "__main__":
    tm.load_saved_attributes()
    app.run(debug = True)