#!/bin/sh

# Install prerequisites for germination.py
sudo apt install python3 python3-pip python3-setuptools aria2 libxslt-dev
sudo dnf install python3 python3-pip python3-setuptools aria2 libxslt-dev
sudo pacman -S python3 python3-pip python3-setuptools aria2 libxslt-dev
pip3 install validators pyquery
