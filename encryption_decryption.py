from tkinter import *
import pybase64

root = Tk()
# Channel Name
root.title('Codemy.com - Encrypt/Decrypt BAse64')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")


def clear():
    pass
def encrypt():
    pass
def decrypt():
    pass

my_frame = Frame(root)
my_frame.pack(pady=20)

enc_button = Button(my_frame, text="Encrypt", font=("Helvetica", 18), command=encrypt)
enc_button.grid(row=0, column=0)

dec_button = Button(my_frame, text="Decrypt", font=("Helvetica", 18), command=decrypt)
dec_button.grid(row=0, column=1)

clear_button = Button(my_frame, text="Clear", font=("Helvetica", 18), command=clear)
clear_button.grid(row=0, column=2)

root.mainloop()