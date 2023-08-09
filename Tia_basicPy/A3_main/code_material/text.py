import tkinter as tk

def foo() -> None:
    global entry
    print(entry.get())
    return None

root = tk.Tk()
root.geometry("400x100")

entry = tk.Entry(
    root, 
    bg = "light blue"
)
entry.pack(
    side=tk.LEFT,
    expand=tk.TRUE
)

button = tk.Button(
    root,
    text="echo in bash",
    command=foo
)
button.pack(
    side=tk.LEFT,
    expand=tk.TRUE
)

root.mainloop()