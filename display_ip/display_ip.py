#!/usr/bin/env python
#
# $Id: display_ip.py,v 1.1 2013/06/11 11:46:56 bob Exp $

import os
from lcd_class import Lcd

lcd = Lcd()

def interrupt():
	return False

# Execute system command
def exec_cmd(cmd):
        p = os.popen(cmd)
        result = p.readline().rstrip('\n')
        return result

lcd.init()
lcd.setWidth(16)
myip = exec_cmd('hostname -I')
count = 5
while  count > 0:
	lcd.scroll1("IP:" + myip, interrupt)
	lcd.line2("Line 2: defghijk")
	count = count - 1

lcd.line1("IP:" + myip)

# End

