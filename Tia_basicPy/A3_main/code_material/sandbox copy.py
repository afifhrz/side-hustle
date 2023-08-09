import tkinter as tk
from tkinter.ttk import Button

class Calc():
    def __init__(self, root: tk.Tk) -> None:
        self._root = root
        self._root.geometry("500x300")
        self._display = ""

        display_frame = tk.Frame(
            self._root,
            bg="red"
            )
        
        display_frame.pack(
            side=tk.TOP,
            fill=tk.BOTH
        )

        self._display_label = tk.Label(
            display_frame,
            text = self._display
        )
        self._display_label.pack(
            side=tk.LEFT
        )

        self._number_frame = tk.Frame(
            self._root,
            bg="green"
            )

        self._number_frame.pack(
            side=tk.LEFT,
            expand=tk.TRUE
        )

        # numbers 0 through 8
        for k in range(0, 9, 3):
            frame = tk.Frame(self._number_frame)
            for num in range(k, k+3):
                self._make_num_button(frame, num).pack(side=tk.LEFT)
            frame.pack()

        # special row
        frame = tk.Frame(self._number_frame)
        self._make_num_button(frame, 9).pack(side=tk.LEFT)
        frame.pack(
            side=tk.LEFT
        )

        def clear():
            """
            """
            self._display = ""
            self._display_label.config(text=self._display)

        tk.Button(
            self._number_frame,
            text="C",
            width=2,
            padx=5,
            pady=5,
            command=clear
        ).pack(
            side=tk.LEFT
        )

        arith_frame = tk.Frame(
            self._root,
            bg="blue"
            )

        self._make_action_button(
            arith_frame,
            "+"
        ).pack()

        self._make_action_button(
            arith_frame,
            "-"
        ).pack()

        self._make_action_button(
            arith_frame,
            "*"
        ).pack()

        def go_equal():
            """
            """
            print("Equals")
            self._display_label.config(text=str(eval(self._display)))

        tk.Button(
            arith_frame,
            text="=",
            width=2,
            padx=5,
            pady=5,
            command=go_equal
        ).pack()

        arith_frame.pack(
            side=tk.LEFT,
            expand=tk.TRUE,
            #fill=tk.BOTH
        )
    
    def _make_num_button(self, frame: tk.Frame, num: int) -> tk.Button:
        """
        """

        def foo():
            # DEBUG PURPOSES
            print(f"{num}")

            # UPDARTE THE DISPLAY
            self._display += str(num)
            self._display_label.config(text=self._display)


        return tk.Button(
            frame,
            text=str(num),
            width=2,
            padx=5,
            pady=5,
            command=foo
        )

    def _make_action_button(self, frame: tk.Frame, symbol: str) -> tk.Button:

        def foo():
            """
            """
            # DEBUGGING
            print(symbol)

            self._display += symbol
            self._display_label.config(text=self._display)

        return tk.Button(
            frame,
            text=symbol,
            width=2,
            padx=5,
            pady=5,
            command=foo
        )


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calc(root)
    root.mainloop()