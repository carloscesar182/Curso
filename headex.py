#  Used to import the tkinter standard library
from tkinter import *


#  Creates a function to save the written information
def save_data():
    fileD = open("deliveries.txt", "a")
    fileD.write("Depot:\n")
    fileD.write("%s\n" % depot.get())
    fileD.write("Description:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("Address:\n")
    fileD.write("%s\n" % address.get("1.0", END))
    depot.set(None)
    description.delete(0, END)
    address.delete("1.0", END)


def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

#  Creates the app
app = Tk()
#  Title for the window
app.title("Head-Ex Control")

#  Creates and draws the label
Label(app, text="Depot:").pack()
#  Creates and draws radio buttons widget
depot = StringVar()
depot.set(None)

options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text="Description:").pack()
description = Entry(app)
description.pack()

#  Creates and draws a multiple-text widget.
Label(app, text="Address:").pack()
address = Text(app)
address.pack()

#  Creates a button and call the function to save the information
Button(app, text="Save", command=save_data).pack()

#  Starts the event
app.mainloop()
