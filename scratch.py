import tkinter as tk, random

paper = tk.Tk()
paper.geometry("400x300")
paper.title("Lotto")

win = random.randint(1, 10)
attempt = 0

for i in range(3):
    for j in range(3):
        num = tk.Button(paper, width=10, height=5, text="X")
        num.grid(row=i, column=j, padx=10, pady=5)

result = tk.Text(paper, width=20, height=3)
result.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

def winning():
    global win, attempt
    contain = random.randint(1, 10)
    if contain == win:
        win_win = tk.Toplevel(paper)
        win_win.geometry("200x100")
        win_win.title("You won")
        mess = tk.Text(win_win, width=20, height=3)
        mess.insert("1.0", "You won, hoorayyy")
        mess.place(rely=.2, relx=.1)
    else:
        result.delete("1.0", tk.END)
        result.insert("1.0", "OH BAD LUCK, TRY AGAIN, the number inside was")
        result.insert("2.0",contain)
        attempt += 1

if attempt > 3:
    result.delete("1.0", tk.END)
    result.insert("1.0", "You lost, better luck next time")
        
for i in paper.winfo_children():
    if isinstance(i, tk.Button):
        i.config(command=winning)

paper.mainloop()