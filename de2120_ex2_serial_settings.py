#!/usr/bin/env python
#-----------------------------------------------------------------------------
# de2120_ex2_serial_settings.py
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
# Example 2

from __future__ import print_function
import de2120_barcode_scanner
import time
import sys
import serial

# TODO: do i even need the flush_rx() function?!

def flash_light():
    # flush_rx()  # Clear the serial rx buffer to avoid line endings

    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Enable flash light")
    print("\n2) Disable flash light")
    print("\n------------------------------------------------")
    
    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nWhite scan light on")
        my_scanner.light_on()
    elif val == '2':
        print("\nWhite scan light off")
        my_scanner.light_off()
    else:
        print("\nCommand not recognized")

def reticle():
    # flush_rx()  # Clear the serial rx buffer to avoid line endings
    
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Enable reticle")
    print("\n2) Disable reticle")
    print("\n------------------------------------------------")

    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nRed scan reticle on")
        my_scanner.reticle_on()
    elif val == '2':
        print("\nRed scan reticle off")
        my_scanner.reticle_off()
    else:
        print("\nCommand not recognized")
    
def reading_area():
    # flush_rx()  # Clear the serial rx buffer ot avoid line endings

    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Full width (default)")
    print("\n2) Center 80%")
    print("\n3) Center 60%")
    print("\n4) Center 40%")
    print("\n5) Center 20%")
    print("\n------------------------------------------------")
    
    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nScanning 100% of frame")
        my_scanner.change_reading_area(100)
    elif val == '2':
        print("\nScanning center 80% of frame")
        my_scanner.change_reading_area(80)
    elif val == '3':
        print("\nScanning center 60% of frame")
        my_scanner.change_reading_area(60)
    elif val == '4':
        print("\nScanning center 40% of frame")
        my_scanner.change_reading_area(40)
    elif val == '5':
        print("\nScanning center 20% of frame")
        my_scanner.change_reading_area(202)
    else:
        print("\nCommand not recognized")

def reading_mode():
    # flush_rx()  # Clear the serial rx buffer

    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Manual read mode (default)")
    print("\n2) Continuous read mode")
    print("\n3) Motion sensor mode")
    print("\n------------------------------------------------")

    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nManual trigger mode enabled")
        my_scanner.disable_motion_sense()
    elif val == '2':
        print("\nContinuous read mode enabled")
        my_scanner.enable_continuous_read()
    elif val == '3':
        print("\nMotion trigger mode enabled")
        # TODO: do i need to set a sensitivity here??
        my_scanner.enable_motion_sense()
    else:
        print("\nCommand not recognized")

def symbologies():
    # flush_rx()  # Clear the rx buffer to avoid line endings

    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Enable all 1D symbologies")
    print("\n2) Disable all 1D symbologies")
    print("\n3) Enable all 2D symbologies")
    print("\n4) Disable all 2D symbologies")
    print("\n------------------------------------------------")

    val = input("\nSelect an option number: ")

    if val == '1':
        print("\n1D symbologies enabled")
        my_scanner.enable_all_1D()
    elif val == '2':
        print("\n1D symbologies disabled")
        my_scanner.disable_all_1D()
    elif val == '3':
        print("\n2D symbologies enabled")
        my_scanner.enable_all_2D()
    elif val == '4':
        print("\n2D symbologies disabled")
        my_scanner.disable_all_2D()
    else:
        print("\nCommand not recognized")

def run_example():

    print("\nSparkFun DE2120 Barcode Scanner Breakout Example 2")
    my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()

    if my_scanner.begin() == False:
        print("\nThe Barcode Scanner module isn't connected correctly to the system. Please check wiring", \
            file=sys.stderr)
        return
    print("\nScanner ready!")

    while True:

        flush_rx()  # Clear the serial rx buffer to avoid line endings
        
        print("\n")
        print("\nSparkFun DE2120 Barcode Scanner Python Package")
        print("\n------------------------------------------------")
        print("\n1) Start Scan")
        print("\n2) Stop Scan")
        print("\n3) Enable/Disable Flashlight")
        print("\n4) Enable/Disable Aiming Reticle")
        print("\n5) Set Reading Area")
        print("\n6) Set Reading Mode")
        print("\n7) Enable/Disable Symbologies")
        print("\n------------------------------------------------")

        # TODO: how to execute other code while waiting for user input?
        val = input("\nSelect an option number: ")

        if val == '1':
            my_scanner.start_scan()
        elif val == '2':
            my_scanner.stop_scan()
        elif val == '3':
            flashlight()
        elif val == '4':
            reticle()
        elif val == '5':
            reading_area()
        elif val == '6':
            reading_mode()
        elif val == '7':
            symbologies()
        else:
            print("\nCommand not recognized")

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 2")
        sys.exit(0)