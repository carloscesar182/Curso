#  Used to import the tkinter standard library
from tkinter import *


#  Creates a function to save the written information
def save_data():
    try:  # Creates an exception handler
        fileD = open("deliveries.txt", "a")
        fileD.write("Depot:\n")
        fileD.write("%s\n" % depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.set(None)  # Using 'set(None)' instead '.delete' because the widget radiobutton or option menu
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        app.title("Can´t write to the file %s" % ex)  # Display the error message in the window title


#  Function to read a file with a list of depots
def read_depots(file):
    depots = []  # Start with an empty array
    depots_f = open(file)  # Open the file
    for line in depots_f:  # Read from the file one line at time
        depots.append(line.rstrip())  # Append a stripped copy of the line to the array
    return depots  # Return the list to the calling code

#  Creates the app
app = Tk()
#  Title for the window
app.title("Head-Ex Control")

#  Creates and draws the label
Label(app, text="Depot:").pack()
depot = StringVar()
depot.set(None)
options = read_depots("depots.txt")
#  Creates and draws an option menu widget
OptionMenu(app, depot, *options).pack()  # This '*.options' calls the variable containing the depots list

#  Creates and draws radio buttons widget (simple and limited widget)
"""
Radiobutton(app, text="Cambridge, MA", value="Cambridge, MA", variable=depot).pack()
Radiobutton(app, text="Cambridge, UK", value="Cambridge, UK", variable=depot).pack()
Radiobutton(app, text="Seattle, WA", value="Seattle, WA", variable=depot).pack()
"""
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
