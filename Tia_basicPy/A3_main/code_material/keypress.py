import tkinter as tk

def foo(event):
    global label
    label.config(text=f"{event.char}, {event.keysym}, {event.keycode}")
    return None

root = tk.Tk()
root.geometry("200x200")

label = tk.Label(
    root,
    text="Empty",
)

label.pack(
    expand=tk.TRUE,
)

root.bind_all("<Key>", foo)
root.mainloop()