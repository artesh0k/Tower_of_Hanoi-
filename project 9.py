import tkinter as tk
import math
import time 
window = tk.Tk()
window.title('-HANOJSKÉ VEŽE-')

obrazok=tk.Canvas(bg='#222424', height=600, width=1000)
obrazok.pack()

obrazok.create_text(500,100, text='-HANOJSKÉ VEŽE-', font='times 40', fill='#fac552')

obrazok.create_rectangle(175,275,225,325, fill='#fac552', outline='#fac552')
obrazok.create_rectangle(775,275,825,325, fill='#fac552', outline='#fac552')

w1=obrazok.create_rectangle(400,200,600,400, fill='#292929', outline='#292929')
w2=obrazok.create_rectangle(425,225,575,375, fill='#454747', outline='#454747')
w3=obrazok.create_rectangle(450,250,550,350, fill='#f2ac13', outline='#f2ac13')
w4=obrazok.create_rectangle(475,275,525,325, fill='#fac552', outline='#fac552')

i=0

s=obrazok.create_text(500,500, text='-start-', font='times 20', fill='#fac552')
q=obrazok.create_text(500,550, text='-quit-', font='times 20', fill='#fac552')

disks = ['disk0','disk1','disk2','disk3','disk4','disk5','disk6']

#-------------------------------------------------------------------------------------------
def escape(event):
    window.destroy()

#-------------------------------------------------------------------------------------------
def start(event):
    obrazok.unbind('<Button-1>')
    global i

    if i == 0:
        obrazok.create_rectangle(100,200,300,400, fill='#292929', outline='#292929')
        obrazok.create_rectangle(700,200,900,400, fill='#292929', outline='#292929')
        obrazok.delete(w3)
    
    if i == 1:
        obrazok.create_rectangle(125,225,275,375, fill='#454747', outline='#454747')
        obrazok.create_rectangle(725,225,875,375, fill='#454747', outline='#454747')
        obrazok.delete(w2)
    
    if i == 2:
        obrazok.create_rectangle(150,250,250,350, fill='#f2ac13', outline='#f2ac13')
        obrazok.create_rectangle(750,250,850,350, fill='#f2ac13', outline='#f2ac13')
        obrazok.delete(w1)
    
    obrazok.create_rectangle(175,275,225,325, fill='#fac552', outline='#fac552')
    obrazok.create_rectangle(775,275,825,325, fill='#fac552', outline='#fac552')
    
    if i != 3:
        obrazok.after(300, start,0)
    if i ==3:
        predgame()
    i+=1

#___________________________________________________________________________________________
obrazok.tag_bind(s, '<Button-1>',start)
obrazok.tag_bind(q, '<Button-1>',escape)

#-------------------------------------------------------------------------------------------
def plusko(event):
    global number_of_disks
    global number
    obrazok.delete(number)
    if number_of_disks<7:
        number_of_disks+=1
    number=obrazok.create_text(500,325, text=f'{number_of_disks}', font='times 25', fill='#fac552')

#-------------------------------------------------------------------------------------------
def minusko(event):
    global number_of_disks
    global number
    obrazok.delete(number)
    if number_of_disks>3:
        number_of_disks-=1
    number=obrazok.create_text(500,325, text=f'{number_of_disks}', font='times 25', fill='#fac552')

#-------------------------------------------------------------------------------------------
def predgame():
    global number_of_disks
    global number
    number_of_disks=3
    obrazok.delete('all')
    obrazok.create_text(500,100, text='-HANOJSKÉ VEŽE-', font='times 40', fill='#fac552')
    obrazok.create_text(500,180, text='choose the number of disks:', font='times 25', fill='#fac552')
    plus=obrazok.create_text(600,300, text='↑', font='times 25', fill='#f2ac13')
    minus=obrazok.create_text(600,350, text='↓', font='times 25', fill='#f2ac13')
    number=obrazok.create_text(500,325, text=f'{number_of_disks}', font='times 25', fill='#fac552')
    game=s=obrazok.create_text(500,500, text='-start-', font='times 20', fill='#fac552')
    obrazok.tag_bind(plus, '<Button-1>',plusko)
    obrazok.tag_bind(minus, '<Button-1>',minusko)
    obrazok.tag_bind(game, '<Button-1>',new_game)

