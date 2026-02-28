#!/bin/bash 

pkgver=6.0

cd /tmp

clear

echo "Downloading from source"

curl -LO https://github.com/digitalencryption/DistroUpdater/releases/download/$pkgver/DistroUpdaterV6.zip

clear

echo "Unzipping the file"

unzip DistroUpdaterV6.zip

clear

echo "Installing DistroUpdater"

sudo install -Dm755 /tmp/DistroUpdaterV6.py /usr/bin/distroupdater

echo "DistroUpdater installed, Run distroupdater in your terminal to start updating!"