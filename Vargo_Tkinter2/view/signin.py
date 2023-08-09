from tkinter import Frame, Label, Entry, Button, StringVar

class SignInView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #------PAGE 1 Login---------------------

        # Create the widgets
        width_line = 475
        self.horizontal_line1 = Frame(self, bg='black', height=1, width=width_line)
        self.horizontal_line2 = Frame(self, bg='black', height=1, width=width_line)
        self.horizontal_line3 = Frame(self, bg='black', height=1, width=width_line)

        self.titleLabel = Label(self, text='Diet Tracker App')

        self.username = StringVar()
        self.usernameEntry = Entry(self, textvariable=self.username, width=30)
        self.usernameLabel = Label(self, text='Username')

        self.password = StringVar()
        self.passwordEntry = Entry(self, textvariable=self.password, show='*', width=30)
        self.passwordLabel = Label(self, text='Password')

        self.page1login_button = Button(self, width=30, text='Login')
        self.page1create_user = Button(self, width=30, text='Create Account')

        # Place the widgets
        self.padding = (50,50)

        ## initialize place
        self.grid(column=0, row=0, columnspan=3)

        self.titleLabel.grid(column=1,row=0, pady=(0,25))
        self.horizontal_line1.grid(column=0,row=1, pady=(0,100))
        self.horizontal_line2.grid(column=1,row=1, pady=(0,100))
        self.horizontal_line3.grid(column=2,row=1, pady=(0,100))
        self.usernameLabel.grid(column=1, row = 2, pady=(0,25))
        self.usernameEntry.grid(column=1, row = 3, pady=(0,50))
        self.passwordLabel.grid(column=1, row = 4, pady=(0,25))
        self.passwordEntry.grid(column=1, row = 5, pady=(0,200))
        self.page1login_button.grid(column=1, row=6)
        self.page1create_user.grid(column=0, row=6)