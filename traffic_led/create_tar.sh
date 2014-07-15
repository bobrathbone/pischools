#!/bin/bash
# $Id: create_tar.sh,v 1.1 2013/06/11 11:46:56 bob Exp $
dir="traffic_led"
FILELIST="../$dir/FlashLed.py  ../$dir/PedestrianCrossing.py  ../$dir/TrafficLED.py"
tar -cvzf  traffic_led.tar.gz ${FILELIST}


