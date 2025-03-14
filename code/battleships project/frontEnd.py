import tkinter as tk
from tkinter import *
import battleShips
import numpy as np

#!constants
battleships = battleShips

playerBoard = battleships.board().createBoard()

AIBoard = battleships.board().createBoard()

shipCount = 0
rotationCount = 0
ship = battleships.carrier(playerBoard).returnIdentifier()
rotation = "V"
buttons = {}

gamestart = False

currentPlayer = 1

gameOver = False


#!commands

def get_location(xcoords, ycoords):
    
    global playerBoard,AIBoard
    global currentPlayer
    
    print(f"x: {xcoords}, y: {ycoords}")
    if currentPlayer == 1:
        if ship == "CA":
            
            temp = battleships.carrier(playerBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "blue")

        elif ship == "BA":
            temp = battleships.battleship(playerBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "green")
                
        elif ship == "SU":
            temp = battleships.Submarine(playerBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "red")
                
        elif ship == "CR":
            temp = battleships.crusier(playerBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "yellow")
                
        elif ship == "DE":
            temp = battleships.destroyer(playerBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "black")
        
    
    else:
        if ship == "CA":
            
            temp = battleships.carrier(AIBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "blue")

        elif ship == "BA":
            temp = battleships.battleship(AIBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "green")
                
        elif ship == "SU":
            temp = battleships.Submarine(AIBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "red")
                
        elif ship == "CR":
            temp = battleships.crusier(AIBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "yellow")
                
        elif ship == "DE":
            temp = battleships.destroyer(AIBoard).placeOnBoard(rotation, xcoords, ycoords)

            if isinstance(temp, str) and temp == "error":
                print(temp)
            else:
                updateButtons(temp, "black")          
    
def switchShip():
    global shipCount
    global ship
    
    shipCount += 1
    
    if shipCount == 5:
        shipCount = 0

    if shipCount == 0:
        ship = battleships.carrier(playerBoard).returnIdentifier()
    elif shipCount == 1:
        ship = battleships.battleship(playerBoard).returnIdentifier()
    elif shipCount == 2:
        ship = battleships.Submarine(playerBoard).returnIdentifier()
    elif shipCount == 3:
        ship = battleships.crusier(playerBoard).returnIdentifier()    
    elif shipCount == 4:
        ship = battleships.destroyer(playerBoard).returnIdentifier()

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
 
def switchPlayer():
    global AIBoard,playerBoard
    global currentPlayer
    
    for x in range(10):
        for y in range(10):
            colors = "white"
            buttons[(x, y)].config(bg=colors)      
    
    if currentPlayer == 1:
        currentPlayer += 1
        print(playerBoard)
    else:
        currentPlayer = 1 
        print(AIBoard)   
        
def startGame():
    global gamestart,currentPlayer
    global playerBoard,AIBoard
    gamestart = True   
    
    button3.destroy()
    button4.destroy()

def shoot(xcoords, ycoords):
    global currentPlayer
    global playerBoard, AIBoard
    
    if currentPlayer == 1:
        temp = battleships.board().shoot(xcoords,ycoords,AIBoard,"player 1")   
        if str(temp) == "gameOver":
            frame1.destroy()
            frame2.destroy()
            lbl = tk.Label(display,text="Game over: Player 1 wins")
            lbl.grid(row=1,column=2)
            return
        else:
            AIBoard = temp
            currentPlayer += 1
    
    else:
        temp = battleships.board().shoot(xcoords,ycoords,playerBoard, "player 2")   
        if str(temp) == "gameOver":
            frame1.destroy()
            frame2.destroy()
            lbl = tk.Label(display,text="Game over: Player 2 wins")
            lbl.grid(row=1,column=2)
            return
        else:
            playerBoard = temp
            currentPlayer = 1
            
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
        btn = Button(frame1,text="",width=7,height=3, command=lambda x=x, y=y: get_location(x, y) if not gamestart else shoot(x,y))
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

button3 = tk.Button(frame2,width=7,height=3,text="next player",command=switchPlayer)
button3.grid(row=3,column=0)

button4 = tk.Button(frame2,width=7,height=3,text="start",command=startGame)
button4.grid(row=4,column=0)

spacer3 = tk.Label(frame2,width=7,height=7)
spacer3.grid(row=2,column=1)


label2 = tk.Label(frame2,text=rotation)
label2.grid(row=1,column=2)

label1 = tk.Label(frame2,text=ship)
label1.grid(row=2,column=2)



display.attributes('-fullscreen',True)
mainloop()
