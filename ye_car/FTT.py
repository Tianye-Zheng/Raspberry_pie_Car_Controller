from global_var import *
import _thread
from speed import *

#adjust_time = 0.2

def Adjust_Direction0(p1,p2,p3,p4):
    Change_speed(p1,0.0)
    Change_speed(p2,2.0)
    Change_speed(p3,2.0)
    Change_speed(p4,0.0)
    while GPIO.input(8):
        pass
    Change_speed(p1,Get_Run_Speed())
    Change_speed(p2,0.0)
    Change_speed(p3,Get_Run_Speed())
    Change_speed(p4,0.0)

    
def Adjust_Direction1(p1,p2,p3,p4):
    Change_speed(p1,2.0)
    Change_speed(p2,0.0)
    Change_speed(p3,0.0)
    Change_speed(p4,2.0)
    while GPIO.input(10):
        pass
    Change_speed(p1,Get_Run_Speed())
    Change_speed(p2,0.0)
    Change_speed(p3,Get_Run_Speed())
    Change_speed(p4,0.0)

    
def Follow_the_Track(p1,p2,p3,p4):
    while True:
        s_t = Get_Speed_Changed()
        if  s_t :
            Change_speed(p1,Get_Run_Speed())
            Change_speed(p3,Get_Run_Speed())
            Change_speed(p2,0.0)
            Change_speed(p4,0.0)
            Set_Speed_Changed(False)
        if Get_Changed() == True:
            break
        if GPIO.event_detected(8):
            Adjust_Direction0(p1,p2,p3,p4)
        if GPIO.event_detected(10):
            Adjust_Direction1(p1,p2,p3,p4)

def Init_FTT():
    p1 = Start_speed(3,Get_Run_Speed())
    p2 = Start_speed(5,0.0)
    p3 = Start_speed(7,Get_Run_Speed())
    p4 = Start_speed(11,0.0)
    _thread.start_new_thread(Follow_the_Track,(p1,p2,p3,p4))

