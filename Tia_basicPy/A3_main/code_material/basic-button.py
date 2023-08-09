import tkinter as tk

def foo():
    print("Ouch")

root = tk.Tk()
root.geometry("200x200")

button = tk.Button(
    root,
    text="Press",
    command=foo
).pack(
    expand=tk.TRUE,
)

root.mainloop()