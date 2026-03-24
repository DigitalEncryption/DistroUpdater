#!/usr/bin/python


import os
import sys
import time
import platform

args = sys.argv[1:]
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

if "install" in args:
    if plfm == "Linux" and os.path.exists("/etc/fedora-release"):
        pkgname = input("What package would you like to install? ")
        os.system("sudo dnf install " + pkgname)
        os.system("clear")
        print(distroassci)
        print("Done!")
        quit()
    if plfm == "Linux" and os.path.exists("/etc/debian-release"):
        pkgname = input("What package would you like to install? ")
        os.system("sudo apt install " + pkgname)
        print(distroassci)
        print("Done!")
        quit()
    if plfm == "Linux" and os.path.exists("/etc/arch-release"):
        pkgname = input("What package would you like to install? ")
        os.system("sudo pacman -S " + pkgname)
        os.system("clear")
        print(distroassci)
        print("Done!")
        quit()
    if plfm == "Darwin" and os.path.exists("/etc/bashrc_Apple_Terminal"):
        print("Sorry, macOS isn't supported for installing applications, quiting.....")
        quit()
    if plfm == "Linux" and andrd == "/data/data/com.termux/files/usr":
        pkgname = input("What would you like to install? ")
        os.system("pkg install " + pkgname)
        os.system("clear")
        print(distroassci)
        print("Done!")
        quit()
    if plfm == "Linux" and os.path.exists("/etc/freebsd-update.conf"):
        pkgname = input("What package would you like to install? ")
        os.system("sudo pkg install " + pkgname)
        os.system("clear")
        print(distroassci)
        print("Done!")
        quit()
    if plfm == "Linux" and os.path.exists("/etc/zypp"):
        pkgname = input("What package would you like to install? ")
        os.system("sudo zypper install " + pkgname)
        os.system("clear")
        print(distroassci)
        print("Done!")
        quit()
    if plfm == "Linux" and os.path.exists("/etc/NIXOS"):
        pkgname = input("What package would you like to install? ")
        os.system("nix profile install nixpkgs#" + pkgname)
        os.system("clear")
        print(distroassci)
        print("Done!")
        quit()
    if pflm == "Linux" and os.path.exists("/etc/redhat-release"):
        ver = input("If your version of RHEL is below 8, say yes, if not say no")
        if ver == "yes" or "y":
            pkgname = input("What package would you like to install? ")
            os.system("sudo yum install" + pkgname)
            os.system("clear")
            print(distroassci)
            print("Done!")
            quit()
        if ver == "no" or "n":
            pkgname = input("What package would you like to install? ")
            os.system("sudo dnf install " + pkgname)
            os.system("clear")
            print(distroassci)
            print("Done!")
            quit()
        else:
            print("No option selected, exiting.....")
            quit()
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
    ver = input("If your version of RHEL is below 8, say yes, if not say no")
    if ver == "yes" or "y":
     os.system("sudo yum update -y")
     os.system("clear")
    if ver == "no" or "n":
     os.system("sudo dnf upgrade --refresh -y")
     os.system("clear")
elif plfm == "Linux" and os.path.exists("etc/gentoo-release"):
    os.system("sudo emerge -avDuN world")
    os.system("clear")
elif plfm == "Linux" and os.path.exists("/etc/slackware-version"):
    os.system("slackpkg update gpg")
    os.system("slackpkg update")
    os.system("slackpkg upgrade-all")
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


        
