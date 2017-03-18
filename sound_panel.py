from tkinter import *
import pygame


# When this function is called, it is expecting three parameters
def create_gui(app, mixer, sound_file):
    def track_toggle():  # This function is local to the 'create_gui' function
        if track_playing.get() == 1:  # The IntVar´s get method. '1' for ticket, '0' for unticked
            track.play(loops=-1)
        else:
            track.stop()

    #  A function created to change de music volume. It is local too.
    def change_volume(v):  # Its needed a parameter 'v', but I don´t know why.
        track.set_volume(volume.get())

    # When the function is called, it starts executing from here
    track = mixer.Sound(sound_file)
    track_playing = IntVar()
    # Widget to create a check button - 'Checkbutton'
    track_button = Checkbutton(app, variable=track_playing, command=track_toggle, text=sound_file).pack(side=LEFT)

    volume = DoubleVar()  # A variable used to handle with floating-points numbers
    volume.set(track.get_volume())
    # Widget to create a slider - 'Scale'
    volume_scale = Scale(app, variable=volume, from_=0.0, to=1.0, resolution=0.1,  # 'resolution' is a kind of interval
                         command=change_volume, label='Volume', orient=HORIZONTAL).pack(side=RIGHT)
