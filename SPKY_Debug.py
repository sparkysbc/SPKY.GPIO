import os

os.chdir("/usr/local/lib/python2.7/dist-packages/")
os.system("sudo rm SPKY.GPIO-0.0.1.egg-info")
os.system("sudo rm -r SPKY")

os.chdir("/home/rapi/SPKY.GPIO/")
os.system("python setup.py install")
os.system("sudo python setup.py install")

os.chdir("/home/rapi/SPKY.GPIO/test/")
os.system("sudo python led.py")
