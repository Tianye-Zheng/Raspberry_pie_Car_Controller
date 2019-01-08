from global_var import *

import socket    # prepare for network
import sys
Host_IP = ''
Host_Port = 8888
Host_Addr= (Host_IP,Host_Port)

socket_tcp = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket_tcp.bind(Host_Addr)
socket_tcp.listen(1)
socket_con , (client_ip , client_port) = socket_tcp.accept()

from OA import Init_OA
from FTT import Init_FTT
from MC import Init_MC
from PM import Init_Music

def Change_Process(data):
    if data[0] == 'm':
        if data[1] == '1':
            #print('calling init_mc')
            Init_MC()
        elif data[1] == '2':
            #print('calling init_oa')
            Init_OA()
        elif data[1] == '3':
            #print('calling init_ftt')
            Init_FTT()
        else:
            pass
            
    elif data[0] == 'v':
        Set_Music_Changed(True)
        #print(data)
        if data[1] == '0':
            pass
        elif data[1] == '1':
            Init_Music(1)
        elif data[1] == '2':
            Init_Music(2)
        else: # data[1] == '3':
            Init_Music(3)
        
    elif data[0] == 's':
        if data[1] == '0':
            Set_Run_Speed(0.0)
        elif data[1] == '1':
            Set_Run_Speed(1.0)
        elif data[1] == '2':
            Set_Run_Speed(2.0)
        else:
            Set_Run_Speed(3.0)
        Set_Speed_Changed(True)

    elif (data[0] == 't') or (data[0] == 'g') or (data[0] == 'f'):
        Set_Command(data)
        Set_Command_Arrived(True)
                
    else:
        pass

def Process(data):
    #print("executing")
    if data[0] == 'm':
        Set_Changed_Done(False)
        Set_Changed(True)
        time.sleep(1) # wait the current thread to do the aftermath
    Set_Changed(False)
    Set_Changed_Done(True)
    Change_Process(data)

Init_OA()   # starting into the OA mode

while True:
    try:
        data = socket_con.recv(512)
        data = data.decode()
        Process(data)
            
    except Exception:
        socket_tcp.close()
        sys.exit(1)
