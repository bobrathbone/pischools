#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# Traffic Light sequencer
# Bob Rathbone www.bobrathbone.com
# Adapted from code by Nathan Chantrell http://nathan.chantrell.net

# GNU GPL V3 

# SK Pang Electronics June 2012

import smbus
import sys
import getopt
import time 
#bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

address = 0x20 # I2C address of MCP23017
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to output 
bus.write_byte_data(0x20,0x00,0x80) # Set  A0 of bank A to input 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 
#bus.write_byte_data(0x20,0x01,0x80) # Set  A0 of bank A to input 


# bank b = 0, bank a = 1
def set_led(data,bank):
  ##print "bank "+ str(bank) + " data=" + str(data)
  if bank == 1:
   bus.write_byte_data(address,0x12,data)
  else:
   bus.write_byte_data(address,0x13,data)
  return

# Handle the command line arguments
def main():
   plus3 = 2
   green_led = 1 + plus3
   amber_led = 8
   red_led = 64
   bank0 = 0

   while True:
       set_led(plus3,bank0)
       set_led(green_led,bank0)
       print "Green"
       buttonPressed = False
       while not buttonPressed:
           inp = bus.read_byte_data(address,0x12)
           if inp > 0:
               buttonPressed = True
               print "Button pressed"
           else:
               time.sleep(0.25)

       set_led(amber_led,bank0)
       print "Amber"
       time.sleep(3)
       set_led(red_led,bank0)
       print "Red"
       time.sleep(3)
       set_led(red_led | amber_led,bank0)
       print "Red and Amber"
       time.sleep(3)

if __name__ == "__main__":
   main()
