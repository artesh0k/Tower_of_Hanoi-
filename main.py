import tkinter as tk
import math


# -------------------------------------------------------------------------------------------
def escape(event):
    window.destroy()


# -------------------------------------------------------------------------------------------
def start(event):
    canvas.unbind('<Button-1>')
    global i

    if i == 0:
        canvas.create_rectangle(100, 200, 300, 400, fill='#292929', outline='#292929')
        canvas.create_rectangle(700, 200, 900, 400, fill='#292929', outline='#292929')
        canvas.delete(w3)

    if i == 1:
        canvas.create_rectangle(125, 225, 275, 375, fill='#454747', outline='#454747')
        canvas.create_rectangle(725, 225, 875, 375, fill='#454747', outline='#454747')
        canvas.delete(w2)

    if i == 2:
        canvas.create_rectangle(150, 250, 250, 350, fill='#f2ac13', outline='#f2ac13')
        canvas.create_rectangle(750, 250, 850, 350, fill='#f2ac13', outline='#f2ac13')
        canvas.delete(w1)

    canvas.create_rectangle(175, 275, 225, 325, fill='#fac552', outline='#fac552')
    canvas.create_rectangle(775, 275, 825, 325, fill='#fac552', outline='#fac552')

    if i != 3:
        canvas.after(300, start, 0)
    if i == 3:
        pregame()
    i += 1


# -------------------------------------------------------------------------------------------
def increase(event):
    global number_of_disks
    global number
    canvas.delete(number)
    if number_of_disks < 7:
        number_of_disks += 1
    number = canvas.create_text(500, 325, text=f'{number_of_disks}', font='times 25', fill='#fac552')


# -------------------------------------------------------------------------------------------
def decrease(event):
    global number_of_disks
    global number
    canvas.delete(number)
    if number_of_disks > 3:
        number_of_disks -= 1
    number = canvas.create_text(500, 325, text=f'{number_of_disks}', font='times 25', fill='#fac552')


# -------------------------------------------------------------------------------------------
def pregame():
    global number_of_disks
    global number
    number_of_disks = 3
    canvas.delete('all')
    canvas.create_text(500, 100, text='-TOWER OF HANOI-', font='times 40', fill='#fac552')
    canvas.create_text(500, 180, text='choose the number of disks:', font='times 25', fill='#fac552')
    plus = canvas.create_text(600, 300, text='↑', font='times 25', fill='#f2ac13')
    minus = canvas.create_text(600, 350, text='↓', font='times 25', fill='#f2ac13')
    number = canvas.create_text(500, 325, text=f'{number_of_disks}', font='times 25', fill='#fac552')
    game = s = canvas.create_text(500, 500, text='-start-', font='times 20', fill='#fac552')
    canvas.tag_bind(plus, '<Button-1>', increase)
    canvas.tag_bind(minus, '<Button-1>', decrease)
    canvas.tag_bind(game, '<Button-1>', new_game)


# -------------------------------------------------------------------------------------------
def new_game(event):
    canvas.delete('all')

    global rod1
    global rod2
    global rod3
    global remaining_space

    remaining_space = canvas.create_rectangle(0, 0, 1000, 600, fill='#222424', outline='#fac552')
    canvas.create_text(500, 100, text='-TOWER OF HANOI-', font='times 40', fill='#fac552')
    rod1 = canvas.create_rectangle(110, 250, 290, 430, fill='#222424', outline='#222424')
    rod2 = canvas.create_rectangle(410, 250, 590, 430, fill='#222424', outline='#222424')
    rod3 = canvas.create_rectangle(710, 250, 890, 430, fill='#222424', outline='#222424')

    global number_of_disks
    global s1
    global s2
    global s3
    canvas.create_text(500, 500, text=f'{number_of_disks}', font='times 20', fill='#fac552')
    s1 = canvas.create_rectangle(190, 250, 210, 430, fill='#fac552', outline='#fac552')
    s2 = canvas.create_rectangle(490, 250, 510, 430, fill='#fac552', outline='#fac552')
    s3 = canvas.create_rectangle(790, 250, 810, 430, fill='#fac552', outline='#fac552')
    global disks
    global rod_info1
    global rod_info2
    global rod_info3
    rod_info1 = []
    rod_info2 = []
    rod_info3 = []

    for o in range(number_of_disks):
        disks[o] = canvas.create_rectangle(470 - (o) * 10,  # x1
                                           290 + (7 - number_of_disks + o) * 20,  # y1
                                           530 + (o) * 10,  # x2
                                           310 + (7 - number_of_disks + o) * 20,  # y2
                                           fill='#f2ac13',
                                           outline='black')
        rod_info2.append(number_of_disks - o - 1)
    global win
    win = []
    win = rod_info2
    print(win)
    game_process()


# -------------------------------------------------------------------------------------------
def cancel(event):
    global disks
    global y
    canvas.itemconfig(disks[y], fill='#f2ac13')


