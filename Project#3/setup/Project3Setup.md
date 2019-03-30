# Installing Logitech Driver For PI
sudo apt-get install fswebcam
sudo usermod -a -G video pi

# Testing The Camera By Capturing the image
fswebcam -r 1280x720 --no-banner image.jpg

