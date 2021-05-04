#!/usr/bin/env python
#-----------------------------------------------------------------------------
# de2120_ex2_serial_settings.py
#------------------------------------------------------------------------
#
# Written by Priyanka Makin @ SparkFun Electronics, April 2021
#
# This example demonstrates how to configure the settings of the DE2120 Breakout
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
# Example 2

from __future__ import print_function
import de2120_barcode_scanner
import time
import sys
import serial

def flash_light(bar_scanner):
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Enable flash light")
    print("\n2) Disable flash light")
    print("\n------------------------------------------------")
    
    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nWhite scan light on")
        bar_scanner.light_on()
    elif val == '2':
        print("\nWhite scan light off")
        bar_scanner.light_off()
    else:
        print("\nCommand not recognized")

def reticle(bar_scanner):    
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Enable reticle")
    print("\n2) Disable reticle")
    print("\n------------------------------------------------")

    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nRed scan reticle on")
        bar_scanner.reticle_on()
    elif val == '2':
        print("\nRed scan reticle off")
        bar_scanner.reticle_off()
    else:
        print("\nCommand not recognized")
    
def decode_beep(bar_scanner):
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Enable decode beep")
    print("\n2) Disable decode beep")
    print("\n------------------------------------------------")
    
    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nDecode beep turned on")
        bar_scanner.enable_decode_beep()
    elif val == '2':
        print("\nDecode beep turned off")
        bar_scanner.disable_decode_beep()
    else:
        print("\nCommand not recognized")
        
def boot_beep(bar_scanner):
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Enable beep on module power on")
    print("\n2) Disable beep on module power off")
    print("\n------------------------------------------------")
    
    val = input("\nSelect an option number: ")
    
    if val == '1':
        print("\nBeep on power on enabled")
        bar_scanner.enable_boot_beep()
    elif val == '2':
        print("\nBeep on power on disabled")
        bar_scanner.disable_boot_beep()
    else:
        print("\nCommand not recognized")
        
def change_buzz_freq(bar_scanner):
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Passive low frequency")
    print("\n2) Passive medium frequency")
    print("\n3) Passive high frequency")
    
    val = input("\nSelect an option number: ")
    
    if val == '1':
        bar_scanner.change_buzzer_tone(int(val))
    elif val == '2':
        bar_scanner.change_buzzer_tone(int(val))
    elif val == '3':
        bar_scanner.change_buzzer_tone(int(val))
    else:
        print("\nCommand not recognized")

def image_flip(bar_scanner):
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Turn on image flipping")
    print("\n2) Turn off image flipping (default)")
    print("\n------------------------------------------------")
    
    val = input("\nSelect an option number: ")
    
    if val == '1':
        bar_scanner.enable_image_flipping()
    elif val == '2':
        bar_scanner.disable_image_flipping()
    else:
        print("\nCommand not recognized")
def reading_area(bar_scanner):
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
        bar_scanner.change_reading_area(100)
    elif val == '2':
        print("\nScanning center 80% of frame")
        bar_scanner.change_reading_area(80)
    elif val == '3':
        print("\nScanning center 60% of frame")
        bar_scanner.change_reading_area(60)
    elif val == '4':
        print("\nScanning center 40% of frame")
        bar_scanner.change_reading_area(40)
    elif val == '5':
        print("\nScanning center 20% of frame")
        bar_scanner.change_reading_area(20)
    else:
        print("\nCommand not recognized")

def reading_mode(bar_scanner):
    print("\n")
    print("\n------------------------------------------------")
    print("\n1) Manual read mode (default)")
    print("\n2) Continuous read mode")
    print("\n3) Motion sensor mode")
    print("\n------------------------------------------------")

    val = input("\nSelect an option number: ")

    if val == '1':
        print("\nManual trigger mode enabled")
        bar_scanner.enable_manual_trigger()
    elif val == '2':
        print("\nContinuous read mode enabled")
        bar_scanner.enable_continuous_read(1)
    elif val == '3':
        print("\nMotion trigger mode enabled")
        bar_scanner.enable_motion_sense()
    else:
        print("\nCommand not recognized")

def symbologies(bar_scanner):
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
        bar_scanner.enable_all_1D()
    elif val == '2':
        print("\n1D symbologies disabled")
        bar_scanner.disable_all_1D()
    elif val == '3':
        print("\n2D symbologies enabled")
        bar_scanner.enable_all_2D()
    elif val == '4':
        print("\n2D symbologies disabled")
        bar_scanner.disable_all_2D()
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
        
        print("\n")
        print("\nSparkFun DE2120 Barcode Scanner Python Package")
        print("\n------------------------------------------------")
        print("\n1) Start Scan")
        print("\n2) Stop Scan")
        print("\n3) Enable/Disable Flashlight")
        print("\n4) Enable/Disable Aiming Reticle")
        print("\n5) Enable/Disable Decode Beep")
        print("\n6) Enable/Disable Start Up Beep")
        print("\n7) Change Buzzer Frequency")
        print("\n8) Enablde/Disable Image Flipping")
        print("\n9) Set Reading Area")
        print("\n10) Set Reading Mode")
        print("\n11) Enable/Disable Symbologies")
        print("\n------------------------------------------------")

        val = input("\nSelect an option number: ")

        if val == '1':
            my_scanner.start_scan()
        elif val == '2':
            my_scanner.stop_scan()
        elif val == '3':
            flash_light(my_scanner)
        elif val == '4':
            reticle(my_scanner)
        elif val == '5':
            decode_beep(my_scanner)
        elif val == '6':
            boot_beep(my_scanner)
        elif val == '7':
            change_buzz_freq(my_scanner)
        elif val == '8':
            image_flip(my_scanner)
        elif val == '9':
            reading_area(my_scanner)
        elif val == '10':
            reading_mode(my_scanner)
        elif val == '11':
            symbologies(my_scanner)
        else:
            print("\nCommand not recognized")

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 2")
        sys.exit(0)
