#!/bin/bash

#run with $ yes | script

echo -e \\nCleaning Cache.....................................
sudo apt-get clean 

# Add PPAs
echo -e \\nAdding PPAs.......................................\\n
sudo add-apt-repository -y ppa:kupfer-team/ppa 

# System update
echo -e \\nUpdating List......................................\\n
sudo apt-get update && 

echo -e \\nUpgrading packages.................................\\n
sudo apt-get -y upgrade && 

echo Updating Distribution....................................\\n
sudo apt-get -y dist-upgrade 


# Install Softwares

echo -e \\nInstalling Softwares...............................\\n

sudo apt-get install -y kupfer plasma-nm dconf-tools powertop htop compizconfig-settings-manager deluge vlc smplayer chromium-browser python-software-properties 

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -

sudo apt-get install -y nodejs

sudo npm install -g npm

echo -e \\nCleaning...........................................\\n
sudo apt-get -y purge
