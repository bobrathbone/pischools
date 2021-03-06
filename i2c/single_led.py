#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# Flash a single LED
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
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 

def set_led(data,bank):
  #print "set_led bank=" + str(bank) + " data=" + str(data) 
  if bank == 1:
   bus.write_byte_data(address,0x12,data)
  else:
   bus.write_byte_data(address,0x13,data)
  return

# Handle the command line arguments
def main():
   a = 0
delay = 0.5
while True:
     led = 2
     bank = 0
     set_led(led,bank)
     time.sleep(delay)
     set_led(0,bank)
     time.sleep(delay)

if __name__ == "__main__":
   main()
