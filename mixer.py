from tkinter import *
import pygame.mixer
from tkinter.messagebox import askokcancel

app = Tk()
app.title("Head First Mix")

sound_file = "50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()


# A function created to use the checkbutton widget
def track_toggle():
    if track_playing.get() == 1:  # The IntVar´s get method. '1' for ticket, '0' for unticked
        track.play(loops=-1)
    else:
        track.stop()

track = mixer.Sound(sound_file)
track_playing = IntVar()
# Widget to create a check button - 'Checkbutton'
track_button = Checkbutton(app, variable=track_playing, command=track_toggle, text=sound_file).pack()


#  A function created to change de music volume
def change_volume(v):  # Its needed a parameter 'v', but I don´t know why.
    track.set_volume(volume.get())

volume = DoubleVar()  # A variable used to handle with floating-points numbers
volume.set(track.get_volume())
# Widget to create a slider - 'Scale'
volume_scale = Scale(app, variable=volume, from_=0.0, to=1.0, resolution=0.1,  # 'resolution' is a kind of interval
                     command=change_volume, label='Volume', orient=HORIZONTAL).pack(side=RIGHT)


# A function created to stop the song if the user click on the close button before stop the song
def shutdown():
    track.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)  # An event protocol to execute a specific code instead the default one
app.mainloop()
