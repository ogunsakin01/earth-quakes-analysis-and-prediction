# Earth Quakes Prediction Using ML
### System Requirements
- Docker
- Python3
- Keras
- Flask
- Numpy
- Pandas
- Jupyter
- Sklearn
- Folium

### Installation & Setup
To successfully set up and run this project, you need to have installed Docker desktop on your computer. You can install from this link https://docs.docker.com/engine/install/
After installing docker desktop, you need to run this command `docker build -t my-api .` and `docker run -p 80:80 my-api
` This will start the Docker container and map port 80 on the container to port 80 on your local machine. Ensure no other process in using port 80 on your computer before running these commands, if you do, ensure to disable the processes to keep the prot free.

### Running Jupyter Notebook without the container
Ensure you have python installed on your computer and then run the command below to have Jupyter and other required tools installed by running this command in the root folder of the project
````shell
pip3 install --trusted-host pypi.python.org -r requirements.txt
````

After successful installation of the required tools and packages, then run the command below to start your jupyter server
````shell
jupyter notebook
````
This will launch the jupyter server and make it available through the URL http://localhost:8889/. From the URL, select the `experiment.ipynb` and have access to the results 
### Accessing Prediction Endpoints
Visit http://localhost/ in your web browser to confirm everything works fine. Another test URL is provided to further confirm everything works.
http://localhost/test-data
Then you can further access each prediction algorithms through the endpoints below.


`/test-data` 


### Limitation & Challenge

You have to run `docker build -t my-api .` and `docker run -p 80:80 my-api` everytime you make updates to the files to view your new updates
