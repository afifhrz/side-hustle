from __future__ import annotations
import tkinter as tk


class Calculator():
    def __init__(self, master: tk.Tk) -> None:
        self.expression = ""

        # do all of the layout
        self.master = master
        self.master.geometry("300x300")
        self.master.title("Calculator")

        ## DISPLAY
        frame = tk.Frame(
            self.master,
            bg="red"
        )
        frame.pack(
            side=tk.TOP,
            fill=tk.X
        )
        self.display = tk.Label(
            frame,
            text="Hello World",
            bg="blue"
        )
        self.display.pack(
            anchor=tk.W
        )

        ## NUMBERED BUTTONS
        buttons = []

        frame_numbers = tk.Frame(
            self.master
        )
        frame_numbers.pack(
            side=tk.LEFT,
            expand=tk.TRUE
        )

        # ROW 1
        frame = tk.Frame(
            frame_numbers,
            bg="purple"
        )

        buttons.append(self._make_button(frame, "0"))
        buttons.append(self._make_button(frame, "1"))
        buttons.append(self._make_button(frame, "2"))

        frame.pack(
            side=tk.TOP,
            expand=tk.TRUE,
            fill=tk.BOTH
        )

        # ROW 2
        frame = tk.Frame(
            frame_numbers,
            bg="purple"
        )

        buttons.append(self._make_button(frame, "3"))
        buttons.append(self._make_button(frame, "4"))
        buttons.append(self._make_button(frame, "5"))

        frame.pack(
            side=tk.TOP,
            expand=tk.TRUE,
            fill=tk.BOTH
        )

        # ROW 3
        frame = tk.Frame(
            frame_numbers,
            bg="purple"
        )

        buttons.append(self._make_button(frame, "6"))
        buttons.append(self._make_button(frame, "7"))
        buttons.append(self._make_button(frame, "8"))

        frame.pack(
            side=tk.TOP,
            expand=tk.TRUE,
            fill=tk.BOTH
        )

# ROW 3
        frame = tk.Frame(
            frame_numbers,
            bg="purple"
        )

        buttons.append(self._make_button(frame, "."))
        buttons.append(self._make_button(frame, "9"))
        buttons.append(self._make_button(frame, "C"))

        frame.pack(
            side=tk.TOP,
            expand=tk.TRUE,
            fill=tk.BOTH
        )

        # PACK ALL BUTTONS
        for button in buttons:
            button.pack(
                side=tk.LEFT
            )

        ## OPERATION BUTTONS
        buttons = []

        frame_ops = tk.Frame(
            self.master
        )
        frame_ops.pack(
            side=tk.RIGHT,
            expand=tk.TRUE
        )

        buttons.append(self._make_button(frame_ops, "+"))
        buttons.append(self._make_button(frame_ops, "-"))
        buttons.append(self._make_button(frame_ops, "×"))
        buttons.append(self._make_button(frame_ops, "÷"))
        buttons.append(self._make_button(frame_ops, "="))

        for button in buttons:
            button.pack(side=tk.TOP)

        equal_button = buttons[-1]
        def handler():
            ans = eval(self.expression)
            self.display.config(text=str(ans))
            self.expression = ""
            return None

        equal_button.config(command=handler)



    def _make_button(self, frame: tk.Frame, cs: str) -> tk.Button:

        def handler() -> None:
            self.expression += cs
            self.display.config(text=self.expression)
            return None

        button = tk.Button(
            frame,
            text=cs,
            width=2,
            padx=10,
            pady=5,
            command=handler
        )
        return button




if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()