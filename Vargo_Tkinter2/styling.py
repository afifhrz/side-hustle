from tkinter import ttk

class Styling:
    def __init__(self):
        # frame style
        self.style = ttk.Style()

        ## define the ok.TButton Style
        self.font_style = "Roboto"
        self.style.configure("ok.TButton", font=(self.font_style,20,"bold"), justify='center')

        ## define the desc.TLabel Style
        self.style.configure("desc.TLabel", font=(self.font_style,20))
        self.style.configure("title.TLabel", font=(self.font_style,30,"bold"), justify="center")