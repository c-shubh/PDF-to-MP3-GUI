from tkinter import (Tk, Menu, ttk, messagebox)
from PdfTab import PdfTab
from TextTab import TextTab

# GUI start------------------------------------------------
root = Tk()
root.title("PDF to MP3 Convertor")
topmenu = Menu(root)

# Menu Bar open--------------------------------------------


# File Menu------------------------------------------------


filemenu = Menu(topmenu, tearoff=0)
topmenu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Recent", command=None)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.destroy)

# Help Menu------------------------------------------------

helpmenu = Menu(topmenu, tearoff=0)
topmenu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Instructions", command=lambda: messagebox.showinfo(
    "Instructions", "Hello"))
helpmenu.add_separator()
helpmenu.add_command(label="About", command=lambda: messagebox.showinfo(
    "About", "Hi there! My name is Dhruti and I'm currently pursuing 3rd year of my Engineering. I developed this mini project using Python."))
root.config(menu=topmenu)

# Menu Bar close-------------------------------------------


# Tabs-----------------------------------------------------

tabs = ttk.Notebook(root)

PdfTab = PdfTab(tabs)
TextTab = TextTab(tabs)

tabs.pack(expand=1, fill="both")

root.mainloop()
