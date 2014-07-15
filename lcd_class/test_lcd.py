#!/usr/bin/env python
#

# Imports
from lcd_class import Lcd
from time import sleep
from time import strftime

lcd = Lcd()

# LCD interrupt scroll routine
def interrupt():
	return False

lcd.init()
lcd.setWidth(16)

# Display line 1 and 2
lcd.line1("Line 1: Test LCD")
lcd.line2("Line 2: defghijk")
sleep(3)

while True:
	todaysdate = strftime("%H:%M %d/%m/%Y")
	lcd.line1(todaysdate) 
	lcd.scroll2("Line 4: abcdefghijklmnopqrstuvwxyz 0123456789",interrupt) 

# End
