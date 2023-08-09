import tkinter as tk
from random import randint
def randcolor() -> str:
    r = lambda: randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def make_label(x: int, frame: tk.Frame) -> tk.Label:
    """
    """
    lab = tk.Label(
        frame,
        text=str(x),
        bg=randcolor(),
        width=2,
        padx=10,
        pady=10
    )
    return lab

root = tk.Tk()
root.geometry("200x200")

main_frame = tk.Frame(root)


for k in range(0, 9, 3):
    row = tk.Frame(main_frame)
    row.pack(side=tk.TOP)
    
    for num in range(k, k+3):
        make_label(num, row).pack(side=tk.LEFT)
    
row = tk.Frame(main_frame)
row.pack(side=tk.TOP)
make_label(9, row).pack(side=tk.LEFT)

main_frame.pack(
    expand = tk.TRUE
)
root.mainloop()