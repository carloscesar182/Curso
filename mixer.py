from tkinter import *
import pygame.mixer
from tkinter.messagebox import askokcancel

app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')
sound_file = "50459_M_RED_Nephlimizer.wav"
mixer = pygame.mixer
mixer.init()
track_playing = IntVar()


# A function created to use the checkbutton widget
def track_toggle():
    if track_playing.get() == 1:  # The IntVar´s get method. '1' for ticket, '0' for unticked
        track.play(loops=-1)
    else:
        track.stop()


# A function created to stop the song if the user click on the close button before stop the song
def shutdown():
    track.stop()
    app.destroy()
    """if askokcancel(title='Are you sure?', message='Do you really want to quit?'):  # A question message box
        app.destroy()  # It will end de app and will stop the song"""

track = mixer.Sound(sound_file)

track_button = Checkbutton(app, variable=track_playing, command=track_toggle, text=sound_file).pack()

app.protocol("WM_DELETE_WINDOW", shutdown)  # An event protocol to execute a specific code instead the default one
app.mainloop()
