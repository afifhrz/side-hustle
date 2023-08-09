import tkinter as tk

def foo():
    global entry
    print(f"{entry.get()}")

root = tk.Tk()
root.geometry("400x100")

entry = tk.Entry(
    root,
    bg="light blue",
    fg="black"
)

entry.pack(
    side=tk.LEFT,
    expand=tk.TRUE
    )

tk.Button(
    root,
    text="Echo",
    command=foo
).pack(
    side=tk.LEFT,
    expand=tk.TRUE
    )

root.mainloop()