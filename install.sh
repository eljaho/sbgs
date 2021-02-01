#!/bin/sh

# Install prerequisites for germination.py
sudo apt install python3 python3-pip python3-setuptools aria2
sudo dnf install python3 python3-pip python3-setuptools aria2
sudo pacman -S python3 python3-pip python3-setuptools aria2
pip3 install validators pyquery
