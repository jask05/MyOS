# -*- coding: utf-8 -*-
import subprocess
import os

logo = """
 ________  _________    ___      ___ 
|\  _____\|\___   ___\ |\  \    /  /|
\ \  \__/ \|___ \  \_| \ \  \  /  / /
 \ \   __\     \ \  \   \ \  \/  / / 
  \ \  \_|      \ \  \   \ \    / /  
   \ \__\        \ \__\   \ \__/ /   
    \|__|         \|__|    \|__|/    
"""

# Functions
def installPackage():
    # return subprocess.Popen("sudo apt-get install vim tmux fish", shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    return subprocess.Popen("sudo apt-get install audacity -y", shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")

def checkInstalledPackages():
    pass

# Texts
text1 = "[-] Install and configure Fish, Tmux and Vim."
text2 = "[+] Do you want to continue? (y/N) "
text3 = "[-] You will be asked for \"sudo password\" in order to install these packages."

# Main
print(logo)
print(text1)
confirm = input(text2) or "42"

if confirm.lower() == "y" or confirm.lower() == "s" or confirm.lower() == "yes" or confirm.lower() == "si":
    # Check if packages exist
    checkPackages = checkInstalledPackages()
    
    print(text3)
    proc = installPackage()
    proc.wait()