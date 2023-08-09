import tkinter as tk

def foo(event):
    global label
    label.config(text=f"{event.char}   {event.keysym}   {event.keycode}")

root = tk.Tk()
root.geometry("200x200")

label = tk.Label(
    text="X",
)

label.pack(
    expand=tk.TRUE
)

root.bind_all("<Key>", foo)

root.mainloop()