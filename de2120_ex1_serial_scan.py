#!/usr/bin/env python
#-----------------------------------------------------------------------------
# qde2120_ex1_serial_scan.py
#------------------------------------------------------------------------
#
# Written by Priyanka Makin @ SparkFun Electronics, April 2021
#
# This example demonstrates how to get the scanner connected and will output
# and barcode it sees.
# 
# NOTE: you must put the module into TTL mode by scanning the POR232 barcode 
# in the datasheet. This will put the module in the correct mode to receive 
# and transmit serial. This package will automatically set the baud rate to 9600 bps.
#
# This package has been developed on a Raspberry Pi 3. To connect:
#
# (Raspberry Pi pin) = (Scanner pin)
# GPIO 14 (TXD) = RX pin
# GPIO 15 (RXD) = TX pin
# GND = GND
# 3.3V = 3.3V
#  
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2021 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
# Example 1

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

    BUFFER_LEN = 40
    scan_buffer = [None] * BUFFER_LEN

    while True:

        if my_scanner.read_barcode(scan_buffer, BUFFER_LEN):
            print("\nCode found: ")
            for i in range(0, len(scan_buffer):
                print(scan_buffer[i])
            print("\n")
        
        time.sleep(0.2)
    
if __name__ == '__main__':
    try:
        run_example()
    except(KeyboarInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
