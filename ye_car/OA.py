from global_var import *

import _thread
from speed import *

Threshold = 0.15
MinThreshold = 0.01
TurnTime = 0.6

def Calculate_Distance():
    count = 0
    GPIO.output(TRIG,GPIO.HIGH)
    time.sleep(0.000015) #0.000015
    GPIO.output(TRIG,GPIO.LOW)
    while not GPIO.input(ECHO) :
        count+=1
        if count > 99999:
            return 10
    start = time.time()
    while GPIO.input(ECHO):
        pass
    stop = time.time()
    return (stop-start)*340/2
    
    
def Obstacle_Avoidance(p1,p2,p3,p4):
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
        distance = Calculate_Distance()
        #print(distance)
        if (distance < Threshold) & (distance > MinThreshold) :
            Change_speed(p1,2.0)
            Change_speed(p2,0.0)
            Change_speed(p3,0.0)
            Change_speed(p4,2.0)
            time.sleep(TurnTime)
            Change_speed(p1,Get_Run_Speed())
            Change_speed(p3,Get_Run_Speed())
            Change_speed(p2,0.0)
            Change_speed(p4,0.0)

def Init_OA():
    p1 = Start_speed(3,Get_Run_Speed())
    p2 = Start_speed(5,0.0)
    p3 = Start_speed(7,Get_Run_Speed())
    p4 = Start_speed(11,0.0)
    _thread.start_new_thread(Obstacle_Avoidance,(p1,p2,p3,p4))
