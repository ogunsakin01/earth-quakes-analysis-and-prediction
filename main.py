from flask import Flask, jsonify
import revised.welcome as welcome
import revised.test_file as test_file

app = Flask(__name__)

@app.route('/')
def index():
    return welcome.index()

@app.route('/test-data')
def testData():
    return test_file.test_data()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)