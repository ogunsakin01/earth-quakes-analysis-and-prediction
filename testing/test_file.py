from flask import jsonify


def handle():
    data = {'name': 'Earthquake Experiment', 'Year': 2023}
    return jsonify(data)
