#coding=utf-8
import os, platform

bit=platform.architecture()[0]

if bit == "64bit":
    os.system("dpkg -i Muskan*.deb")
    os.system("Muskan")
elif bit == "32bit":
    import Waheed
    Waheed.wg()
