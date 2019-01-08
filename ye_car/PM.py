from global_var import *
import _thread
import transfer

def Syllable(freq):
    if freq == 0:
        target = 0.0
        #f = open('/sys/class/pwm/pwm0/enable','w')
        #f.write('0\n')
        #f.close()
        #time.sleep(0.100)
        #time.sleep(0.125)
        #f = open('/sys/class/pwm/pwm0/enable','w')
        #f.write('1\n')
        #f.close()
    else :
        target = 1.0/freq*1000000000
    f = open('/sys/class/pwm/pwm0/duty_cycle','w')
    f.write(str(int(target/2))+'\n')
    #f.close()
    f = open('/sys/class/pwm/pwm0/period','w')
    f.write(str(int(target))+'\n')
    #f.close()
    time.sleep(0.100)
    #time.sleep(0.125)

def Play_Music(alist):
    aindex = 0
    aend = len(alist) - 1
    while True:
        if Get_Music_Changed() == True:
            Syllable(0)
            break
        Syllable(transfer.T(alist[aindex]))
        if aindex == aend:
            aindex = 0
        else:
            aindex += 1

def Init_Music(v_num):
    finit = open('/sys/class/pwm/pwm0/enable','w')
    finit.write('1\n')
    if v_num == 1:
        music = open('/ye_car/Gokurakujoudo.txt','r')
    elif v_num == 2:
        music = open('/ye_car/Kimigaireba.txt','r')
    alist = music.readline().strip('\n').split(',')    
    _thread.start_new_thread(Play_Music,(alist,))
    Set_Music_Changed(False)
    #fend = open('/sys/class/pwm/pwm0/enable','w')
    #fend.write('0\n')
    #fend.close()
