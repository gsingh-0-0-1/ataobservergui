import tkinter as tk
from tkinter import Entry, Label
import subprocess

PROJECTS = {
	"P025" : "Maser",
	"P009" : "Pulsar"
}

window = tk.Tk()
window.geometry("500x300")
window.title("ATA Observer Dialog")

window.grid_columnconfigure((0,1), weight=1)

UserLabel = Label(window, text = "Observer Name")
ProjectLabel = Label(window, text = "Project ID")

UserEntry = Entry(window)
ProjectEntry = Entry(window)

UserLabel.grid(row=1, column=0)
UserEntry.grid(row=1, column=1, sticky="ew")
ProjectLabel.grid(row=2, column=0)
ProjectEntry.grid(row=2, column=1, sticky="ew")

SubmitButton = tk.Button(text = "Submit",
		width=25,
		height=5,
		bg = "blue")
SubmitLabel = Label(window, text = "")

def handle_click(event):
	user = UserEntry.get()
	pid = ProjectEntry.get()
	pname = PROJECTS[pid]
	subprocess.run(("./slackpost.bash %s %s %s" % (user, pid, pname)).split(" "))


SubmitButton.bind("<Button-1>", handle_click)

SubmitButton.grid(row = 4, column = 0)
SubmitLabel.grid(row = 4, column = 1)


window.mainloop()

