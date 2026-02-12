#!/usr/bin/python


import os
import sys
import time
import platform


apt1 = " apt update"
apt2 = " apt upgrade -y" 
arch1 = " pacman -Syu --noconfirm"
fedora = " dnf upgrade --refresh -y"
tmx1 = " pkg update"
tmx2 = " pkg upgrade -y"
bsd = " freebsd-update fetch install"
bsd1 = " pkg upgrade -y"
mac = " softwareupdate --install --all"
suse = " zypper dup -y"
nix = " nixos-rebuild switch --upgrade"
rhel = " yum update"

plfm = platform.system()
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
        
elif plfm == "Linux" and os.path.exists("/etc/freebsd-update.conf"):
    os.system("sudo" + bsd)
    os.system("sudo" + bsd1)
    os.system("clear")   

elif plfm == "Darwin" and os.path.exists("/etc/bashrc_Apple_Terminal"):
    os.system("sudo" + mac)
    os.system("clear")

elif plfm == "Linux" and os.path.exists("/etc/zypp"):
     os.system("sudo" + suse)
     os.system("clear")

elif plfm == "Linux" and os.path.exists("/etc/NIXOS"):
     os.system("sudo" + nix)
     os.system("clear")

elif plfm == "Linux" and os.path.exists("/etc/redhat-release"):
     os.system("sudo" + rhel)
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
    os.system("clear")
    print("No option selected, exiting.....")
    quit()