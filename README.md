# Earth Quakes Prediction Using Machine Learning Algorithms
This research explores the prediction of future earthquakes by combining tectonic plate data with historical earthquake data using various machine learning (ML) algorithms. The study employs a comprehensive dataset of tectonic plate movements and historical earthquake data to train and test different ML models, including decision trees, random forests, and neural networks. The study focuses on improving earthquake prediction accuracy by examining the influence of various input features on model performance. The results demonstrate that the proposed approach can effectively predict future earthquakes with high accuracy, providing valuable insights into earthquake forecasting and risk mitigation. This research will provide a significant contribution to earthquake prediction and underscores the potential of ML algorithms in predicting future natural disasters.
## System(s) Requirements
To set up this project on your computer, you will need to have the following application and libraries installed on your computer
- [Docker (Docker Desktop)](https://docs.docker.com/engine/install/)
- Python3
- Keras
- Flask
- Numpy
- Pandas
- Jupyter
- Sklearn
- Folium

## Installation & Setup 
To install, you need to clone this repository by copying the repository https url. You can do this by clicking on the `Code` button displayed on this repo menu. The repository link should look similar or be exactly this `https://github.com/ogunsakin01/earth-quakes-analysis-and-prediction.git`. Then open the terminal interface on your machine and navigate to the desired directory you wish to set up the project. 
After that, then run this command below to clone the repository

```shell
git clone https://github.com/ogunsakin01/earth-quakes-analysis-and-prediction.git
```

On successful completion of this command, a folder names "earth-quakes-analysis-and-prediction" will be created in the directory location with the source code of this research, then you can run the command below to switch to the root directory of the project in your terminal

````shell
cd earth-quakes-analysis-and-prediction
````

### Running without Docker
Before doing anything else, ensure `python` and its associated terminal helper command `pip` is installed and working on your computer. You can confirm that by running this command in the terminal
```shell
python3 --version && pip3 --version
```
or run the command below to confirm another version of `python` and `pip` is installed
```shell
python --verson && pip --version
```

If Python is installed and working, then you can proceed to the next step by installing the required libraries and packages using in this research experiment. You can do that by running the command below

```shell
pip3 install --trusted-host pypi.python.org -r requirements.txt
```

This command will install the following libraries and packages to your computer
`flask`, `numpy`, `pandas`, `jupyter`, `scikit-learn`, `keras`, and `folium`

#### Accessing the Jupyter notebook
To access the main experiment, run the command below in your terminal while still in the root folder of the project. 

```shell
jupyter notebook experiment.ipynb
```
This will start up the jupyter notebook server and auto redirect to a browser tab with the experiment open and ready to use. 
If that does not happen, copy and paste this url into your browser `http://localhost:8888/notebooks/experiment.ipynb`

### Running with Docker (API)
This project also provides a second setup that opens up the experiment, and it's output over different endpoints
To successfully set up and run this project, you need to have installed Docker desktop on your computer.
After installing docker desktop, you need to run this command to build your docker container
```shell
docker build -t my-api .
```
then run the command below to start the API
```shell
docker run -p 80:80 my-api
``` 

This will start the Docker container and map port 80 on the container to port 80 on your local machine. Ensure no other process in using port 80 on your computer before running these commands, if you do, ensure to disable the processes to keep the prot free.

#### Accessing Analysis & Predictions Endpoints
Visit `http://localhost` in your web browser to confirm everything works fine. Another test URL is provided to further confirm everything works.
`http://localhost/test-data`
Then you can further access each prediction algorithms through other endpoint which will be listed below


#### Limitation & Challenge of Current Docker Setup
You have to run `docker build -t my-api .` and `docker run -p 80:80 my-api` everytime you make updates to the files to view your new updates
