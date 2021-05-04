#!/usr/bin/env python
#-----------------------------------------------------------------------------
# de2120_ex3_send_command.py
#------------------------------------------------------------------------
#
# Written by Priyanka Makin @ SparkFun Electronics, April 2021
#
# This example demonstrates how to use the "send_command()" method to send 
# arbitrary serial commands to the barcode reader. It also demonstrates the "CIDENA"
# or "Code ID Enable" function, which includes the barcode type when transmitting the
# decoded string.
#
# send_command() takes two strings as arguments, concatenate them, adds the command
# prefix "^_^" and the command suffix "." and then transmits the command to the module.
# For example, to enable matrix 2 of 5 scanning, which is done using the command
# "^_^M25ENA1." you would make the call "my_scanner.send_command("M25ENA", 1)"
#
# While it is valid to call "my_scanner.send_command("M25ENA1")", the former method
# is preferred in many cases.
# 
# NOTE: you must put the module into COM mode by scanning the PORVIC barcode 
# in the datasheet. This will put the module in the correct mode to receive 
# and transmit serial.
#
# This package has been developed on a Raspberry Pi 4. Connect the DE2120 Barcode
# Scanner Breakout directly to your Pi using a USB-C cable
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
# Example 3

from __future__ import print_function
import de2120_barcode_scanner
import time
import sys

def run_example():

    print("\nSparkFun DE2120 Barcode Scanner Breakout Example 3")
    my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()

    if my_scanner.begin() == False:
        print("\nThe Barcode Scanner module isn't connected correctly to the system. Please check wiring", \
            file=sys.stderr)
        return
    print("\nScanner ready!")

    print("\n")
    print("\nTransmit Code ID with Barcode? (y/n)")
    print("\n---------------------------------------------")

    val = input("\nType 'y' or 'n' or scan a barcode: ")

    if val == 'y':
        print("\nCode ID will be displayed on scan")
        my_scanner.send_command("CIDENA", "1")
    elif val == 'n':
        print("\nCode ID will NOT be displayed on scan")
        my_scanner.send_command("CIDENA", "0")
    else:
        print("\nCommand not recognized")
            
    scan_buffer = ""
    
    while True:
        scan_buffer = my_scanner.read_barcode()
        if scan_buffer:
            print("\nCode found: ")
            print("\n" + str(scan_buffer))
            scan_buffer = ""
        
        time.sleep(0.02)


if __name__ == '__main__':
    try: 
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 3")
        sys.exit(0)
