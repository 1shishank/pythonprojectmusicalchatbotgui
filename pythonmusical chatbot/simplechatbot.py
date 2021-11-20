from tkinter import *




def fun():
    def send():
        send = " You = >" + e.get()
        txt.insert(END, " \n" + send)
        if (e.get() == "hello"):
            txt.insert(END,
                       "\n" + "sam => hi this is your beatbox teacher plz select your level as a beatboxer you think you are \n* beginner \n* intermediate \n* pro "

                       )
        elif (e.get() == "beginner"):
            txt.insert(END,
                       "\n" + "sam => so u are a beginner so u need to start from basics kindly refer to following videos fro learning basic sounds \n most basic sounds if u dont know anything \nhttps://www.youtube.com/watch?v=GC_SzDCEIrc "
                       )
        elif (e.get() == "intermediate"):
            txt.insert(END,
                       "\n" + "sam =>so you are intremediate kindly select the intermediate sounds you want to learn \n * humming beatbox \n * lip bass \n * lip rolls \n * throat bass  ")
        elif (e.get() == "humming beatbox"):
            txt.insert(END,
                       "\n" + "sam => kindly refer to the following video \nhttps://www.youtube.com/watch?v=RRYHW4ONgx8 ")
        elif (e.get() == "lip bass"):
            txt.insert(END,
                       "\n" + "sam => kindly refer to the following video \nhttps://www.youtube.com/watch?v=7j7f5odEl5U ")
        elif (e.get() == "lip rolls"):
            txt.insert(END,
                       "\n" + "sam => kindly refer to the following video \nhttps://www.youtube.com/watch?v=-50nUNHjo8E ")
        elif (e.get() == "throat bass"):
            txt.insert(END,
                       "\n" + "sam => kindly refer to the following video \nhttps://www.youtube.com/watch?v=HjSnFPYHcyo")
        elif (e.get() == "pro"):
            txt.insert(END,
                       "\n" + "sam =>so u are a pro beatboxer kindly visit the following links for practice \n https://www.youtube.com/watch?v=D3-UfEuHqcg")
        else:
            txt.insert(END, "\n" + "sam => didint get it kindy select from the given options")
        e.delete(0, END)

    root = Tk()
    global txt
    global e
    txt = Text(root)
    txt.grid(row=0, column=1, columnspan=2, rowspan=1)
    e = Entry(root, width=100)
    e.grid(row=1, column=1)
    root.title("sam beatboxer")

    send = Button(root, text="send",command=send).grid(row=1, column=2, padx=20, pady=20)
    root.mainloop()

