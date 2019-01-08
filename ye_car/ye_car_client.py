from tkinter import *
from car_client import *
to_be_started = True
car_control = Tk()
car_control.title('car remote-control')
car_control.geometry('600x550')

########################### network
Connect_the_pi()

########################### main text
main_text = StringVar()
main_text.set('')
main_label = Label(car_control, textvariable = main_text, bg = 'pink', font = ('Arial','9'),
              width = 30 , height = 4)
main_label.place(x = 80 , y = 0 , anchor = 'nw')

main_text2 = StringVar()
main_text2.set('current state: follow the track\n')
main_label2 = Label(car_control, textvariable = main_text2, bg = 'pink', font = ('Arial','9'),
              width = 30 , height = 2)
main_label2.place(x = 80 , y = 65 , anchor = 'nw')

########################### change the speed
def ChangeSpeed(v): # get the value
    if v == '0':
        main_text.set( 'car stopped.' + '\n\n' )
    elif v ==  '4':
        main_text.set('set the car to full speed: ' + v + '\n\n')
    else:
        main_text.set('set the car to speed ' + v + '\n\n')
    Send_message('s' + v)

speed_scale = Scale(car_control, label = 'Speed Adjustment', from_ = 4, to = 0, length = 200, showvalue = 1,
                    tickinterval = 1, resolution = 1, command = ChangeSpeed).place(x = 50,y = 120, anchor = 'nw')

########################### music
music1 = '極楽浄土'
music2 = 'キミがいれば'

def SelectMusic():
    choice = music_box.get(music_box.curselection()) # get the value
    if choice == 'stop music':
        main_text.set('\n' + 'not playing music' + '\n')
    else:
        main_text.set('\n' + 'play music: ' + choice + '\n')
    if choice == 'stop music':
        Send_message('v0')
    elif choice == '極楽浄土':
        Send_message('v1')
    elif choice == 'キミがいれば':
        Send_message('v2')
    else:
        Send_message('v3')

music_var = StringVar()
music_var.set(( 'stop music',music1,music2))
music_box = Listbox(car_control , listvariable = music_var)
music_box.place(x = 240, y = 120 , anchor = 'nw')
music_button = Button(car_control, text = 'Adjust Music', width = 15 ,
                      height = 2 , command = SelectMusic)
music_button.place(x = 250, y = 320 , anchor = 'nw')

########################### manual operation
def ChangeToManualControl():
    main_text2.set('current state: manual control\n')
    Send_message('m1')
def Process_Text():
    var = manual_entry.get()
    Send_message(var)

manual_button = Button(car_control, text = 'manual control',width = 18,
                    height = 2, fg = 'Navy',  command = ChangeToManualControl)
manual_button.place(x = 250 , y = 400 , anchor = 'nw')
manual_button2 = Button(car_control, text = 'send order',width = 15,
                    height = 2 , command = Process_Text)
manual_button2.place(x = 420 , y = 320 , anchor = 'nw')
manual_entry = Entry(car_control)
manual_entry.place(x = 400, y = 230, anchor = 'nw')

########################### obstacle avoidance
def ChangeToObstacleAvoidance():
    main_text2.set('current state: obstacle avoidance\n')
    Send_message('m2')

OA_button = Button(car_control, text = 'obstacle avoidance',width = 18,
                   height = 2, fg = 'Navy' ,command = ChangeToObstacleAvoidance)
OA_button.place(x = 50 , y = 400 , anchor = 'nw')

########################### follow the track
def ChangeToFollowTheTrack():
    main_text2.set('current state: follow the track\n')
    Send_message('m3')

follow_button = Button(car_control, text = 'follow the track', width = 18,
                       height = 2, fg = 'Navy', command = ChangeToFollowTheTrack)
follow_button.place(x = 50 , y = 460 , anchor = 'nw')

########################### about and help
def AboutAndHelp():
    help_win = Tk()
    help_win.title('about and help')
    help_win.geometry('500x500')
    help_var = StringVar()
    help_file = open('help.txt', 'r')
    help_var.set(help_file.read())
    help_label = Label(help_win, textvariable = help_var, bg = 'green', font = ('Arial','9'),
                       width = 40, height = 40)
    help_file.close()
    help_label.pack()
    help_win.mainloop()

about_button = Button(car_control, text = 'about & help', width = 18,
                      height = 2, command = AboutAndHelp)
about_button.place(x = 250 , y = 460 , anchor = 'nw')



car_control.mainloop()
Exit_connection(socket_tcp)