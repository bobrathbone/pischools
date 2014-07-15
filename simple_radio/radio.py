# Simple radio using four buttons
import RPi.GPIO as GPIO
import os
import atexit
from time import sleep

# Register exit routine
def finish():
	exec_command("service mpd stop")
        print("Radio stopped")

atexit.register(finish)

# Switch definitions
VOLUME_UP = 11
VOLUME_DOWN = 12
CHANNEL_UP = 15
CHANNEL_DOWN = 16

# Execute system command sub-routine
def exec_command(cmd):
	result = ""
	p = os.popen(cmd)
	for line in p.readline().split('\n'):
		result = result + line
	return result

### Main routine ###
if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(VOLUME_UP,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(VOLUME_DOWN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(CHANNEL_UP,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(CHANNEL_DOWN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	exec_command("service mpd start")
	exec_command("mpc clear")
	exec_command("mpc load mylist.pls")
	exec_command("mpc play")
	exec_command("mpc volume 70")

	while True:
		newChannel = False
		volChanged = False
		if GPIO.input(VOLUME_UP): 
			exec_command("mpc volume +4")
			volChanged = True
		if GPIO.input(VOLUME_DOWN): 
			exec_command("mpc volume -4")
			volChanged = True
		if GPIO.input(CHANNEL_UP): 
			exec_command("mpc next")
			newChannel = True
		if GPIO.input(CHANNEL_DOWN): 
			exec_command("mpc prev")
			newChannel = True
		if newChannel:
			current = exec_command("mpc current")
			print current
		elif volChanged:
			status = exec_command("mpc status")
			print status
		sleep(0.2)


