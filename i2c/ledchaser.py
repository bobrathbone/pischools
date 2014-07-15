#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# By Nathan Chantrell http://nathan.chantrell.net
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
  print "set_led bank=" + str(bank) + " data=" + str(data) 
  if bank == 1:
   bus.write_byte_data(address,0x12,data)
  else:
   bus.write_byte_data(address,0x13,data)
  return

# Handle the command line arguments
def main():
   a = 0
delay = 0.05   
while True:

# Move led left  
   for x in range(0,8):
     a = 1 << x
     set_led(a,0)
     time.sleep(delay)
   set_led(0,0)
   for x in range(0,8):
     a = 1 << x
     set_led(a,1)
     time.sleep(delay)
   set_led(0,1)  
 
# Move led right 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,1)
     time.sleep(delay)
   set_led(0,1)
 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,0)
     time.sleep(delay)
   set_led(0,0)
   
  
if __name__ == "__main__":
   main()
