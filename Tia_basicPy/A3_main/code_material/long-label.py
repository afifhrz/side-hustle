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

row1 = tk.Frame(main_frame)
row1.pack(side=tk.TOP)

make_label(0, row1).pack(side=tk.LEFT)
make_label(1, row1).pack(side=tk.LEFT)
make_label(2, row1).pack(side=tk.LEFT)

row2 = tk.Frame(main_frame)
row2.pack(side=tk.TOP)

make_label(3, row2).pack(side=tk.LEFT)
make_label(4, row2).pack(side=tk.LEFT)
make_label(5, row2).pack(side=tk.LEFT)

row3 = tk.Frame(main_frame)
row3.pack(side=tk.TOP)

make_label(6, row3).pack(side=tk.LEFT)
make_label(7, row3).pack(side=tk.LEFT)
make_label(8, row3).pack(side=tk.LEFT)

row4 = tk.Frame(main_frame)
row4.pack(side=tk.TOP)

make_label(9, row4).pack(side=tk.LEFT)

main_frame.pack(
    expand = tk.TRUE
)
root.mainloop()