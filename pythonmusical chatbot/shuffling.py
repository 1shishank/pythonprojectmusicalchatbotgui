from tkinter import *




def shuff():
    def send():
        send = " You = >" + e.get()
        txt.insert(END, " \n" + send)
        if (e.get() == "hello"):
            txt.insert(END,
                       "\n" + "mj => hi this is your shuffling teacher plz select your level as  you think you are \n* beginner \n* intermediate \n* pro "

                       )
        elif (e.get() == "beginner"):
            txt.insert(END,
                       "\n" + "mj => so u are a beginner so u need to start from basics kindly refer to following videos fro learning basic  \n most basic sounds if u dont know anything \nhttps://www.youtube.com/watch?v=GC_SzDCEIrc "
                       )
        elif (e.get() == "intermediate"):
            txt.insert(END,
                       "\n" + "mj =>so you are intremediate kindly select the intermediate  you want to learn \n * straight \n * legs   ")
        elif (e.get() == "straight"):
            txt.insert(END,
                       "\n" + "mj => kindly refer to the following video \nhttps://www.youtube.com/watch?v=RRYHW4ONgx8 ")
        elif (e.get() == "legs"):
            txt.insert(END,
                       "\n" + "mj=> kindly refer to the following video \nhttps://www.youtube.com/watch?v=RRYHW4ONgx8 ")
        elif (e.get() == "pro"):
            txt.insert(END,
                       "\n" + "mj =>so u are a pro beatboxer kindly visit the following links for practice \n https://www.youtube.com/watch?v=D3-UfEuHqcg")
        else:
            txt.insert(END, "\n" + "mj => didint get it kindy select from the given options")
        e.delete(0, END)

    root = Tk()
    global txt
    global e
    txt = Text(root)
    txt.grid(row=0, column=1, columnspan=2, rowspan=1)
    e = Entry(root, width=100)
    e.grid(row=1, column=1)
    root.title("mj the dancer")

    send = Button(root, text="send",command=send).grid(row=1, column=2, padx=20, pady=20)
    root.mainloop()

