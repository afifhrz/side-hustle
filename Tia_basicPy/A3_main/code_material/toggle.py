import tkinter as tk

def toggle() -> None:
    global frame

    if frame["bg"] == "purple":
        frame.config(bg="yellow")
    else:
        frame.config(bg="purple")

    return None

root = tk.Tk()
root.geometry("200x200")

frame = tk.Frame(
    root,
    bg="purple"
)

button = tk.Button(
    frame,
    text="press me",
    command=toggle
)

button.pack(
    expand=tk.TRUE
)

frame.pack(
    expand=tk.TRUE,
    fill=tk.BOTH
)

root.mainloop()