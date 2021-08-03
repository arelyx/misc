from tkinter import Tk, Canvas, Button,ALL
import time
import random

THRESHOLD = 0.75
WIDTH = 50
HEIGHT = 30
animating = False
tk = Tk()
tk.title("conway")
tk.configure(bg="black")
board = [[1 if random.randint(0,100) >= 100*THRESHOLD else 0 for x in range(WIDTH)] for x in range(HEIGHT)]

# for y in board:
#     print(y)

def update_board():
    newBoard = [[0 for x in range(WIDTH)] for x in range(HEIGHT)]
    for iy, y in enumerate(board):
        for ix, x in enumerate(y):
            neighbors = 0
            # print(iy)
            # print(ix)
            if board[iy-1][ix-1]:
                neighbors+=1
            if board[iy-1][ix]:
                neighbors+=1
            try:
                if board[iy-1][ix+1]:
                    neighbors+=1
            except:
                if board[iy-1][0]:
                    neighbors+=1
            
            if board[iy][ix-1]:
                neighbors+=1
            try:
                if board[iy][ix+1]:
                    neighbors+=1
            except:
                if board[iy][0]:
                    neighbors+=1
            
            try:
                if board[iy+1][ix-1]:
                    neighbors+=1
            except:
                if board[0][ix-1]:
                    neighbors+=1
            try:      
                if board[iy+1][ix]:
                    neighbors+=1
            except:
                if board[0][ix]:
                    neighbors+=1
            try:
                if board[iy+1][ix+1]:
                    neighbors+=1
            except:
                if board[0][0]:
                    neighbors+=1
            
            # print(neighbors)
            if x:
                if neighbors < 2 or neighbors > 3:
                    newBoard[iy][ix] = 0
                else:
                    newBoard[iy][ix] = 1
            else:
                if neighbors == 3:
                    newBoard[iy][ix] = 1
    return newBoard
                    

def draw():
    canvas.delete(ALL)
    for iy, y in enumerate(board):
        y_shift = iy*10
        for ix, x in enumerate(y):
            x_shift = ix*10
            if x == 1:
                canvas.create_rectangle(x_shift,y_shift,x_shift+10,y_shift+10,fill="white",outline="")
            else:
                canvas.create_rectangle(x_shift,y_shift,x_shift+10,y_shift+10,fill="black",outline="")

def update():
    global board
    board = update_board()
    draw()
def animate():
    global board
    while True:
        for x in range(250):
            update()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        board = [[1 if random.randint(0,100) >= 100*THRESHOLD else 0 for x in range(WIDTH)] for x in range(HEIGHT)]

canvas = Canvas(tk,width=WIDTH*10,height=HEIGHT*10,bg="red",borderwidth=0,highlightthickness=0)
canvas.pack()
draw()
animate()
# updateButton = Button(tk,text="Step",command=update)
# updateButton.pack()
tk.mainloop()