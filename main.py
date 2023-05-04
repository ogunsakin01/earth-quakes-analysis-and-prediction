from flask import Flask
import testing.welcome as welcome
import testing.test_file as test_file
# from experiments import dataset_cleaning as data_cleaning

app = Flask(__name__)

@app.route('/')
def index():
    return welcome.handle()

@app.route('/test-data')
def testData():
    return test_file.handle()

@app.route('/clean-data-set')
def cleanDataSet():
    return []


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)