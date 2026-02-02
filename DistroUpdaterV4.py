#!/usr/bin/python


import os
import sys
import time
import platform

apt1 = " apt update"
apt2 = " apt upgrade" 
arch1 = " pacman -Syu"
fedora = " dnf upgrade --refresh"
tmx1 = " pkg update"
tmx2 = " pkg upgrade"
plfm = platform.system()
lnxunr = os.system("uname -r")
andrd = os.environ.get("PREFIX")
os.system ("clear")
distroassci = r"""
  ___  _    _             _   _          _      _           
 |   \(_)__| |_ _ _ ___  | | | |_ __  __| |__ _| |_ ___ _ _ 
 | |) | (_-<  _| '_/ _ \ | |_| | '_ \/ _` / _` |  _/ -_) '_|
 |___/|_/__/\__|_| \___/  \___/| .__/\__,_\__,_|\__\___|_|  
                               |_|                          
"""

print(distroassci)



if plfm == "Linux" and os.path.exists("/etc/arch-release"):
        os.system("sudo" + arch1)
        os.system("clear")
      
elif plfm == "Linux" and os.path.exists("/etc/debian_version"):
          os.system("sudo" + apt1)
          os.system("sudo" + apt2)
          os.system("clear")

elif plfm == "Linux" and os.path.exists("/etc/fedora-release"):
          os.system("sudo" + fedora)
          os.system("clear")
          

elif plfm == "Linux" and andrd == "/data/data/com.termux/files/usr":
          os.system(tmx1)
          os.system(tmx2)
          os.system("clear")
        

answer = input("Would you like to reboot now? It is highly recommended: ")

if answer == "yes" or  answer == "y":
    print("Rebooting in 5 seconds....")
    time.sleep(5)
    os.system("reboot")

elif answer == "no" or answer == "n":
    os.system("clear")
    quit()

else:
    print("No option selected, exiting.....")
    quit()