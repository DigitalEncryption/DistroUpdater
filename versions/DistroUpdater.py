import os
import time
import sys 

#Variables
args = sys.argv[1:]
arch1 = "sudo pacman -Syu"
deb1 = "sudo apt update && sudo apt upgrade"
fedora1 = "sudo dnf upgrade --refresh"


if "--arch" in args:
    os.system(arch1)
    print("Updates finished, rebooting in 5 seconds")
    time.sleep(5)
    os.system("reboot")
elif "--debian" in args:
    os.system(deb1)
    print("Updates finished, rebooting in 5 seconds")
    time.sleep(5)
    os.system("reboot")   
elif "--fedora" in args:
    os.system(fedora1)
    print("Updates finished, rebooting in 5 seconds")
    time.sleep(5)
    os.system("reboot")

else: 
    print("No arguments detected, please add --arch, --fedora or --debian depending on your distro")
    

 
