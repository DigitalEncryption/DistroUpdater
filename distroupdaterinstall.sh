#!/bin/bash 

pkgver=8.0

cd /tmp

clear

echo "Downloading from source"

curl -LO https://github.com/digitalencryption/DistroUpdater/releases/download/$pkgver/DistroUpdaterV8.zip

clear

echo "Unzipping the file"

unzip DistroUpdaterV8.zip

clear

echo "Installing DistroUpdater"

sudo install -Dm755 /tmp/DistroUpdaterV8.py /usr/bin/distroupdater

echo "DistroUpdater installed, Run distroupdater in your terminal to start updating!"