from tkinter import *
import pygame.mixer


# The SoundPanel class
class SoundPanel(Frame):
    """ An initializer method comes first. Note that this method needs to be called "__init__" in Python in order
    to be called automatically when the object is created"""
    def __init__(self, app, mixer, sound_file):
        Frame.__init__(self, app)
        # When the function is called, it starts executing from here
        self.track = mixer.Sound(sound_file)  # Each SoundPanel() object has its own track
        self.track_playing = IntVar()
        # Widget to create a check button - 'Checkbutton'
        track_button = Checkbutton(self, variable=self.track_playing, command=self.track_toggle,
                                   text=sound_file).pack(side=LEFT)
        self.volume = DoubleVar()  # A variable used to handle with floating-points numbers
        self.volume.set(self.track.get_volume())
        # Widget to create a slider - 'Scale'
        volume_scale = Scale(self, variable=self.volume, from_=0.0, to=1.0,
                             resolution=0.1,  # 'resolution' is a kind of interval
                             command=self.change_volume, label='Volume', orient=HORIZONTAL).pack(side=RIGHT)


    def track_toggle(self):  # This function is local to the 'create_gui' function
        if self.track_playing.get() == 1:  # The IntVar´s get method. '1' for ticket, '0' for unticked
            self.track.play(loops=-1)
        else:
            self.track.stop()

    #  A function created to change de music volume. It is local too.
    def change_volume(self, v):  # Its needed a parameter 'v', but I don´t know why.
        self.track.set_volume(self.volume.get())





