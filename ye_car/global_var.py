#others should detect the variable CHANGED
#

import RPi.GPIO as GPIO
import time

RunSpeed = 1.0
SPEED_CHANGED = False
MUSIC_CHANGED = False
CHANGED = False
CHANGED_DONE = True
command = ''
command_arrived = False

# enable the engines
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
ECHO = 35
TRIG = 37
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.add_event_detect(8 , GPIO.RISING)
GPIO.add_event_detect(10 , GPIO.RISING)

def Get_Music_Changed():
    return MUSIC_CHANGED

def Set_Music_Changed(var):
    global MUSIC_CHANGED
    MUSIC_CHANGED = var

def Get_Command():
    return command

def Set_Command(var):
    global command
    command = var

def Get_Command_Arrived():
    return command_arrived

def Set_Command_Arrived(var):
    global command_arrived
    command_arrived = var

def Get_Speed_Changed():
    return SPEED_CHANGED

def Set_Speed_Changed(var):
    global SPEED_CHANGED
    SPEED_CHANGED = var

def Get_Run_Speed():
    return RunSpeed

def Set_Run_Speed(var):
    global RunSpeed
    RunSpeed = var

def Set_Changed(var):
    global CHANGED
    CHANGED = var

def Get_Changed():
    return CHANGED

def Set_Changed_Done(var):
    global CHANGED_DONE
    CHANGED_DONE = var

def Get_Changed_Done():
    return CHANGED_DONE