# -------------------------------------------------------------------------------------------
def move(event):
    global disks
    global rod_info1
    global rod_info2
    global rod_info3
    global x
    global y
    global remaining_space
    x1 = x
    criterium = 1
    print(x1)
    if event.x >= 110:
        x = 1
        if event.x >= 410:
            x = 2
            if event.x >= 710:
                x = 3
    y1 = 0
    if rod_info1 != win:
        if rod_info3 != win:
            if x == 1:

                if x1 == 2:
                    if len(rod_info1) > 0:
                        if rod_info1[-1] < rod_info2[-1]:
                            criterium = 0
                            y1 = rod_info2[-1]
                    if criterium == 1:
                        rod_info1.append(rod_info2[-1])
                        y1 = rod_info1[-1]
                        rod_info2.pop()
                else:
                    if len(rod_info1) > 0:
                        if rod_info1[-1] < rod_info3[-1]:
                            criterium = 0
                            y1 = rod_info3[-1]
                    if criterium == 1:
                        rod_info1.append(rod_info3[-1])
                        y1 = rod_info1[-1]
                        rod_info3.pop()

                if criterium == 1:
                    canvas.coords(disks[y1],
                                  170 + 300 * (x - 1) - 10 * y1,  # x1
                                  450 - 20 * len(rod_info1),  # y1
                                  230 + 300 * (x - 1) + 10 * y1,  # x2
                                  430 - 20 * len(rod_info1))  # y2
                    canvas.itemconfig(disks[y1], fill='#f2ac13')
                    print('rod 1:', rod_info1)
                    print('rod 2:', rod_info2)
                    print('rod 3:', rod_info3)
                else:
                    canvas.itemconfig(disks[y1], fill='#f2ac13')
                    print('there is the bigger disk')

            if x == 2:

                if x1 == 1:
                    if len(rod_info2) > 0:
                        if rod_info2[-1] < rod_info1[-1]:
                            criterium = 0
                            y1 = rod_info1[-1]
                    if criterium == 1:
                        rod_info2.append(rod_info1[-1])
                        y1 = rod_info2[-1]
                        rod_info1.pop()
                else:
                    if len(rod_info2) > 0:
                        if rod_info2[-1] < rod_info3[-1]:
                            criterium = 0
                            y1 = rod_info3[-1]
                    if criterium == 1:
                        rod_info2.append(rod_info3[-1])
                        y1 = rod_info2[-1]
                        rod_info3.pop()

                if criterium == 1:
                    canvas.coords(disks[y1],
                                  170 + 300 * (x - 1) - 10 * y1,  # x1
                                  450 - 20 * len(rod_info2),  # y1
                                  230 + 300 * (x - 1) + 10 * y1,  # x2
                                  430 - 20 * len(rod_info2))  # y2
                    canvas.itemconfig(disks[y1], fill='#f2ac13')
                    print('rod 1:', rod_info1)
                    print('rod 2:', rod_info2)
                    print('rod 3:', rod_info3)
                else:
                    canvas.itemconfig(disks[y1], fill='#f2ac13')
                    print('there is the bigger disk')

            if x == 3:

                if x1 == 1:
                    if len(rod_info3) > 0:
                        if rod_info3[-1] < rod_info1[-1]:
                            criterium = 0
                            y1 = rod_info1[-1]
                    if criterium == 1:
                        rod_info3.append(rod_info1[-1])
                        y1 = rod_info3[-1]
                        rod_info1.pop()
                else:
                    if len(rod_info3) > 0:
                        if rod_info3[-1] < rod_info2[-1]:
                            criterium = 0
                            y1 = rod_info2[-1]
                    if criterium == 1:
                        rod_info3.append(rod_info2[-1])
                        y1 = rod_info3[-1]
                        rod_info2.pop()

                if criterium == 1:
                    canvas.coords(disks[y1],
                                  170 + 300 * (x - 1) - 10 * y1,  # x1
                                  450 - 20 * len(rod_info3),  # y1
                                  230 + 300 * (x - 1) + 10 * y1,  # x2
                                  430 - 20 * len(rod_info3))  # y2
                    canvas.itemconfig(disks[y1], fill='#f2ac13')
                    print('rod 1:', rod_info1)
                    print('rod 2:', rod_info2)
                    print('rod 3:', rod_info3)
                else:
                    canvas.itemconfig(disks[y1], fill='#f2ac13')
                    print('there is the bigger disk')
        else:
            print('victory')
            canvas.create_text(500, 150, text='-YOU WON-', font='times 25', fill='#fac552')
    else:
        print('victory')
        canvas.create_text(500, 150, text='-YOU WON-', font='times 25', fill='#fac552')


