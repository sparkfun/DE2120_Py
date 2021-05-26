DE2120_Py
===============

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/de2120-barcode-scanner/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/de2120-barcode-scanner.svg" /></a>
	<a href="https://github.com/sparkfun/DE2120_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/DE2120_Py.svg" /></a>
	<a href="https://de2120-py.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/de2120-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/DE2120_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>

</p>

<a href="https://www.sparkfun.com/products/18088"><img src="https://cdn.sparkfun.com/assets/parts/1/7/4/0/7/18088-SparkFun_2D_Barcode_Scanner-06.jpg"  align="right" width=300 alt="SparkFun 2D Barcode Scanner Breakout"></a>

Python module for the [SparkFun 2D Barcode Scanner Breakout - DE2120](https://www.sparkfun.com/products/18088).

This python package is a port of the existing [SparkFun DE2120 Arduino Library](https://github.com/sparkfun/SparkFun_DE2120_Arduino_Library)

## Contents

* [Supported Platforms](#supported-platforms)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Supported Platforms
--------------------
The Qwiic Button Python package current supports the following platforms:
* [Raspberry Pi](https://www.sparkfun.com/search/results?term=raspberry+pi)

Dependencies
--------------
This driver package depends on the pyserial package.

Documentation
-------------
The SparkFun 2D Barcode Scanner Breakout module documentation is hosted at [ReadTheDocs](https://de2120-py.readthedocs.io/en/latest/?)

Installation
---------------
### PyPi Installation

This repository is hosted on PyPi as the [de2120-barcode-scanner](https://pypi.org/project/de2120-barcode-scanner/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install de2120-barcode-scanner
```
For the current user:

```sh
pip install de2120-barcode-scanner
```
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install de2120-barcode-scanner-<version>.tar.gz
```

Example Use
 -------------
See the examples directory for more detailed use examples.

```python
from __future__ import print_function
import de2120_barcode_scanner
import time
import sys

def run_example():

    print("\nSparkFun DE2120 Barcode Scanner Breakout Example 1")
    my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()

    if my_scanner.begin() == False:
        print("\nThe Barcode Scanner module isn't connected correctly to the system. Please check wiring", \
            file=sys.stderr)
        return
    print("\nScanner ready!")

    scan_buffer = ""
    
    while True:
        scan_buffer = my_scanner.read_barcode()
        if scan_buffer:
            print("\nCode found: " + str(scan_buffer))
            scan_buffer = ""
        
        time.sleep(0.02)
    
if __name__ == '__main__':
    try:
        run_example()
    except(KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)

```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>
