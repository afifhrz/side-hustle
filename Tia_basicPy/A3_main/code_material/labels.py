from __future__ import annotations
from typing import Callable
from random import randint
import tkinter as tk

def randcolor() -> str:
    r = lambda: randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def number_label(root: tk.Tk, x: int) -> tk.Label:
    label = tk.Label(
        root,
        text=str(x),
        bg=randcolor(),
        fg="black",
        width=2,
        padx=10,
        pady=10
    )
    return label

root = tk.Tk()
root.geometry("300x300")


frame_frame = tk.Frame(root); 
frame_frame.pack(
    expand=tk.TRUE
)

row1_frame = tk.Frame(frame_frame); row1_frame.pack()
row2_frame = tk.Frame(frame_frame); row2_frame.pack()
row3_frame = tk.Frame(frame_frame); row3_frame.pack()
row4_frame = tk.Frame(frame_frame); row4_frame.pack()

labels = []
for k in [0, 1, 2]:
    labels.append(number_label(row1_frame, k))

for k in [3, 4, 5]:
    labels.append(number_label(row2_frame, k))

for k in [6, 7, 8]:
    labels.append(number_label(row3_frame, k))

labels.append(number_label(row4_frame, 9))

for label in labels:
    label.pack(side=tk.LEFT)

root.mainloop()