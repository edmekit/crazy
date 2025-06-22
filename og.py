import tkinter as tk

main = tk.Tk()
main.title("HELLO")
main.geometry("400x300")
main.grid_rowconfigure(0, weight=1)
main.grid_columnconfigure(0, weight=1)

def yes_win():
    window1= tk.Toplevel(main)
    window1.geometry("200x100")
    window1.title("YEHEEEYYYY")
    mess = tk.Text(window1, width=20, height=3)
    mess.insert("1.0", "YEESSSSS, I LOVE YOUU TOOOO :)))")
    mess.place(rely=.2, relx=.1)

def no_win():
    window2= tk.Toplevel(main)
    window2.geometry("250x100")
    window2.title("awwwwww")
    mess1 = tk.Text(window2, width=25, height=3)
    mess1.insert("1.0", "YES YOU DO, press that yes button")
    mess1.place(rely=.2, relx=.1)


quest = tk.Text(main, width=20, height=3)
quest.place(rely=.2, x=132)
quest.insert("1.0", "Do you love me? :(")
choice1 = tk.Button(main, width=10, text="Yes <33", command=yes_win)
choice1.place(relx=.2, rely=0.5)
choice2 = tk.Button(main, width=10, text="No :((", command=no_win)
choice2.place(rely=.5, relx=.6)

main.mainloop()