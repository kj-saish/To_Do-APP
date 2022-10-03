#importing packages 
from tkinter import * 
import tkinter.messagebox
from turtle import color, left

def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            with open('data.txt', 'a',encoding="utf-8") as t:
                t.write(f'\n{input_text}')
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add)
    button_temp.pack()
    root1.mainloop()
    
#function to facilitate the delete task from the Listbox
def deletetask():
    #selects the selected item and then deletes it 
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])
    with open('data.txt', 'r',encoding="utf-8") as fr:
        # reading line by line
        lines = fr.readlines()
        # pointer for position
        ptr = 0
       # opening in writing mode
        with open('data.txt', 'w',encoding="utf-8") as fw:
            for line in lines:
                # we want to remove 5th line
                if ptr != selected[0]:
                        fw.write(line)
                ptr += 1    

#Executes this to mark completed 
def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)
    with open('completed.txt', 'a',encoding="utf-8") as t:
                t.write(f'{temp_marked}')
    #update it 
    temp_marked=temp_marked+"  \u2713"
    with open('data.txt', 'r',encoding="utf-8") as fr:
        # reading line by line
        lines = fr.readlines()
        # pointer for position
        ptr = 0
       # opening in writing mode
    with open('data.txt', 'w',encoding="utf-8") as fw:
        for line in lines:
            if ptr != marked[0]:
                fw.write(line)
            ptr += 1
   #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)
    
def completedlist():
    root2=Tk()
    root2.title("Completed Task")
    frame_task=Frame(root2)
    frame_task.pack()
    listbox_task=Listbox(frame_task,bg="black",fg="green",height=20,width=50,font = "Helvetica")  
    listbox_task.pack(side=tkinter.LEFT)
    with open('completed.txt', 'r+',encoding="utf-8") as tasks_list:
        for task in tasks_list:
            listbox_task.insert(END, task)
        tasks_list.close()
    root2.mainloop()

def pendinglist():
    root3=Tk()
    root3.title("Pending Task")
    frame_task=Frame(root3)
    frame_task.pack()
    listbox_task=Listbox(frame_task,bg="black",fg="red",height=20,width=50,font = "Helvetica")  
    listbox_task.pack(side=tkinter.LEFT)
    with open('data.txt', 'r+',encoding="utf-8") as tasks_list:
        for task in tasks_list:
            listbox_task.insert(END, task)
        tasks_list.close()
    root3.mainloop()

#creating the initial window
window=Tk()
#giving a title
window.title("To-Do APP")
#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()
#to hold items in a listbox
listbox_task=Listbox(frame_task,bg="black",fg="white",height=20,width=70,font = "Helvetica")  
listbox_task.pack(side=tkinter.LEFT)
#Scrolldown in case the total list exceeds the size of the given window 
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)
with open('data.txt', 'r+',encoding="utf-8") as tasks_list:
    for task in tasks_list:
        listbox_task.insert(END, task)
    tasks_list.close()
#Button widget 
entry_button=Button(window,text="Add task",width=50, background = "blue", fg = "black",command=entertask)
entry_button.pack(side = TOP, expand = True, fill = BOTH)
delete_button=Button(window,text="Delete task",width=50, background = "orange", fg = "black",command=deletetask)
delete_button.pack(side = TOP, expand = True, fill = BOTH)
mark_button=Button(window,text="Mark as completed ",width=50, background = "yellow", fg = "black",command=markcompleted)
mark_button.pack(side = TOP, expand = True, fill = BOTH)
comp_button=Button(window,text="Completed task",width=50,background = "green", fg = "black",command=completedlist)
comp_button.pack(side = TOP, expand = True, fill = BOTH)
pend_button=Button(window,text="Pending task",width=50,background = "red", fg = "black",command=pendinglist)
pend_button.pack(side = TOP, expand = True, fill = BOTH)
window.mainloop()



