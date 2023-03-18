from flask import jsonify


def test_data():
    data = {'name': 'Earthquake Experiment', 'Year': 2023}
    return jsonify(data)
