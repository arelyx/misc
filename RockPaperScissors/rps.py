import random
WIN_STATES = {"Rock":"Scissors","Scissors":"Paper","Paper":"Rock"}
user = input("RPS: ")
comp = random.choice(["Rock","Paper","Scissors"])
print(comp)
if user == comp:
    print("tie")
elif WIN_STATES[user] == comp:
    print("you win")
else:
    print("you lose")


