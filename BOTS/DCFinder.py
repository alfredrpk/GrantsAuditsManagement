from tkinter import filedialog
# import tkinter as tk

# root= tk.Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Select file",filetypes = (("PDF Files","*.pdf"),("All Files","*.*")))
# #button = tk.Button(r, text='Browse File', width=25, command=r.filename)

import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds')
def openfile():
	filename = filedialog.askopenfilename(initialdir = "C:/",title = "Select file",filetypes = (("PDF Files","*.pdf"),("All Files","*.*")))
	return(filename)

button = tk.Button(r, text='Stop', width=25, command=openfile) 
button.pack() 

r.geometry("500x500")

r.mainloop() 

# #! Python 3.4
# """
# Open a file dialog window in tkinter using the filedialog method.
# Tkinter has a prebuilt dialog window to access files. 
# This example is designed to show how you might use a file dialog askopenfilename
# and use it in a program.
# """

# from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename

# root = Tk(  )

# #This is where we lauch the file manager bar.
# def OpenFile():
#     name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
#                            filetypes =(("Text File", "*.txt"),("All Files","*.*")),
#                            title = "Choose a file."
#                            )
#     print (name)
#     #Using try in case user types in unknown file or closes without choosing a file.
#     try:
#         with open(name,'r') as UseFile:
#             print(UseFile.read())
#     except:
#         print("No file exists")


# Title = root.title( "File Opener")
# label = ttk.Label(root, text ="I'm BATMAN!!!",foreground="red",font=("Helvetica", 16))
# label.pack()

# #Menu Bar

# menu = Menu(root)
# root.config(menu=menu)

# file = Menu(menu)

# file.add_command(label = 'Open', command = OpenFile)
# file.add_command(label = 'Exit', command = lambda:exit())

# menu.add_cascade(label = 'File', menu = file)





# root.mainloop()

# '''
# RESULTS:
# >>> 
# C:/Users/Scott/Documents/Programming/json/test.txt
# "I like to move it, groove it!"
# '''
