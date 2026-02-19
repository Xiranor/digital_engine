from libraries import master
from resource_checks import demo_check
from tkinter import *
import random

random.seed()

def populate(deck, cards):
    for card in cards:
        if not card in deck:
            deck[card] = deck["deck_keys"]
if demo_check == 1:
    from libraries import demo
    populate(master.regions, demo.regions)
    populate(master.landmarks, demo.landmarks)
    populate(master.namesakes, demo.namesakes)
    populate(master.origins, demo.origins)
    populate(master.attributes, demo.attributes)
    populate(master.advents, demo.advents)

def pull_card(deck):
    pull = random.randint(1, len(deck)-1)
    return list(deck)[pull]
root = Tk()
root.title("The Digital Engine")
root.geometry('1280x720')

lbl = Label(root, text = "Region")
lbl.grid()

def clicked():
    lbl.configure(text = pull_card(master.regions))

btn = Button(root, text = "Pull a region",
             fg = "red", command=clicked)
btn.grid(column=1, row=0)


root.mainloop()