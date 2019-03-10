#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install build-essential cmake pkg-config -y
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
sudo apt-get install libgtk2.0-dev libgtk-3-dev -y
sudo apt-get install libatlas-base-dev gfortran -y

sudo apt-get install python3-dev -y
sudo apt-get install python3-pip -y

pip3 install opencv-python
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libqtgui4 -y
sudo apt install libqt4-test -y
sudo modprobe bcm2835-v4l2 -y


python3 -m pip install opencv-contrib-python
sudo apt-get install libhdf5-dev -y
sudo apt-get install libhdf5-serial-dev -y