#-------------------------------------------------------------------------------------------
def new_game(event):
    obrazok.delete('all')
    
    global can1
    global can2
    global can3
    global yes
    
    yes=obrazok.create_rectangle(0,0,1000,600, fill='#222424', outline='#fac552')
    obrazok.create_text(500,100, text='-HANOJSKÉ VEŽE-', font='times 40', fill='#fac552')
    can1=obrazok.create_rectangle(110,250,290,430,fill='#222424', outline='#222424')
    can2=obrazok.create_rectangle(410,250,590,430,fill='#222424', outline='#222424')
    can3=obrazok.create_rectangle(710,250,890,430,fill='#222424', outline='#222424')
    
    global number_of_disks
    global s1
    global s2
    global s3
    obrazok.create_text(500,500, text=f'{number_of_disks}', font='times 20', fill='#fac552')
    s1=obrazok.create_rectangle(190,250,210,430,fill='#fac552', outline='#fac552')
    s2=obrazok.create_rectangle(490,250,510,430,fill='#fac552', outline='#fac552')
    s3=obrazok.create_rectangle(790,250,810,430,fill='#fac552', outline='#fac552')
    global disks
    global stolb1
    global stolb2
    global stolb3
    stolb1=[]
    stolb2=[]
    stolb3=[]
    
    for o in range(number_of_disks):
        disks[o]=obrazok.create_rectangle(470-(o)*10, #x1
                                          290+(7-number_of_disks+o)*20, #y1
                                          530+(o)*10, #x2
                                          310+(7-number_of_disks+o)*20, #y2
                                          fill='#f2ac13',
                                          outline='black')
        stolb2.append(number_of_disks-o-1)
    global win
    win=[]
    win=stolb2
    print(win)
    process_game()
#-------------------------------------------------------------------------------------------
def otmena(event):
    global disks
    global y
    obrazok.itemconfig(disks[y],fill='#f2ac13')

#-------------------------------------------------------------------------------------------
def kuda(event):
    global disks
    global stolb1
    global stolb2
    global stolb3
    global x
    global y
    global yes
    x1=x
    mensi_alebo_nie=1
    print(x1)
    if event.x >= 110:
       x=1
       if event.x >= 410:
           x=2
           if event.x >= 710:
               x=3
    y1=0
    if stolb1!=win:
        if stolb3!=win:
            if x==1:

                if x1==2:
                    if len(stolb1)>0:
                        if stolb1[-1]<stolb2[-1]:
                            mensi_alebo_nie=0
                            y1=stolb2[-1]
                    if mensi_alebo_nie==1:
                        stolb1.append(stolb2[-1])
                        y1=stolb1[-1]
                        stolb2.pop()
                else:
                    if len(stolb1)>0:
                        if stolb1[-1]<stolb3[-1]:
                            mensi_alebo_nie=0
                            y1=stolb3[-1]
                    if mensi_alebo_nie==1:
                        stolb1.append(stolb3[-1])
                        y1=stolb1[-1]
                        stolb3.pop()

                if mensi_alebo_nie==1:
                    obrazok.coords(disks[y1],
                                   170+300*(x-1)-10*y1, #x1
                                   450-20*len(stolb1), #y1
                                   230+300*(x-1)+10*y1, #x2
                                   430-20*len(stolb1)) #y2
                    obrazok.itemconfig(disks[y1],fill='#f2ac13')
                    print('stolb1:',stolb1)
                    print('stolb2:',stolb2)
                    print('stolb3:',stolb3)
                else:
                    obrazok.itemconfig(disks[y1],fill='#f2ac13')
                    print('tam bolse')
        
            if x==2:

                if x1==1:
                    if len(stolb2)>0:
                        if stolb2[-1]<stolb1[-1]:
                            mensi_alebo_nie=0
                            y1=stolb1[-1]
                    if mensi_alebo_nie==1:
                        stolb2.append(stolb1[-1])
                        y1=stolb2[-1]
                        stolb1.pop()
                else:
                    if len(stolb2)>0:
                        if stolb2[-1]<stolb3[-1]:
                            mensi_alebo_nie=0
                            y1=stolb3[-1]
                    if mensi_alebo_nie==1:
                        stolb2.append(stolb3[-1])
                        y1=stolb2[-1]
                        stolb3.pop()

                if mensi_alebo_nie==1:
                    obrazok.coords(disks[y1],
                                   170+300*(x-1)-10*y1, #x1
                                   450-20*len(stolb2), #y1
                                   230+300*(x-1)+10*y1, #x2
                                   430-20*len(stolb2)) #y2
                    obrazok.itemconfig(disks[y1],fill='#f2ac13')
                    print('stolb1:',stolb1)
                    print('stolb2:',stolb2)
                    print('stolb3:',stolb3)
                else:
                    obrazok.itemconfig(disks[y1],fill='#f2ac13')
                    print('tam bolse')
        
            if x==3:

                if x1==1:
                    if len(stolb3)>0:
                        if stolb3[-1]<stolb1[-1]:
                            mensi_alebo_nie=0
                            y1=stolb1[-1]
                    if mensi_alebo_nie==1:
                        stolb3.append(stolb1[-1])
                        y1=stolb3[-1]
                        stolb1.pop()
                else:
                    if len(stolb3)>0:
                        if stolb3[-1]<stolb2[-1]:
                            mensi_alebo_nie=0
                            y1=stolb2[-1]
                    if mensi_alebo_nie==1:
                        stolb3.append(stolb2[-1])
                        y1=stolb3[-1]
                        stolb2.pop()

                if mensi_alebo_nie==1:
                    obrazok.coords(disks[y1],
                                   170+300*(x-1)-10*y1, #x1
                                   450-20*len(stolb3), #y1
                                   230+300*(x-1)+10*y1, #x2
                                   430-20*len(stolb3)) #y2
                    obrazok.itemconfig(disks[y1],fill='#f2ac13')
                    print('stolb1:',stolb1)
                    print('stolb2:',stolb2)
                    print('stolb3:',stolb3)
                else:
                    obrazok.itemconfig(disks[y1],fill='#f2ac13')
                    print('tam bolse')
        else:
            print('won')
            obrazok.create_text(500,150, text='-YOU WON-', font='times 25', fill='#fac552')      
    else:
        print('won')
        obrazok.create_text(500,150, text='-YOU WON-', font='times 25', fill='#fac552')
            
