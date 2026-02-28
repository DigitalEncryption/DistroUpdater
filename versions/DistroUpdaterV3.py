import os
import sys
import time
import platform

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
          os.system("sleep 5 && reboot")

elif plfm == "Linux" and andrd == "/data/data/com.termux/files/usr":
          os.system("pkg update && pkg upgrade")