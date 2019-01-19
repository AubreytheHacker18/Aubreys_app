from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
from tkinter.messagebox import *
from tkinter.filedialog import *

# Main window
root = Tk(className="Aubreys text-editor (:")
textArea = scrolledtext.ScrolledText(root, width=100, height=40, bg="white", fg="black")
textArea.pack()

# Functions
def findinfile():
    findString = simpledialog.askstring("Find...", "Enter text")
    textdata = textArea.get("1.0", END)
    # count = 0
    occurrances = textdata.upper().count(findString.upper())

    if textdata.upper().count(findString.upper()) > 0:
        showinfo("Results", findString + " has multiple occurances, " + str(occurrances))
    else:
        showinfo("Results", "Then is no such word")

    print(findString.upper() in textdata.upper())





def newfile():
    if len(textArea.get("1.0", END+"-1c")) > 0:
        if messagebox.askyesno("Save", "Do you wish to save"):
            savefile()
    textArea.delete("1.0", END)

def openfile():
    file = filedialog.askopenfile(parent=root, title="Select a text file", filetypes=(("Text file", "*.txt"), ("All files", "*.")))

    if file != None:
        contents = file.read()
        textArea.insert("1.0", contents)
        file.close()

def savefile():
    file = filedialog.asksaveasfile(mode="w", filetypes=(("Text file", "*.txt"), ("All files", "*.")))

    if file != None:
        data = textArea.get("1.0", END+"-1c")
        file.write(data)
        file.close()

def about():
     showinfo("About", "A text-editor made by Aubrey Kellermann in python.")

def exit():
    if messagebox.askyesno("Quit", "Are you sure you want to quit? "):
        root.destroy()



# Menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newfile)
fileMenu.add_command(label="Open", command=openfile)
fileMenu.add_command(label="Save as", command=savefile)
fileMenu.add_command(label="Find", command=findinfile)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_command(label="About", command=about)



# Keep_window_open
root.mainloop()


