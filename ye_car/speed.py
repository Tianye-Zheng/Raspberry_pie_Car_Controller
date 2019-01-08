#  the speed is between 0 and 4
#  0  means stop , 4 means the full speed
#  port is the port to change (3,5,... etc)
#  p is the pwm created
import RPi.GPIO as GPIO


def Change_speed (p,speed) :
        p.ChangeDutyCycle(100*(speed/4.0))
        
def Start_speed(port,speed):
       p = GPIO.PWM( port , 1000 ) # 1000Hz
       p.start(100*(speed/4.0))
       return p

def Stop_speed(p):
       p.stop()   
       
