SPKY.GPIO README

SPKY.GPIO is a GPIO library that can support Sparky. The API is the compatible with RPi.GPIO for Raspberry Pi. [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO).

You can donwload the SPKY.GPIO from:
https://github.com/sparkysbc/SPKY.GPIO.
## Support Hardware
    Banana Pro/Pi
    Sparky SBC

## Download
	git clone https://github.com/sparkysbc/SPKY.GPIO.git
    

## Installation
    sudo apt-get update
    sudo apt-get install python-dev
    cd /SPKY.GPIO
    python setup.py install                 
    sudo python setup.py install
    
Please be attention that you need use both python and sudo pytohn to make the SPKY.GPIO work well.

## Remove
    cd /usr/local/lib/python2.7/dist-packages/
    sudo rm -r SPKY
    
Note that the SPKY library might be under /usr/lib/python2.7/dist-packages/, depending your system path setup. Remove the folder SPKY and the python egg info file.

## Examples
Under source/test directory, there are some examples.
under the source/test directory, there are some eaxmples for reference.
