import sys
import tkinter as tk
import time
import classes # or // from classes import *
# from functions import *


sys.dont_write_bytecode = True # Avoid the automatic creation .pyc File inside __pycache__ folder


iLoop=0

def mouseClicked(event):
    # nonlocal iLoop
    global iLoop
    if (iLoop % 2)== 0:
        sw.Start()
    else:  
        sw.Stop()
    iLoop+=1



root = tk.Tk() # initializing the tcl/tk interpreter and creating the root window
sw = classes.StopWatch(root)
sw.pack(side=tk.TOP)



frame = tk.Frame(root, width=100, height=100)
frame.bind("<Button-2>", mouseClicked)
frame.pack()

root.mainloop()
    
    
