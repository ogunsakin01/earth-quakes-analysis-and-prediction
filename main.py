from flask import Flask, render_template
from api.earthquake_prediction_data_cleaning import EarthquakePredictionDataCleaning
from api.earthquakes_and_tectonic_plates_visualisation import EarthquakeAndTectonicPlatesVisualisations
from api.earthquake_prediction import EarthQuakePrediction
from api.predict_location_with_lstm import PredictLocationWithLSTM
import json

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Group 15 Project"


@app.route('/get-clean-earthquakes-and-tectonic-plates-data', methods=['GET'])
def getCleanEarthquakesAndTectonicPlatesData():
    cleaned = EarthquakePredictionDataCleaning()
    return cleaned.get_combined_data()


@app.route('/get-clean-earthquakes-data', methods=['GET'])
def getCleanEarthquakesData():
    cleaned = EarthquakePredictionDataCleaning()
    return cleaned.get_cleaned_earthquake_data()


@app.route('/get-clean-tectonic-plates-data', methods=['GET'])
def getCleanTectonicPlates():
    cleaned = EarthquakePredictionDataCleaning()
    return cleaned.get_cleaned_tectonic_plate_data()


@app.route('/visualise-tectonic-plate', methods=['GET'])
def visualiseTectonicPlates():
    visualisations = EarthquakeAndTectonicPlatesVisualisations()
    folium_map = visualisations.visualise_tectonic_plate()
    map_html = folium_map._repr_html_()
    return render_template('map.html', map_html=map_html)


@app.route('/visualise-earthquake-on-tectonic-plate', methods=['GET'])
def visualiseEarthquakeOnTectonicPlates():
    visualisations = EarthquakeAndTectonicPlatesVisualisations()
    folium_map = visualisations.visualise_earthquakes_on_tectonic_plate()
    map_html = folium_map._repr_html_()
    return render_template('map.html', map_html=map_html)


@app.route('/get-prediction/<param1>', methods=['GET'])
def getPrediction(param1):  # Date Format = YYYY-MM-DD
    prediction = EarthQuakePrediction(param1)
    return prediction.handle()


@app.route('/get-lstm-prediction/<param1>', methods=['GET'])
def getLSTMPrediction(param1):  # Date Format = YYYY-MM-DD
    prediction = PredictLocationWithLSTM(param1)
    return prediction.handle()


@app.route('/visualise-prediction/<param1>', methods=['GET'])
def visualisePrediction(param1):  # Date Format = YYYY-MM-DD
    prediction = EarthQuakePrediction(param1)
    predicted_data_frame = prediction.predicted
    predicted = predicted_data_frame.to_json(orient='records')
    predicted = json.loads(predicted)[0]
    visualisations = EarthquakeAndTectonicPlatesVisualisations()
    folium_map = visualisations.visualise_predicted_earthquake_on_tectonic_plate(predicted_data_frame)
    map_html = folium_map._repr_html_()
    return render_template('predicted_map.html', map_html=map_html, predicted=predicted)


@app.route('/visualise-lstm-prediction/<param1>', methods=['GET'])
def visualiseLSTMPrediction(param1):  # Date Format = YYYY-MM-DD
    prediction = PredictLocationWithLSTM(param1)
    predicted_data_frame = prediction.predicted
    predicted = predicted_data_frame.to_json(orient='records')
    predicted = json.loads(predicted)[0]
    visualisations = EarthquakeAndTectonicPlatesVisualisations()
    folium_map = visualisations.visualise_predicted_earthquake_on_tectonic_plate(predicted_data_frame)
    map_html = folium_map._repr_html_()
    return render_template('predicted_map.html', map_html=map_html, predicted=predicted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
