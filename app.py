#importing module (1)
from tkinter import *
from tkinter import messagebox

#button funtion to add (5)
def newTask():
    task = my_input.get()
    if task != "":
        lb.insert(END, task)
        my_input.delete(0,"end")
    else:
        messagebox.showwarning("Warning!","Please enter your task first!")


def deleteTask():
    lb.delete(ANCHOR)

#configure and create mainwindow (2)
ws = Tk()
ws.geometry("500x560+560+200")
ws.title("To-Do List")
ws.resizable(width=False, height=True)
ws.config(bg="#312244")



#create widgets like frame, buttons, scrollbar, listbox and inputbox (4)
frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width = 30,
    height = 9,
    font = ("Helvetica", 20),
    bd=0,
    fg="#464646",
    selectbackground = "#cdb4db",
    activestyle="none",
    highlightthickness=0


)
lb.pack(side=LEFT, fill=BOTH)

#make a storagelist
task_list = [
    "code a To-Do list",
    "play spellbreak"
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_input = Entry(
    ws,
    font=("Helvetica", 20)

)
my_input.pack(pady=20
)
button_frame = Frame(ws)
button_frame.pack(pady=20)

#add buttons 
add_button = Button(
    button_frame,
    text="Add",
    font=("Helvetica", 15),
    bg="#95d5b2",
    padx=20,
    pady=10,
    command = newTask

)
add_button.pack(side=LEFT, fill=BOTH, expand=True)

delete_button = Button(
    button_frame,
    text="Delete",
    font=("Helvetica", 15),
    bg="#f08080",
    padx=17,
    pady=10,
    command = deleteTask

)
delete_button.pack(side=LEFT, fill=BOTH, expand=True)

#credits
txt = Label(ws, text="made by senpai_knock")
txt.pack(pady=10)

#start a loop in order to see the tkinter window, mainloop(3)
ws.mainloop()


