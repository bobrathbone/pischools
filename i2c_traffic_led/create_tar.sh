#!/bin/bash
# $Id: create_tar.sh,v 1.1 2013/06/11 11:46:56 bob Exp $
dir="i2c_traffic_led"
FILELIST="../$dir/i2c3leds.py  ../$dir/i2cPedestrianLights.py  ../$dir/i2cTrafficLights.py  ../$dir/ledchaser.py  ../$dir/single_led.py"
tar -cvzf  i2c_traffic_led.tar.gz ${FILELIST}


