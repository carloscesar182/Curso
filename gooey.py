#  Import the library code
from tkinter import *
import pygame.mixer

#  Event handlers that set the IntVar and play the appropriate sound
def play_correct_sound():
    num_good.set(num_good.get() + 1)
    s_correct.play()

def play_wrong_sound():
    num_bad.set(num_bad.get() + 1)
    s_wrong.play()

#  Creates the Gui application window
app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

#  Initialize the sound system
sounds = pygame.mixer
sounds.init()

#  Load the required sound effects
s_correct = sounds.Sound("correct.wav")
s_wrong = sounds.Sound("wrong.wav")

#  Create the IntVars to count the answers
num_good = IntVar()
num_good.set(0)
num_bad = IntVar()
num_bad.set(0)

#  Creates a friendly message that tells what to do
lab = Label(app, text = 'Where you are ready, click on the buttons.', height = 3)
#  Be sure to pack your widgets
lab.pack()

#  A label to count and connect to the relevant IntVar
lab1 = Label(app, textvariable = num_good)
lab1.pack(side = 'left')

#  A label to count and connect to the relevant IntVar
lab2 = Label(app, textvariable = num_bad)
lab2.pack(side = 'right')

#  A button connected with its relevant event handler
b1 = Button(app, text = "Correct!", width = 10, command = play_correct_sound)  # add the button
b1.pack(side = 'left', padx = 10, pady = 10)  # links the button and the window

b2 = Button(app, text = "Wrong!", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

#  Starts the tkinter mainloop
app.mainloop()
