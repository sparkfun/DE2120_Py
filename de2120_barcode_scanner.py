#-----------------------------------------------------------------------------
# de2120_barcode_scanner.py
#
# Python library for the SparkFun 2D Barcode Scanner Breakout.
#   TODO: (check) https://www.sparkfun.com/products/15932
#
#------------------------------------------------------------------------
# Written by Priyanka Makin @ SparkFun Electronics, April 2021
#
# Do you like this library? Help support SparkFun. Buy a board!
#==================================================================================
# Copyright (c) 2020 SparkFun Electronics
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

"""
de2120_barcode_scanner
============
Python module for the 2D Barcode Scanner.

This python package is a port of the exisiting [SparkFun DE2120 Arduino Library](https://github.com/sparkfun/SparkFun_DE2120_Arduino_Library)

"""
#-----------------------------------------------------------------------------------

import serial

_DEFAULT_NAME = "DE2120 Barcode Scanner"

class DE2120BarcodeScanner(object):
    """
    DE2120BarcodeScanner 

    Initialize the library with the given port.

    :param hard_port:   The port to use to communicate with the module, this
                        is a serial port at 9600 baud rate.

    :return:            The DE2120BarcodeScanner object.
    :rtype:             Object
    """
    # Constructor
    device_name = _DEFAULT_NAME
    
    # DE2120 response
    DE2120_COMMAND_ACK = 0x06
    DE2120_COMMAND_NACK = 0x15

    # Send commands
    # Need to prepend "^_^" and append "."
    COMMAND_START_SCAN = "SCAN"
    COMMAND_STOP_SCAN = "SLEEP"
    COMMAND_SET_DEFAULTS = "DEFALT
    COMMAND_GET_VERSION = "DSPYFW"

    PROPERTY_BUZZER_FREQ = "BEPPWM"
    # BEPPWM0 - Active Drive
    # BEPPWM1 - Passive Low Freq
    # BEPPWM2 - Passive Med Freq (default)
    # BEPPWM3 - Passive Hi Freq

    PROPERTY_DECODE_BEEP = "BEPSUC"
    # BEPSUC1 - ON (default)
    # BEPSUC0 - OFF

    PROPERTY_BOOT_BEEP = "BEPPWR"
    # BEPPWR1 - ON (default)
    # BEPPWR0 - OFF

    PROPERTY_FLASH_LIGHT = "LAMENA"
    # LAMENA1 - ON (default)
    # LAMENA0 - OFF

    PROPERTY_AIM_LIGHT = "AIMENA"
    # AIMENA1 - ON (default)
    # AIMENA0 - OFF

    PROPERTY_READING_AREA = "IMGREG"
    # IMGREG0 - Full Width (default)
    # IMGREG1 - Center 80%
    # IMGREG2 - Center 60%
    # IMGREG3 - Center 40%
    # IMGREG4 - Center 20%

    PROPERTY_MIRROR_FLIP = "MIRLRE"
    # MIRLRE1 - ON
    # MIRLRE0 - OFF (default)

    PROPERTY_USB_DATA_FORMAT = "UTFEAN"
    # UTFEAN0 - GBK (default)
    # UTFEAN1 - UTF-8

    PROPERTY_SERIAL_DATA_FORMAT = "232UTF"
    # 232UTF0 - GBK (default)
    # 232UTF1 - UTF-8
    # 232UTF2 - Unicode BIG
    # 232UTF3 - Unicode little

    PROPERTY_INVOICE_MODE = "SPCINV"
    # SPCINV1 - ON
    # SPCINV0 - OFF (default)

    PROPERTY_VIRTUAL_KEYBOARD = "KBDVIR"
    # KBDVIR1 - ON (default)
    # KBDVIR0 - OFF

    PROPERTY_COMM_MODE = "POR"
    # PORKBD - USB-KBW Mode
    # PORHID - USB-HID Mode
    # PORVIC - USB-COM Mode
    # POR232 - TTL/RS232

    PROPERTY_BAUD_RATE = "232BAD"
    # 232BAD2 - 1200 bps
    # 232BAD3 - 2400 bps
    # 232BAD4 - 4800 bps
    # 232BAD5 - 9600 bps
    # 232BAD6 - 19200 bps
    # 232BAD7 - 38400 bps
    # 232BAD8 - 57600 bps
    # 232BAD9 - 115200 bps (default)

    PROPERTY_READING_MODE = "SCM"
    # SCMMAN - Manual (default)
    # SCMCNT - Continuous
    # SCMMDH - Motion Mode

    PROPERTY_CONTINUOUS_MODE_INTERVAL = "CNTALW"
    # CNTALW0 - Output Once
    # CNTALW1 - Output Continuous No Interval
    # CNTALW2 - Output Continuous 0.5s Interval
    # CNTALW3 - Output Continuous 1s Interval

    PROPERTY_MOTION_SENSITIVITY = "MDTTHR"
    # MDTTHR15 - Extremely High Sensitivity
    # MDTTHR20 - High Sensitivity (default)
    # MDTTHR30 - Highish Sensitivity
    # MDTTHR50 - Mid Sensitivity
    # MDTTHR100 - Low Sensitivity

    PROPERTY_TRANSFER_CODE_ID = "CIDENA"
    # CIDENA1 - Transfer Code ID
    # CIDENA0 - Do Not Transfer Code ID (default)

    PROPERTY_KBD_CASE_CONVERSION = "KBDCNV"
    # KBDCNV0 - No conversion (default)
    # KBDCNV1 - ALL CAPS
    # KBDCNV2 - all lowercase
    # KBDCNV3 - case-to-case

    # Barcode Style Enable/Disable
    PROPERTY_ENABLE_ALL_1D = "ODCENA"
    PROPERTY_DISABLE_ALL_1D = "ODCDIS"
    PROPERTY_ENABLE_ALL_2D = "AQRENA"
    PROPERTY_DISABLE_ALL_2D = "AQRDIS"
