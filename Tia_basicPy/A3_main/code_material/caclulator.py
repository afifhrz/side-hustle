from __future__ import annotations
import tkinter as tk

class CalcApp():
    def __init__(self, master: tk.TK) -> None:
        self.master = master
        self.master.title("Calculator")
        self.expression = ""

        #DISPLAY
        frame = tk.Frame(
            self.master,
            bg="black",
            pady=10,
        )
        frame.pack(
            fill=tk.X
        )
        self.display = tk.Label(
            frame,
            text="",
            bg="black",
            fg="white",
        )
        self.display.pack(
            anchor=tk.W,
        )

        #NUMBER PAD
        frame_number_buttons = tk.Frame(
            self.master,
            padx=10,
            pady=10
        )
        frame_number_buttons.pack(
            side=tk.LEFT
        )

        for m in [0,3,6]:
            frame_row = tk.Frame(frame_number_buttons)
            frame_row.pack(side=tk.TOP)
            for k in [0,1,2]:
                self._make_button(frame_row, str(m+k)).pack(side=tk.LEFT)

        # Special Row
        frame_row = tk.Frame(frame_number_buttons)
        frame_row.pack(side=tk.TOP)
        self._make_button(frame_row, ".").pack(side=tk.LEFT)
        self._make_button(frame_row, "9").pack(side=tk.LEFT)
        
        button = self._make_button(frame_row, "C")
        def handler():
            self.expression = ""
            self._refresh()
        button.config(
            command=handler
        )
        button.pack(side=tk.LEFT)

        #OPERATION PAD
        frame = tk.Frame(
            self.master,
            padx=10,
            pady=10
        )
        frame.pack(side=tk.RIGHT)
        self._make_button(frame, "+").pack(side=tk.TOP)
        self._make_button(frame, "-").pack(side=tk.TOP)
        self._make_button(frame, "*").pack(side=tk.TOP)


        button = self._make_button(frame, "=")
        def handler():
            try:
                self.expression = str(eval(self.expression))
                self._refresh()
                print(f"pressed =.  Expresssion {self.expression}")
            except:
                self.expression = "ERROR.  PRESS C TO RESET"
                self._refresh()
        button.config(command=handler)
        button.pack(side=tk.TOP)


    def _make_button(self, root: tk.Tk, cs: str) -> tk.Button:
        def handler():
            self.expression += cs
            self._refresh()
            print(f"pressed {cs}.  Expresssion {self.expression}")

        button = tk.Button(
            root,
            text=cs,
            width=2,
            padx=10,
            pady=10,
            command=handler
        )
        return button

    def _refresh(self):
        self.display.config(
            text=self.expression
        )


if __name__ == "__main__":
    root = tk.Tk()
    calc = CalcApp(root)
    root.mainloop()