# MARS ROVER API

## Overview
This project will perform download and store images locally from [NASA API website](https://api.nasa.gov/).

## Instruction on running the program.
### We have 2 options to up and run the program.

### 1. Run and deploy via docker container (Recommended).
#### This option is only tested using the following linux flavors (Ubuntu, centos).
#### ***Note:*** *Deployment in other operating systems such as Windows and Mac is not yet tested.*
#### - First clone the program github repository: (https://github.com/Pikasu12/mars_rover_api.git)[https://github.com/Pikasu12/mars_rover_api.git]
#### - Perform the following command.
```
cd mars_rover_api
docker-compose up
```
#### ***Note:*** *If the docker-compose is not yet install you can find the installation process (here.)[https://docs.docker.com/compose/install/]*
#### - Once the 
### 2. Run and deploy locally using your prefered terminal.
#### This option required two terminal since we use 2 ports, 1 for our frontend written in React JS and 1 for the backend written in Python.


## How to run unittest
### Our unittest in python must run before deploying the program to ensure it's quality.
### Follow the instructions below.
#### 1. Go to the backend directory which our python package root is located.
#### 2. You must ensure the nose2 is installed. *"Note: If you deploy the program via docker container this library is already installed"*
#### 3. Perform the command below:
```
nose2
```
#### 4. The result must show the total test run and the overall all status of the test.


## Instruction on how to use.
