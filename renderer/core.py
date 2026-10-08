import tkinter as tk


def start():
    root = tk.Tk()

    window = tk.Canvas(root,width= root.winfo_x(),height=root.winfo_y(),background='black')
    window.pack(expand=True,fill="both")

    root.mainloop()
