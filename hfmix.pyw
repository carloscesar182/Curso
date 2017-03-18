from tkinter import *
from sound_panel import *
import pygame.mixer
import os  # Necessary to 'talk' with your OS

app = Tk()
app.title('Head First Mixer')

mixer = pygame.mixer
mixer.init()

dirList = os.listdir(".")
# It will get the names of everything ended with '.wav' in the directory
for fname in dirList:  # Takes each of the file names
    if fname.endswith(".wav"):  # ... and if ends with '.wav' ...
        # ... it will draw in your GUI
        panel = SoundPanel(app, mixer, fname).pack()


def shutdown():
    mixer.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
