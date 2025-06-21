import tkinter as tk

main = tk.Tk()
main.title("HELLO")
main.geometry("400x300")
main.grid_rowconfigure(0, weight=1)
main.grid_columnconfigure(0, weight=1)

quest = tk.Text(main, width=20, height=3)
quest.place(rely=.2, x=133)
choice1 = tk.Button(main, width=10)
choice1.place(relx=.2, rely=0.5)
choice2 = tk.Button(main, width=10)
choice2.place(rely=.5, relx=.6)

main.mainloop()