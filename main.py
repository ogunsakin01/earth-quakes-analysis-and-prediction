from flask import Flask, jsonify
import testing.welcome as welcome
import testing.test_file as test_file

app = Flask(__name__)

@app.route('/')
def index():
    return welcome.handle()

@app.route('/test-data')
def testData():
    return test_file.handle()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)