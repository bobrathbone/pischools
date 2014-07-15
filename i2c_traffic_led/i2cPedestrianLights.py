#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# Traffic Light sequencer
# Bob Rathbone www.bobrathbone.com
# Adapted from code by Nathan Chantrell http://nathan.chantrell.net

# Licence GNU GPL V3 

import smbus
import time 
import atexit 

# Define bus - 0 for revision 1 boards or 1 for rev 2 
#bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# Define the MCP23017 expander banks
bankA = 0x13 
bankB = 0x12 

# Define the address of the expander
address = 0x20 # I2C address of MCP23017

bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to output 
bus.write_byte_data(0x20,0x00,0x80) # Set  A7 of bank A to input 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 

# Register exit routine
def finish():
       set_led(0,bankA)
       set_led(0,bankB)
       print("Program stopped")

atexit.register(finish)

# Write a byte to either bank A or B
def set_led(data,bank):
  ##print "bank "+ str(bank) + " data=" + str(data)
    bus.write_byte_data(address,bank,data)
    return

# Main routine for traffic light sequence
def main():
   # Make pin A7 high so we have +3.3v available for the switch
   plus3 = 2

   # Define the LEDs - For green led also make A7 high 
   green_led = 1 + plus3
   amber_led = 8
   red_led = 64

   while True:
       set_led(plus3,bankA)
       set_led(green_led,bankA)
       print "Green"
       buttonPressed = False
       while not buttonPressed:
           inp = bus.read_byte_data(address,bankB)
           if inp > 0:
               buttonPressed = True
               print "Button pressed value=" + str(inp)
           else:
               time.sleep(0.25)

       set_led(amber_led,bankA)
       print "Amber"
       time.sleep(3)
       set_led(red_led,bankA)
       print "Red"
       time.sleep(3)
     
       # Flash the amber light
       count = 5
       print "Flash Amber"
       while count > 0:
           set_led(amber_led,bankA)
           time.sleep(0.5)
           set_led(0,bankA)
           time.sleep(0.5)
           count = count-1

# Tell the program where to start
if __name__ == "__main__":
   main()

# End
