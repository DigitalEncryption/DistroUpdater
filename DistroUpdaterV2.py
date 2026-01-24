import os
import sys
import time
import platform

plfm = platform.system()
lnxunr = os.system("uname -r")

os.system ("clear")
os.system ("cat banner.txt")


if plfm == "Linux" and os.path.exists("/etc/arch-release"):
        os.system("sudo pacman -Syu")
        os.system("clear")
        print ("Arch upgraded, restarting in 5 seconds.....")
        os.system("sleep 5 && reboot")

elif plfm == "Linux" and os.path.exists("/etc/debian_version"):
          os.system("sudo apt update && sudo apt upgrade")
          os.system("clear")
          print ("Debian upgraded, restarting in 5 seconds.....")
          os.system("sleep 5 && reboot")

elif plfm == "Linux" and os.path.exists("/etc/fedora-release"):
          os.system("sudo dnf upgrade --refresh")
          os.system("clear")
          print ("Fedora upgraded, restarting in 5 seconds.....")