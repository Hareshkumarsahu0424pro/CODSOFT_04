import random
import tkinter as tk
from tkinter import messagebox
def play():
    user=user_input.get().lower()
    possible=["rock","paper","scissor"]
    computer=random.choice(possible)
    if user==computer:
        result_label.config(text="it is tie")
    elif user=='rock':
        result_label.config(text="you win" if computer=="scissor" else "computer win")
    elif user=='paper':
       result_label.config(text="you win"if computer=="rock" else "computer win")
    elif user=='scissor':
        result_label.config(text="you win" if computer=="paper" else "computer win")
    else:
        result_label.config(text="invalid choice")
def play_again():
    user_input.delete(0,tk.END)
    result_label.config(text="")
    user_input.focus()
root=tk.Tk()
root.title("rock paper game")
user_input=tk.Entry(root,width=30)
user_input.pack(pady=10)
play_button=tk.Button(root,text='play',command=play)
play_button.pack()
result_label=tk.Label(root,text="",font=("arial",20))
result_label.pack()
play_again_button=tk.Button(root,text='play again',command=play_again)
play_again_button.pack()
quit_button=tk.Button(root,text="quit",command=root.destroy)
quit_button.pack()
root.mainloop()