from tkinter import *
import tkinter.messagebox

def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning !!!", message="Please enter text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add Task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add Task", command=add)
    button_temp.pack()
    root1.mainloop()

def deletetask():
    selected = listbox_task.curselection()
    if selected:
        listbox_task.delete(selected[0])

def markcompleted():
    selected = listbox_task.curselection()
    if selected:
        marked_text = listbox_task.get(selected)
        marked_text += " /Completed"
        listbox_task.delete(selected)
        listbox_task.insert(selected, marked_text)

window = Tk()
window.title("To Do List GUI")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="bold")
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Add Task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete Selected Task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as Completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