#------------------------------------------------------------------------------------------
def stlacenie_disku(event):
    global disks
    global stolb1
    global stolb2
    global stolb3
    global can1
    global can2
    global can3
    global number_of_disks
    global x
    global y
    global yes
    global s1
    global s2
    global s3
    global win
    x=0
    
    if stolb1!=win:
        if stolb3!=win:

            if event.x >= 110:
               x=1
               y=math.floor((event.y-290-(7-len(stolb1))*20)/20)
               if event.x >= 410:
                   x=2
                   y=math.floor((event.y-290-(7-len(stolb2))*20)/20)
                   if event.x >= 710:
                       x=3
                       y=math.floor((event.y-290-(7-len(stolb3))*20)/20)

            print(x,y)
    
            if x==1:
                if y==0:
                    obrazok.itemconfig(disks[stolb1[-1]],fill='#ffcc00')
                    print('vysoko')
                    obrazok.tag_bind(yes,'<Button-1>',otmena)
                    obrazok.tag_bind(can1,'<Button-1>',otmena)
                    obrazok.tag_bind(can2,'<Button-1>',kuda)
                    obrazok.tag_bind(can3,'<Button-1>',kuda)
                    obrazok.tag_bind(s2,'<Button-1>',kuda)
                    obrazok.tag_bind(s3,'<Button-1>',kuda)
            
            
            if x==2:
                if y==0:
                    obrazok.itemconfig(disks[stolb2[-1]],fill='#ffcc00')
                    print('vysoko')
                    obrazok.tag_bind(yes,'<Button-1>',otmena)
                    obrazok.tag_bind(can1,'<Button-1>',kuda)
                    obrazok.tag_bind(can2,'<Button-1>',otmena)
                    obrazok.tag_bind(can3,'<Button-1>',kuda)
                    obrazok.tag_bind(s1,'<Button-1>',kuda)
                    obrazok.tag_bind(s3,'<Button-1>',kuda)
            
            if x==3:
                if y==0:
                    obrazok.itemconfig(disks[stolb3[-1]],fill='#ffcc00')
                    print('vysoko')
                    obrazok.tag_bind(yes,'<Button-1>',otmena)
                    obrazok.tag_bind(can1,'<Button-1>',kuda)
                    obrazok.tag_bind(can2,'<Button-1>',kuda)
                    obrazok.tag_bind(can3,'<Button-1>',otmena)
                    obrazok.tag_bind(s1,'<Button-1>',kuda)
                    obrazok.tag_bind(s2,'<Button-1>',kuda)
    
        else:
            print('won')
            obrazok.create_text(500,150, text='-YOU WON-', font='times 25', fill='#fac552')
    else:
        print('won')
        obrazok.create_text(500,150, text='-YOU WON-', font='times 25', fill='#fac552')
    

#-------------------------------------------------------------------------------------------
def process_game():
    global disks
    global stolb1
    global stolb2
    global stolb3
    global can1
    global can2
    global can3
    global number_of_disks
    global win
    
    for y in range(number_of_disks):
        obrazok.tag_bind(disks[y],'<Button-1>',stlacenie_disku)

    restart=obrazok.create_text(500,550, text='-restart-', font='times 25', fill='#fac552')
    obrazok.tag_bind(restart,'<Button-1>',new_game)
    if stolb1==win:
        print('won')
        obrazok.create_text(500,150, text='-YOU WON-', font='times 25', fill='#fac552')
    if stolb3==win:
        print('won')
        obrazok.create_text(500,150, text='-YOU WON-', font='times 25', fill='#fac552')
    print('stolb1:',stolb1)
    print('stolb2:',stolb2)
    print('stolb3:',stolb3)

#-------------------------------------------------------------------------------------------

