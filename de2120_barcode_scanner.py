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
import time

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

    # Constructor
    def __init__(self, hard_port = None):
        if hard_port is None:
            # TODO: need to check if this is correct
            self.hard_port = serial.Serial("/dev/serial0/", 9600, timeout=1)
            # self.hard_port = serial.Serial("/dev/ttyS0", 9600, timeout=1)
        else:
            self.hard_port = hard_port
    
    # --------------------------------------------------------
    # begin()
    #
    # Initializes the device with basic settings. Returns false
    # if the device is not detected
    def begin(self):
        """
            Initializes the device with basic settings. Calls the 
            is_connected() function

            :return: Returns true if initialization was successful
            :rtype: bool
        """
        if self.is_connected() == False:
            return False
        
        # Clear any remaining incoming chars. This prevents a mis-read
        # of the first barcode
        self.hard_port.flush()

        # We're all setup
        return True
    
    # ---------------------------------------------------------
    # is_connected()
    #
    # Try to retrieve the firmware verison number as a test to 
    # determine whether the module is connected.
    def is_connected(self):
        """
            Ask the DE2120 for the firmware version.

            :return: Returns true if the DE2120 responds with an ACK.
            Retruns false otherwise.
            :rtype: bool
        """
        # So, we've already opened the port at a baude rate of 9600

        # Let's try getting the firmware version
        # It takes ~430 ms to get firmware version response
        if self.send_command(self.COMMAND_GET_VERSION, "", 800)  
            return True

        # If we failed, try again at the factory default of 115200 bps
        self.hard_port = serial.Serial("/dev/serial0/", 115200, timeout=1)

        time.sleep(0.01)

        # Go to 9600bps
        # 300 ms is too quick for module to switch to new setting
        self.send_command(self.PROPERTY_BAUD_RATE, "5", 500)

        # Return to 9600bps
        self.hard_port = serial.Serial("/dev/serial0/", 9600, timeout=1)

        time.sleep(0.01)

        # Let's try getting the firmware version again
        # It takes ~430 ms to get firmware version response
        if self.send_command(self.COMMAND_GET_VERION, "", 800)
            return True
        
        return False
    
    # ---------------------------------------------------------
    # factory_default()
    # 
    # Returns the DE2120 to factory default settings. This will 
    # disconnect the module from the serial port
    def factory_defaul(self):
        """
            Send command to put the module back into facory default
            settings. This will disconnect the module from the serial
            port.

            :return: True if command successfully received, false
            otherwise.
            :rtype: bool
        """
        return self.send_command(self.COMMAND_SET_DEFAULTS)
    
    # --------------------------------------------------------
    # available()
    #
    # Returns the number of bytes in the serial receive buffer
    def available(self):
        """
            :return: the number of bytes in the serial receive buffer
            :rtype: int
        """
        return self.hard_port.in_waiting()

    # --------------------------------------------------------
    # read()
    # 
    # Read byte from the serial port
    def read(self):
        """
            :return: the first byte on the serial port
            :rtype: int
        """
        return self.hard_port.read()
    
    # --------------------------------------------------------
    # send_command(cmd, arg, max_wait_in_ms)
    #
    # Construct a command/parameter and send it to the module.
    def send_command(self, cmd, arg = "", max_wait_in_ms = 3000):
        """
            Create command string and send to DE2120 over serial 
            port. Check serial buffer for a response

            :param cmd: The command name
            :param arg: The command variation, if there is one
            :param max_wait_in_ms: Maximum time to wait for ACK/NACK
            :return: True if the response from DE2120 contains the 
            ACK character, false otherwise.
            :rtype: bool
        """
        start = '^_^'
        end = '.'

        command_string = start + cmd + arg + end
        # Use encode() to turn string into bytes
        self.hard_port.write(command_string.encode())

        timeout = (time.time() * 1000) + max_wait_in_ms

        while (time.time() * 1000 < timeout):

            if self.hard_port.in_waiting():

                while self.hard_port.in_waiting():
                    incoming = self.hard_port.read()

                    if incoming == self.DE2120_COMMAND_ACK:
                        return True
                    
                    elif incoming == self.DE2120_COMMAND_NACK:
                        return False

            time.sleep(0.001) 
        
        return False
    
    # --------------------------------------------------------
    # read_barcode()
    #
    # Check the receive buffer for serial data from the barcode 
    # scanner.
    def read_barcode(self, result_buffer, size)
        """
            Check the receive buffer for a CR (marks a complete scan).
            If a CR is found, we overwrite the result_buffer until it's
            either full or we reach a CR in the receive buffer

            :param result_buffer: list that stores the barcode read from
                serial port
            :param size: size of the result_buffer
            :return: true if NULL character found in barcode, false other
            :rtype: bool
        """
        # Check if there's data available
        if self.hard_port.in_waiting() == False:
            return False

        cr_found = False

        for idx in (0, size):

            if result_buffer[idx] == '\r':
                cr_found = True
        
        if cr_found:
            result_buffer[0] = '\0'
        
        for idx in (len(result_buffer), size):

            if self.hard_port.in_waiting():
                result_buffer[idx] = self.hard_port.read()
            
                if result_buffer[idx] == '\r': 
                    result_buffer[idx+1] = '\0'
                    return True
            
            else
                return False
        
        return False
    
    # -------------------------------------------------------
    # change_baud_rate(baud)
    #
    # Change the serial baud rate for the barcode module
    def change_baud_rate(self, baud):
        """
            Change the serial baud rate for the barcode module.
            Default 115200

            :param baud: baud rate to change to
            :return: true if command is successfully send, false otherwise
            :rtype: bool
        """
        # TODO: The following line is the C++ code of the arduino library,
        # I have no idea what it does
        # char arg[2] = {'0', '\0'};

        if baud = 1200:
            arg = '2'
        elif baud = 2400:
            arg = '3'
        elif baud = 4800:
            arg = '4'
        elif baud = 9600:
            arg = '5'
        elif baud = 19200:
            arg = '6'
        elif baud = 38400:
            arg = '7'
        elif baud = 57600:
            arg = '8'
        elif baud = 115200:
            arg = '9'

        # Only change the baud rate if a valid value is passed
        if arg != '0':
            return self.send_command(self.PROPERTY_BAUD_RATE, arg)
        
        return False
    
    # --------------------------------------------------------
    # change_buzzer_tone(tone)
    #
    # Change the beep frequency between low, med, and high
    def change_buzzer_tone(self, tone):
        """
            Change the buzzer frequency between low, med, and high

            :param tone: int that's 1 = low, 2 = med, 3 = high frequency
            :return: true if command is successfully sent, false otherwise
            :rtype: bool
        """
        # Only change the frequency if a valid value is passes
        if tone > 0 and tone < 4:
            return self.send_command(self.PROPERTY_BUZZER_FREQ, tone)
        return False
    
    # --------------------------------------------------------
    # enable_decode_beep()
    #
    # Enable buzzer beep on successful read
    def enable_decode_beep(self):
        """
            Enable beep on successful read

            :return: true if command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_DECODE_BEEP, "1")
    
    # ---------------------------------------------------------
    # disable_decode_beep()
    #
    # Disable buzzer beep on successful read
    def disable_decode_beep(self):
        """
            Disable beep on successful read

            :return: true if command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_DECODE_BEEP, "0")

    # --------------------------------------------------------
    # enable_boot_beep
    #
    # Enable buzzer beep on module startup
    def enable_decode_beep(self):
        """
            Enable beep on module startup

            :return: true if command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_BOOT_BEEP, "1")
    
    # --------------------------------------------------------
    # disable_boot_beep
    #
    # Disable buzzer beep on module  startup
    def disable_boot_beep(self):
        """
            Disable beep on module startup

            :return: true if command successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_BOOT_BEEP, "0")
    
    # ---------------------------------------------------------
    # light_on()
    #
    # Turn white illumination LED on
    def light_on(self):
        """
            Turn white illumination LED on

            :return: true if command successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_FLASH_LIGHT, "1")
    
    # ---------------------------------------------------------
    # light_off()
    #
    # Turn white illumination LED off
    def light_off(self):
        """
            Turn white illumination LED off

            :return: true if command successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_FLASH_LIGHT, "0")
        
    # ---------------------------------------------------------
    # reticle_on()
    #
    # Turn red scan line on
    def reticle_on(self):
        """
            Turn red scan line on

            :return: true if command successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_AIM_LIGHT, "1")
    
    # ---------------------------------------------------------
    # reticle_off()
    #
    # Turn red scan line off
    def reticle_off(self):
        """
            Turn red scan line off

            :return true if command successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_AIM_LIGHT, "0")
    
    # ---------------------------------------------------------
    # change_reading_area()
    #
    # Change the percentage of the frame to scan for barcodes
    def change_reading_area(self, percent):
        """
            Change the percentage of the frame to scan for barcodes

            :param percent: Percentage of frame to scan. Valid values
                are 100, 80, 60, 40, 20 as stated in the DE2120 Scan
                Setting Manual
            :return: true if command successfully sent, false otherwise
            :rtype: bool
        """
        if percent = 80:
            arg = '1'
        elif percent = 60:
            arg = '2'
        elif percent = 40:
            arg = '3'
        elif percent = 20:
            arg = '4'
        else:   # Default to scanning 100% of the area
            arg = '0'
        
        # if arg != 0:
        #     return self.send_command(self.PROPERTY_READING_AREA, arg)
        
        # return False
        
        # TODO: couldn't all of this just be
        return self.send_command(self.PROPERTY_READING_AREA, arg)
    
    # ---------------------------------------------------------
    # enable_image_flipping()
    #
    # Enable mirror image reading as defined in the DE2120 Settings Manual
    def enable_image_flipping(self):
        """
            Enable mirror image reading

            :return: true if the command successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_MIRROR_FLIP, "1")
    
    # --------------------------------------------------------
    # disable_image_flipping()
    #
    # Disable mirror image reading as defined in the DE2120 Settings Manual
    def disable_image_flipping(self):
        """
            Disable mirror image reading

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_MIRROR_FLIP, "0")
    
    # ---------------------------------------------------------
    # USB_mode(mode)
    #
    # Enable USB communication and set the mode
    # THIS WILL MAKE THE MODULE UNRESPONSIVE ON TTL
    def USB_mode(self, mode):
        """
            Enable USB communication and set the mode. THIS WILL
            MAKE THE MODULE UNRESPONSIVE ON TTL

            :param mode: string defining what USB mode to set the 
                module in. Valid arguments are "KBD", "HID", "VIC".
            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        if mode == "KBD" or mode == "HID" or mode == "VIC":
            return self.send_command(self.PROPERTY_COMM_MODE, mode)
        
        return False
    
    # ----------------------------------------------------------
    # enable_continuous_read(repeat_interval)
    #
    # Enable continuous reading mode and set the interval for same-code reads
    def enable_continuous_read(self, repeat_interval):
        """
            Enable continuous reading of barcodes and set the time
            interval for same-code reads

            :param repeat_interval: int parameter.
                0: same code output 1 times
                1: continuous output with same code without interval
                2: continuous output with same code, 0.5 second interval
                3: continuous output with same code, 1 second interval
            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        if repeat_interval < 4 and repeat_interval >= 0:
            self.send_command(self.PROPERTY_READING_MODE, "CNT")
            return self.send_command(self.PROPERTY_CONTINUOUS_MODE_INTERVAL, repeat_interval)
        
        return False
    
    # ---------------------------------------------------------
    # disable_continuous_read()
    #
    # Disable continuous reading mode
    def disable_continuous_read(self):
        """
            Disable continuous reading of barcodes.

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_READING_MODE, "MAN")
    
    # ---------------------------------------------------------
    # enable_motion_sense(sensitivity)
    #
    # Enable the motion sensitive read mode.
    def enable_motion_sense(self, sensitivity):
        """
            Enable the motion sensitive read mode and set sensitivity level

            :param sensitivity: int value. The smaller the sensitivity, the
                more sensitive. Values are taken from the DE2120 settings manual.
                Valid arguments are: 15 (very high), 20 (high), 30 (little high), 
                50 (general/default), 100 (low sensitivity)
            :return: true if command is successfully sent, false otherwise
            :rtype: bool
        """
        # Reject invalid sensitivity values
        if sensitivity == 15 or sensitivity == 20 or sensitivity == 30 or sensitivity == 50 or sensitivity == 100:
            sense = str(sensitivity)

            self.send_command(self.PROPERTY_READING_MODE, "MDH")
            return self.send_command(self.PROPERTY_COMM_MODE, sense)

        return False

    # ---------------------------------------------------------
    # disable_motion_sense()
    # 
    # Disable the motion sensitive read mode.
    def disable_motion_sense(self):
        """
            Disable the motioin sensitive read mode.

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_READING_MODE, "MAN")

    # ---------------------------------------------------------
    # enable_all_1D()
    # 
    # Enable decoding of all 1D symbologies
    def enable_all_1D(self):
        """
            Enable decoding of all 1D symbologies

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_ENABLE_ALL_1D)
    
    # ---------------------------------------------------------
    # disable_all_1D()
    #
    # Disable decoding of all 1D symbologies
    def disable_all_1D(self):
        """
            Disable decoding of all 1D symbologies

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_DISABLE_ALL_1D)

    # ---------------------------------------------------------
    # enable_all_2D()
    #
    # Enable decoding of all 2D symbologies
    def enable_all_2D(self):
        """
            Enable decoding of all 2D symbologies

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_ENABLE_ALL_2D)
    
    # --------------------------------------------------------
    # disable_all_2D()
    #
    # Disable decoding of all 2D symbologies
    def disable_all_2D(self):
        """
            Disable decoding of all 2D symbologies

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.PROPERTY_DISABLE_ALL_2D)
    
    # ---------------------------------------------------------
    # start_scan()
    # 
    # Start reading when in trigger mode (default)
    def start_scan(self):
        """
            Start reading when in trigger mode (default)

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.COMMAND_START_SCAN)
    
    # ----------------------------------------------------------
    # stop_scan()
    #
    # Stop reading when in trigger mode. Module will automatically
    # stop reading after a few seconds
    def stop_scan(self):
        """
            Stop reading when in trigger mode. Module will
            automatically stop reading after a few seconds

            :return: true if the command is successfully sent, false otherwise
            :rtype: bool
        """
        return self.send_command(self.COMMAND_STOP_SCAN)