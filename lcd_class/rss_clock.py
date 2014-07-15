#!/usr/bin/python
#
# HD44780 LCD Test Script for
# Raspberry Pi
#
# Date   : 26/07/2012
#

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

#import
import os
import RPi.GPIO as GPIO
import time
import datetime 
from time import strftime
from lcd_class import Lcd

rss_feed = "http://feeds.bbci.co.uk/news/uk/rss.xml?edition=int"

# Set up the LCD object
lcd = Lcd()

# LCD interrupt scroll routine
def interrupt():
	return False


# Main program block
def main():

  # Initialise display and set to 16 characters
  lcd.init()
  lcd.setWidth(16)
  
  # Main processing loop 
  while True:

    # Use curl to get the RSS feed
    exec_cmd("curl " + rss_feed + "| grep '<title>\|<description>' > /tmp/rss")

    # Open the file with read only permit
    f = open('/tmp/rss')
    # Read the first line from the temporary file
    line = f.readline().rstrip('\n')
    line = line.lstrip(' ')
    line = line.lstrip('<title>')

    # If the file is not empty keep reading line one at a time
    # till the file is empty
    while line:
	# Display time on the first line
        todaysdate = strftime("%H:%M %d/%m/%Y")
	lcd.line1(todaysdate)

        # Read a line from the /tmp/rss file
        line = f.readline().rstrip('\n')
        print line
        display = False
        if (line.find("VIDEO:") != -1):
            continue
        if (line.find("AUDIO:") != -1):
            continue
        if (line.find("<title>") != -1):
            display= True
        if (line.find("<description>") != -1):
            display= True

        if display:
            line = line.rstrip(' ')
            line = line.rstrip("/title>")
            line = line.rstrip("/description>")
            line = line.rstrip("<")
            line = line.lstrip(' ')
            line = line.lstrip('<title>')
            line = line.lstrip('<description>')
            lcd.scroll2(line,interrupt)
            time.sleep(1)


    f.close()

# Execute system command
def exec_cmd(cmd):
    p = os.popen(cmd)
    result = p.readline().rstrip('\n')
    return result


# Define program start
if __name__ == '__main__':
  main()


