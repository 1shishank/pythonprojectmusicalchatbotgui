from tkinter import *




def dr():
    def send():
        send = " You = >" + e.get()
        txt.insert(END, " \n" + send)
        if (e.get() == "hello"):
            txt.insert(END,
                       "\n" + "shawn => hi this is your guitar teacher plz select your level as a guitarist you think you are \n* beginner \n* intermediate \n* pro "

                       )
        elif (e.get() == "beginner"):
            txt.insert(END,
                       "\n" + "shawn => so u are a beginner so u need to start from basics kindly refer to following videos fro learning basic sounds \n most basic sounds if u dont know anything \nhttps://www.youtube.com/watch?v=GC_SzDCEIrc "
                       )
        elif (e.get() == "intermediate"):
            txt.insert(END,
                       "\n" + "shawn=>so you are intremediate kindly select the intermediate sounds you want to learn  ")

        elif (e.get() == "pro"):
            txt.insert(END,
                       "\n" + "shawn =>so u are a pro beatboxer kindly visit the following links for practice \n https://www.youtube.com/watch?v=D3-UfEuHqcg")
        else:
            txt.insert(END, "\n" + "shawn => didint get it kindy select from the given options")
        e.delete(0, END)

    root = Tk()
    global txt
    global e
    txt = Text(root)
    txt.grid(row=0, column=1, columnspan=2, rowspan=1)
    e = Entry(root, width=100)
    e.grid(row=1, column=1)
    root.title("shawn the drummer")

    send = Button(root, text="send",command=send).grid(row=1, column=2, padx=20, pady=20)
    root.mainloop()

