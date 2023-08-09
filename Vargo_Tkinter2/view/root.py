from tkinter import Tk, ttk

class Root(Tk):
    def __init__(self):
        super().__init__()

        start_width = 1920        
        start_height = 1000

        self.geometry(f"{start_width}x{start_height}")
        self.propagate(False)
        self.title("Diet App Tracker")
        
        # style
        self.style = ttk.Style()

        ## define the ok.TButton Style
        self.font_style = "Roboto"
        self.style.configure("ok.TButton", font=(self.font_style,20,"bold"), justify='center')

        ## define the desc.TLabel Style
        self.style.configure("desc.TLabel", font=(self.font_style,20))
        self.style.configure("title.TLabel", font=(self.font_style,30,"bold"), justify="center")
        
        self.username_logged_in = ''
        self.user_id = 0
