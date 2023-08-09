import tkinter as tk

def foo(event):
    print(event.x, event.y)
    return None

root = tk.Tk()
root.geometry("200x200")

canvas = tk.Canvas(
    root,
    bg = "purple"
)

canvas.pack(
    fill=tk.BOTH,
    expand=tk.TRUE
)
canvas.bind("<Motion>", foo)
canvas.bind("<Button>", foo)

root.mainloop()