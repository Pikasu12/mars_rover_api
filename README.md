# MARS ROVER API

## Overview
This project is written in Python3 will perform download and store images locally from [NASA API website](https://api.nasa.gov/).

## Instruction on running the program.
### We have 2 options to up and run the program.

### 1. Run and deploy via docker container (Recommended).
#### This option is only tested using the following linux flavors (Ubuntu, centos).
#### ***Note:*** *Deployment in other operating systems such as Windows and Mac is not yet tested.*
#### - First clone the program github repository: https://github.com/Pikasu12/mars_rover_api.git
#### - Perform the following command.
```
git clone https://github.com/Pikasu12/mars_rover_api.git
cd mars_rover_api
docker-compose up              <----- Building the image takes sometime depending on the speed of the internet. (Estimated time: 5mins - 10mins)
```
#### ***Note:*** *If the docker-compose is not yet install you can find the installation process [here](https://docs.docker.com/compose/install/)*
#### - Once the downloading of image is done and  the container is exited. you can verify the images downloaded by executing the following command.
```
docker commit $(docker ps -a|grep "backend"|awk '{print $1}') debug/backend   <--- We create new image from the exited image.
docker run -it --rm --entrypoint sh debug/backend                             <--- Here we will run the newly created image that contains the downloaded image.
cd images                                                                     <--- Go to the images directory and explore the images downloaded.
exit
```

### 2. Run and deploy locally using your prefered terminal.
#### - First clone the program github repository: https://github.com/Pikasu12/mars_rover_api.git
```
git clone https://github.com/Pikasu12/mars_rover_api.git 
```
#### Perform the following command to run the program. (Python package is required to perform the below commands)
```
For ubuntu:
apt-get install -y python3-venv           <---- To install virtual env library (Recommended)
sudo python3 -m venv venv                 <---- to create your own virtual env. (Recommended)
source venv/bin/activate                  <---- To activate the virtual env. (Recommended)
cd mars_rover_api/backend                 <---- Go inside to the backend folder.
pip install -r requirements.txt           <---- To install the needed library to run the program.
python server.py

For Windows:
cd mars_rover_api/backend
pip install -r requirements.txt
python server.py
cd images                                 <---- To view the downloaded images.
```
#### ***Note:*** *It may take sometime to download all the images. You can view the donwloaded images in this directory 'backend/image/<image_date>/<image_files>'*

## How to run unittest
### Our unittest in python must run before deploying the program to ensure it's quality, follow the instructions below.
#### 1. Install the needed libraries. (This command is for ubuntu OS)
```
apt-get install -y python3-venv           <---- To install virtual env library (Recommended)
sudo python3 -m venv venv                 <---- to create your own virtual env. (Recommended)
source venv/bin/activate                  <---- To activate the virtual env. (Recommended)
cd mars_rover_api/backend                 <---- Go inside to the backend folder.
pip install -r requirements.txt           <---- To install the needed library to run our unittest. (Please proceed even though some library failed to install.)
nose2                                     <---- To run all the unittest, expected result is 4 test pass.
```