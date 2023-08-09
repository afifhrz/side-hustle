import tkinter as tk
from random import randint

def foo(event):
    print(f"{event.x} {event.y}")

root = tk.Tk()
root.geometry("200x200")

canvas = tk.Canvas(
    root,
    bg="purple"
)

canvas.bind("<Motion>", foo)

canvas.pack(
    expand=tk.TRUE,  #important
    fill=tk.BOTH     #important
)

root.mainloop()