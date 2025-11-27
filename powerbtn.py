import tkinter as tk 
import os 
from tkinter import messagebox
import platform 


def stfu():
    confirm=messagebox.askyesno("confirm","ShutDown?")
    if confirm:
        messagebox.showinfo("Shutdown", "Shutdown command executed (simulated).")
def rest():
    confirm = messagebox.askyesno("Confirm", "Do you want to restart?")
    if confirm:
        messagebox.showinfo("Restart", "Restart command executed (simulated).")

root = tk.Tk()
root.title("System Control App")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="<<< Let your computer rest >>>", font=("Times New Roman", 12, "bold"), bg="#f0f0f0")
label.pack(pady=10)

shutdown_btn = tk.Button(root, text="Shutdown", bg="red", fg="white", font=("Arial", 10, "bold"), command=stfu)
shutdown_btn.pack(pady=10, ipadx=10, ipady=5)

restart_btn = tk.Button(root, text="Restart", bg="blue", fg="white", font=("Arial", 10, "bold"), command=rest)
restart_btn.pack(pady=10, ipadx=10, ipady=5)

    
root.mainloop()