import tkinter as tk

def foo():
    global frame
    
    if frame["bg"] == "purple":
        frame.config(bg="yellow")
    else:
        frame.config(bg="purple")

root = tk.Tk()
root.geometry("200x200")

frame = tk.Frame(
    root,
    bg="purple"
)

frame.pack(
    expand=tk.TRUE,
    fill=tk.BOTH
)

tk.Button(
    frame,
    text="Press Me",
    command=foo
).pack(
    expand=tk.TRUE
)

root.mainloop()