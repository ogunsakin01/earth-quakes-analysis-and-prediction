from flask import Flask, jsonify
import revised.welcome as welcome

app = Flask(__name__)

@app.route('/')
def index():
    return welcome.index()

@app.route('/data')
def data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)