from global_var import *
import _thread
from speed import *

def Process_Order(com_list,p1,p2,p3,p4):
    if com_list[0].lower() == 'turn':
        if com_list[1].lower() == 'left':
            Change_speed(p1,0.0)
            Change_speed(p2,Get_Run_Speed())
            Change_speed(p3,Get_Run_Speed())
            Change_speed(p4,0.0)
        elif com_list[1].lower() == 'right':
            Change_speed(p1,Get_Run_Speed())
            Change_speed(p2,0.0)
            Change_speed(p3,0.0)
            Change_speed(p4,Get_Run_Speed())
        else:
            pass
    elif com_list[0].lower() == 'go':
        if com_list[1].lower() == 'straight':
            Change_speed(p1,Get_Run_Speed())
            Change_speed(p2,0.0)
            Change_speed(p3,Get_Run_Speed())
            Change_speed(p4,0.0)
        elif com_list[1].lower() == 'back':
            Change_speed(p1,0.0)
            Change_speed(p2,Get_Run_Speed())
            Change_speed(p3,0.0)
            Change_speed(p4,Get_Run_Speed())
        else:
            pass
    else:
        pass
    time.sleep(float(com_list[-1]))
    Change_speed(p1,0.0)
    Change_speed(p2,0.0)
    Change_speed(p3,0.0)
    Change_speed(p4,0.0)
    

def Manual_Control(p1,p2,p3,p4):
    while True:
        if Get_Changed() == True:
            break
        if Get_Command_Arrived():
            command = Get_Command()
            com_list = command.split(' ')
            if com_list[0].lower() == 'file':
                file_path = '/ye_car/' + com_list[-1]
                mc_file = open(file_path,'r')
                for line in mc_file.readlines():
                    line = line.strip('\n')
                    Process_Order(line.split(' '),p1,p2,p3,p4)
            else:
                Process_Order(com_list,p1,p2,p3,p4)
            Set_Command_Arrived(False) # process done

def Init_MC():
    p1 = Start_speed(3,0.0)
    p2 = Start_speed(5,0.0)
    p3 = Start_speed(7,0.0)
    p4 = Start_speed(11,0.0)
    _thread.start_new_thread(Manual_Control,(p1,p2,p3,p4))
