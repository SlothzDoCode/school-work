import tkinter as tk
from tkinter import *
import battleShips

#!constants
battleships = battleShips

shipCount = 0
rotationCount = 0
ship = battleships.carrier().returnIdentifier()
rotation = "V"
buttons = {}


#!commands

def get_location(xcoords, ycoords):
    
    print(f"x: {xcoords}, y: {ycoords}")
    
    if ship == "CA":
        temp = battleships.carrier().placeOnBoard(rotation,xcoords,ycoords)
        color = "blue"
    elif ship == "BA":
        temp = battleships.battleship().placeOnBoard(rotation,xcoords,ycoords)    
        color = "green"
    elif ship == "SU":
        temp = battleships.Submarine().placeOnBoard(rotation,xcoords,ycoords) 
        color = "red"
    elif ship == "CR":
        temp = battleships.crusier().placeOnBoard(rotation,xcoords,ycoords) 
        color = "yellow"
    elif ship == "DE":
        temp = battleships.destroyer().placeOnBoard(rotation,xcoords,ycoords) 
        color = "black"
        
    updateButtons(temp,color)
    
def switchShip():
    global shipCount
    global ship
    
    shipCount += 1
    
    if shipCount == 5:
        shipCount = 0

    if shipCount == 0:
        ship = battleships.carrier().returnIdentifier()
    elif shipCount == 1:
        ship = battleships.battleship().returnIdentifier()
    elif shipCount == 2:
        ship = battleships.Submarine().returnIdentifier()
    elif shipCount == 3:
        ship = battleships.crusier().returnIdentifier()    
    elif shipCount == 4:
        ship = battleships.destroyer().returnIdentifier()

    label1.config(text=ship)

def switchRotation():
    global rotationCount
    global rotation
    
    rotationCount += 1
    
    if rotationCount == 2:
        rotationCount = 0

    if rotationCount == 0:
        rotation = "V"
    elif rotationCount == 1:
        rotation = "H"

    
    label2.config(text=rotation)

def updateButtons(temp,color):
    for x in range(10):
        for y in range(10):
            value = temp[y,x]
            colors = "white" if value is None else color
            buttons[(x, y)].config(bg=colors)
            
#!display

display = tk.Tk()

frame1 = Frame(display)
frame1.grid(row=0,column=0, sticky="news")
grid1 = Frame(frame1)
grid1.grid(sticky="news", column=0, row=7, columnspan=2)
frame1.rowconfigure(7, weight=1)
frame1.columnconfigure(0, weight=1)

for x in range(10):
    for y in range(10):
        btn = Button(frame1,text="",width=7,height=3, command=lambda x=x, y=y: get_location(x,y))
        btn.grid(column=x, row=y, sticky="news")
        buttons[(x, y)] = btn

frame1.columnconfigure(tuple(range(10)), weight=1)
frame1.rowconfigure(tuple(range(10)), weight=1)



spacer1 = tk.Label(display,width=7,height=3)
spacer1.grid(row=0,column=1)



frame2 = Frame(display)
frame2.grid(row=0,column=2, sticky="news")
grid2 = Frame(frame2)
grid2.grid(sticky="news", column=0, row=7, columnspan=2)
frame2.rowconfigure(7, weight=1)
frame2.columnconfigure(0, weight=1)


spacer2 = tk.Label(frame2,width=7,height=7)
spacer2.grid(row=0,column=0)

button1 = tk.Button(frame2,width=7,height=3,text="rotate",command=switchRotation)
button1.grid(row=1,column=0)

button2 = tk.Button(frame2,width=7,height=3,text="next ship",command=switchShip)
button2.grid(row=2,column=0)

spacer3 = tk.Label(frame2,width=7,height=7)
spacer3.grid(row=2,column=1)


label2 = tk.Label(frame2,text=rotation)
label2.grid(row=1,column=2)

label1 = tk.Label(frame2,text=ship)
label1.grid(row=2,column=2)



display.attributes('-fullscreen',True)
mainloop()
