from tkinter import *
import random

WIN_STATES = {"Rock":"Scissors","Scissors":"Paper","Paper":"Rock"}

def check_winner(player_choice):
  canvas.delete(ALL)
  computer = random.choice(["Rock","Paper","Scissors"])
  if computer == player_choice:
    result = "It's a tie!"
  elif WIN_STATES[player_choice] == computer:
    result = "You win!"
  else:
    result = "You lose."
  canvas.create_text (150,50, text = f"You chose {player_choice}\nComputer chose {computer}\n{result}", fill = "black",font ="TNR 10")


tk = Tk()
tk.title("Rock Paper Scissors")
tk.geometry("300x250")

label = Label(tk,text="Rock Paper Scissors",font="TNR 18 bold")
label.pack()

rock = Button(tk,text="Rock", command = lambda :check_winner("Rock"), width=10)
rock.pack()

paper = Button(tk,text="Paper", command = lambda :check_winner("Paper"), width=10)
paper.pack()

scissors = Button(tk,text="Scissors", command = lambda :check_winner("Scissors"), width=10)
scissors.pack()

canvas = Canvas (tk, width = 300, height = 100, bg = "#D9D9D9")
canvas.pack()
tk.mainloop()
