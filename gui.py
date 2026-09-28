from tkinter import *
import os

# Functions
def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

def cancel():
    os.system("shutdown /a")

# Create Window
st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="blue")

# Buttons
r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"),
                  relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart (20 sec)", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=140, height=50, width=200)

lg_button = Button(st, text="Log-Out", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=log_out)
lg_button.place(x=150, y=220, height=50, width=200)

sd_button = Button(st, text="Shutdown", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=shutdown)
sd_button.place(x=150, y=300, height=50, width=200)

cn_button = Button(st, text="Cancel", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=cancel)
cn_button.place(x=150, y=380, height=50, width=200)

# Run App
st.mainloop()
