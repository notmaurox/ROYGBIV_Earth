try:
    # This will work in Python 2.7
    import Tkinter
    import tkFileDialog as filedialog
except ImportError:
    # This will work in Python 3.5
    import tkinter.filedialog as filedialog
    import tkinter as Tkinter
    
import dataSorterUser
import mapBuilderUser


root = Tkinter.Tk()
root.title("Map Builder")
root.geometry("600x450")

frameTitle = Tkinter.Frame(root)
frameTitle.grid(row=0, sticky="nsew")

title = Tkinter.Label(frameTitle, 
		 text="ROYGBIV Earth, a global graphing tool",
		 fg = "dark green",
		 font = "Helvetica 25 bold italic").grid(row=0, sticky="N")
         
         
frameInfo = Tkinter.Frame(root)
frameInfo.grid(row=1, sticky="nsew")

# Create a text box that explains the calculation.
titleMSG = Tkinter.Label(frameInfo, text="Graph Title")
titleMSG.grid(row=0, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
title = Tkinter.StringVar()
title.set('Provide graph title here')
title_entry = Tkinter.Entry(frameInfo, width=50, textvariable=title)
title_entry.grid(row=0, column=1)

# Create a text box that explains the calculation.
valMSG = Tkinter.Label(frameInfo, text="Data label")
valMSG.grid(row=1, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
val = Tkinter.StringVar()
val.set('Provide data type here')
val_entry = Tkinter.Entry(frameInfo, width=50, textvariable=val)
val_entry.grid(row=1, column=1)
# Create a text box that explains the calculation.
fileNameMSG = Tkinter.Label(frameInfo, text="Graph output file name")
fileNameMSG.grid(row=2, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
fileNameOut = Tkinter.StringVar()
fileNameOut.set('ROYGBIVEarthOut')
fileNameOut_entry = Tkinter.Entry(frameInfo, width=50, textvariable=fileNameOut)
fileNameOut_entry.grid(row=2, column=1)

# -----------------------------------------------------------------------------
# Create a frame within the main window.
# ----------------------------------------------------------------------------- 
# The frame will contain the widgets needed to do a calculation.
# Each widget in "frame" is created with "frame" as its first argument.
frame = Tkinter.Frame(root)
frame.grid(row=2, sticky="nsew")

greeting = Tkinter.Label(frame, 
                        text="Please specify which percent of countries should fall in each category \nwhere Red is the top 16 percent of countries and Orange is the next top 14 percent...", 
                        font ="Cambria 13 italic")
greeting.grid(row=0, sticky='E')

# Create a text box that explains the calculation.
invitationRed = Tkinter.Label(frame, text="Percentage in red")
invitationRed.grid(row=2, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
red = Tkinter.StringVar()
red.set('16')
red_entry = Tkinter.Entry(frame, width=8, textvariable=red)
red_entry.grid(row=2, column=1)

# Create a text box that explains the calculation.
invitationOrange = Tkinter.Label(frame, text="Percentage in orange")
invitationOrange.grid(row=3, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
orange = Tkinter.StringVar()
orange.set('14')
orange_entry = Tkinter.Entry(frame, width=8, textvariable=orange)
orange_entry.grid(row=3, column=1)

# Create a text box that explains the calculation.
invitationYellow = Tkinter.Label(frame, text="Percentage in yellow")
invitationYellow.grid(row=4, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
Yellow = Tkinter.StringVar()
Yellow.set('14')
Yellow_entry = Tkinter.Entry(frame, width=8, textvariable=Yellow)
Yellow_entry.grid(row=4, column=1)

# Create a text box that explains the calculation.
invitationGreen = Tkinter.Label(frame, text="Percentage in green")
invitationGreen.grid(row=5, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
Green = Tkinter.StringVar()
Green.set('14')
Green_entry = Tkinter.Entry(frame, width=8, textvariable=Green)
Green_entry.grid(row=5, column=1)


# Create a text box that explains the calculation.
invitationBlue = Tkinter.Label(frame, text="Percentage in blue")
invitationBlue.grid(row=6, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
Blue = Tkinter.StringVar()
Blue.set('14')
Blue_entry = Tkinter.Entry(frame, width=8, textvariable=Blue)
Blue_entry.grid(row=6, column=1)


# Create a text box that explains the calculation.
invitationIndigo = Tkinter.Label(frame, text="Percentage in indigo")
invitationIndigo.grid(row=7, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
Indigo = Tkinter.StringVar()
Indigo.set('14')
Indigo_entry = Tkinter.Entry(frame, width=8, textvariable=Indigo)
Indigo_entry.grid(row=7, column=1)

# Create a text box that explains the calculation.
invitationViolet = Tkinter.Label(frame, text="Percentage in violet")
invitationViolet.grid(row=8, sticky='W')
# Define an input variable and add an entry box so the user can change its value.
Violet = Tkinter.StringVar()
Violet.set('14')
Violet_entry = Tkinter.Entry(frame, width=8, textvariable=Violet)
Violet_entry.grid(row=8, column=1)

placeHolder = Tkinter.Label(frame, text = "")
placeHolder.grid(row=10, sticky = 'N')

browseMSG = Tkinter.Label(frame, text="Click Browse button to select data file")
browseMSG.grid(row=11, sticky='W')

filename = Tkinter.StringVar()

def browsefunc():
    filename.set( filedialog.askopenfilename(filetypes=[("CSV files","*.csv")], title="Select Data File") )
    pathlabel.config(text=filename.get())

browsebutton = Tkinter.Button(root, text="Browse", command=browsefunc)
browsebutton.grid(row=10)

pathlabel = Tkinter.Label(root)
pathlabel.grid(row=12)

# Define a function to close the window.
def quit(event=None):
    root.destroy()
    
# Create a button that will close the window.
buttonExit = Tkinter.Button(text="Exit", command=quit)
buttonExit.grid(row = 13, sticky = 'W')

# Define function to make map
def build(event=None):
    dataSorterUser.sort(filename.get(),red.get(),orange.get(),Yellow.get(),Green.get(),Blue.get(),Indigo.get(),Violet.get())
    #finalFileName = fileNameOut.get() + ".html"
    mapBuilderUser.graph("processedData.csv",title.get(),val.get(),fileNameOut.get() )

# Create a button that will close the window.
buttonBuild = Tkinter.Button(text="Create Graph", command=build)
buttonBuild.grid(row = 13, sticky = 'E')

root.mainloop()

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)