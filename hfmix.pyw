from tkinter import *
from sound_panel import *
import pygame.mixer

app = Tk()
app.title('Head First Mixer')

mixer = pygame.mixer
mixer.init()

# By calling the new function TWICE, you create TWO sets of sound controls on the GUI
create_gui(app, mixer, "50459_M_RED_Nephlimizer.wav")
create_gui(app, mixer, "49119_M_RED_HardBouncer.wav")


def shutdown():
    mixer.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