# ------------------------------------------------------------------------------------------
def disk_pressing(event):
    global disks
    global rod_info1
    global rod_info2
    global rod_info3
    global rod1
    global rod2
    global rod3
    global number_of_disks
    global x
    global y
    global remaining_space
    global s1
    global s2
    global s3
    global win
    x = 0

    if rod_info1 != win:
        if rod_info3 != win:

            if event.x >= 110:
                x = 1
                y = math.floor((event.y - 290 - (7 - len(rod_info1)) * 20) / 20)
                if event.x >= 410:
                    x = 2
                    y = math.floor((event.y - 290 - (7 - len(rod_info2)) * 20) / 20)
                    if event.x >= 710:
                        x = 3
                        y = math.floor((event.y - 290 - (7 - len(rod_info3)) * 20) / 20)

            print(x, y)

            if x == 1:
                if y == 0:
                    canvas.itemconfig(disks[rod_info1[-1]], fill='#ffcc00')
                    print('the highest disk is selected')
                    canvas.tag_bind(remaining_space, '<Button-1>', cancel)
                    canvas.tag_bind(rod1, '<Button-1>', cancel)
                    canvas.tag_bind(rod2, '<Button-1>', move)
                    canvas.tag_bind(rod3, '<Button-1>', move)
                    canvas.tag_bind(s2, '<Button-1>', move)
                    canvas.tag_bind(s3, '<Button-1>', move)

            if x == 2:
                if y == 0:
                    canvas.itemconfig(disks[rod_info2[-1]], fill='#ffcc00')
                    print('the highest disk is selected')
                    canvas.tag_bind(remaining_space, '<Button-1>', cancel)
                    canvas.tag_bind(rod1, '<Button-1>', move)
                    canvas.tag_bind(rod2, '<Button-1>', cancel)
                    canvas.tag_bind(rod3, '<Button-1>', move)
                    canvas.tag_bind(s1, '<Button-1>', move)
                    canvas.tag_bind(s3, '<Button-1>', move)

            if x == 3:
                if y == 0:
                    canvas.itemconfig(disks[rod_info3[-1]], fill='#ffcc00')
                    print('the highest disk is selected')
                    canvas.tag_bind(remaining_space, '<Button-1>', cancel)
                    canvas.tag_bind(rod1, '<Button-1>', move)
                    canvas.tag_bind(rod2, '<Button-1>', move)
                    canvas.tag_bind(rod3, '<Button-1>', cancel)
                    canvas.tag_bind(s1, '<Button-1>', move)
                    canvas.tag_bind(s2, '<Button-1>', move)

        else:
            print('victory')
            canvas.create_text(500, 150, text='-YOU WON-', font='times 25', fill='#fac552')
    else:
        print('victory')
        canvas.create_text(500, 150, text='-YOU WON-', font='times 25', fill='#fac552')


# -------------------------------------------------------------------------------------------
def game_process():
    global disks
    global rod_info1
    global rod_info2
    global rod_info3
    global rod1
    global rod2
    global rod3
    global number_of_disks
    global win

    for y in range(number_of_disks):
        canvas.tag_bind(disks[y], '<Button-1>', disk_pressing)

    restart = canvas.create_text(500, 550, text='-restart-', font='times 25', fill='#fac552')
    canvas.tag_bind(restart, '<Button-1>', new_game)
    if rod_info1 == win:
        print('victory')
        canvas.create_text(500, 150, text='-YOU WON-', font='times 25', fill='#fac552')
    if rod_info3 == win:
        print('victory')
        canvas.create_text(500, 150, text='-YOU WON-', font='times 25', fill='#fac552')
    print('rod 1:', rod_info1)
    print('rod 2:', rod_info2)
    print('rod 3:', rod_info3)


# -------------------------------------------------------------------------------------------


window = tk.Tk()
window.title('-TOWER OF HANOI-')

canvas = tk.Canvas(bg='#222424', height=600, width=1000)
canvas.pack()

canvas.create_text(500, 100, text='-TOWER OF HANOI-', font='times 40', fill='#fac552')

canvas.create_rectangle(175, 275, 225, 325, fill='#fac552', outline='#fac552')
canvas.create_rectangle(775, 275, 825, 325, fill='#fac552', outline='#fac552')

w1 = canvas.create_rectangle(400, 200, 600, 400, fill='#292929', outline='#292929')
w2 = canvas.create_rectangle(425, 225, 575, 375, fill='#454747', outline='#454747')
w3 = canvas.create_rectangle(450, 250, 550, 350, fill='#f2ac13', outline='#f2ac13')
w4 = canvas.create_rectangle(475, 275, 525, 325, fill='#fac552', outline='#fac552')

i = 0

start_title = canvas.create_text(500, 500, text='-start-', font='times 20', fill='#fac552')
quit_title = canvas.create_text(500, 550, text='-quit-', font='times 20', fill='#fac552')

disks = ['disk0', 'disk1', 'disk2', 'disk3', 'disk4', 'disk5', 'disk6']

canvas.tag_bind(start_title, '<Button-1>', start)
canvas.tag_bind(quit_title, '<Button-1>', escape)
