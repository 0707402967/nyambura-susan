import tkinter
print("imported") 
root = tkinter.Tk

root.title("student registration form")
name_label = tkinter.Label(root,text = "Enter students name")
name_label.pack()
name_textbox = tkinter.Entry(root)
name_textbox.pack()

root.title("student registration form")
Age_label = tkinter.Label(root,text = "Enter age")
Age_label.pack()
Age_textbox = tkinter.Entry(root)
Age_textbox.pack()

root.title("student registration form")
date_label = tkinter.Label(root,text ="Enter registration date")
date_label.pack()
date_textbox = tkinter.Entry(root)
date_textbox.pack()

root.mainloop()




