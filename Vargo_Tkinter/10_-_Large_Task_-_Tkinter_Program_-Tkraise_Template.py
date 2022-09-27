from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# frame initiation
root = Tk()
root.geometry("1920x1000")
root.propagate(False)

# frame style
style = ttk.Style()
style.configure("ok.TButton", font=("Calibri",20,"bold"), justify='center')
style.configure("desc.TLabel", font=("Calibri",16))

# load the image

# for main page
image_data = ['Image\\image1.png']
image = []
for path in image_data:
    image1 = Image.open(path)
    image1 = image1.resize((1000,600))
    image1 = ImageTk.PhotoImage(image1)
    image.append(image1)

# for stories
image_data = ['Image\\image2.png',
    'Image\\image3a.png','Image\\image3b.png',
    'Image\\image4a.png','Image\\image4b.png','Image\\image4c.png','Image\\image4d.png',
    'Image\\image5a.png','Image\\image5b.png','Image\\image5c.png','Image\\image5d.png',
    'Image\\image5e.png','Image\\image5f.png','Image\\image5g.png','Image\\image5h.png']
for path in image_data:
    image1 = Image.open(path)
    image1 = image1.resize((900,550))
    image1 = ImageTk.PhotoImage(image1)
    image.append(image1)

# Define the main window for each page
page1 = ttk.Frame(root)
page2 = ttk.Frame(root)

page3 =[]
for data in range(2):
     page3.append(ttk.Frame(root))

page4 = []
for data in range(4):
    page4.append(ttk.Frame(root))

page5 = []
for data in range(8):
    page5.append(ttk.Frame(root))

# Create a function to easily use tkraise method
def raise_frame(frame):
    frame.tkraise()

def next_step():
    if mandatory_entry.get():
        # the user entered data in the mandatory entry: proceed to next step
        raise_frame(page2)
    else:
        # the mandatory field is empty
        mandatory_entry.focus_set()

#------PAGE 1---------------------

# Create the widgets
mandatory_entry = ttk.Entry(page1, width=30, font=('Calibri',16))
page1image = ttk.Label(page1, text='Image Page 1', image=image[0])
page1_entrylabel = ttk.Label(page1, text='Input Name', style="desc.TLabel")
page1button = ttk.Button(page1, text='Start', style="ok.TButton", command=next_step)

# Place the widgets
page1['padding'] = (250,50)

page1.grid(column=0, row=0)
page1image.grid(column=0,row=1, columnspan=3, pady=(0,25))
page1_entrylabel.grid(column=0, row = 2)
mandatory_entry.grid(column=1, row = 2)
page1button.grid(column=2, row=2)

def create_page_story(root_frame, title_text, image, button_a_label, button_b_label, page_back_act, page_a_act, page_b_act, lastpage = False):
    # Create the widgets
    frame_a = ttk.Frame(root_frame, width=1920,height=200)
    page_label = ttk.Label(frame_a, text=title_text, style="desc.TLabel")

    frame_b = ttk.Frame(root_frame, width=1920, height=800)
    page_image = ttk.Label(frame_b, text='Image Page', image=image)
    page_button1 = ttk.Button(frame_b, text='Back', style="ok.TButton", command=lambda:raise_frame(page_back_act))

    if not lastpage:
        page_button2 = ttk.Button(frame_b, text=button_a_label, style="ok.TButton", command=lambda:raise_frame(page_a_act))
        page_button3 = ttk.Button(frame_b, text=button_b_label, style="ok.TButton", command=lambda:raise_frame(page_b_act))
    else:
        page_button2 = ttk.Button(frame_b, text="Restart", style="ok.TButton", command=lambda:raise_frame(page1))

    # Place the widgets
    root_frame['padding'] = (250,0)
    frame_a['padding'] = (0,0,0,10)

    root_frame.grid(column=0, row=0)
    frame_a.grid(column=0, row=0)
    frame_b.grid(column=0, row=1)

    page_label.grid(column=0, row=0)

    if not lastpage:
        page_image.grid(column=0, row=2, columnspan=3, pady=(0,10))
        page_button1.grid(column=0, row=3)
        page_button2.grid(column=1, row=3)
        page_button3.grid(column=2, row=3)
    else:
        page_image.grid(column=0, row=2, columnspan=2, pady=(0,40))
        page_button1.grid(column=0, row=3)
        page_button2.grid(column=1, row=3)

    return root_frame

title_text = '''Boby is a 23-year-old male. He is from Canada and his tour group has fled away. You are now
in charge of bossing him around the city. Remember, you're not touring him; you're bossing him
because, apparently, he doesn't have a choice in this game, unlike you.'''

# page2
page2 = create_page_story(page2, title_text, image[1], "Bring him to\nSanta Monica Pier", "Bring him to\nThe Griffith Observatory", page1, page3[0], page3[1])

# # page3
title_text='''
You've decided to take Bop to the Santa Monica Pier. He is exhausted and sweating profusely
as a result of the hot weather. He needs food.'''
create_page_story(page3[0], title_text, image[2], "Ask him to\nFish", "5-star\nrestaurant", page2, page4[0], page4[1])

title_text='''
You've decided to take Bop to Griffith Observatory. You arrived a little early, so sunset will be
just around the corner by the time his free parking runs out.'''
create_page_story(page3[1], title_text, image[3], "Wait for\nthe sunset", "We should\ngo!", page2, page4[2], page4[3])

# page4
title_text='''
Oh no! His fishing rod was bitten and dragged away by a shark. Bop has entered the waters.
He meets a cute shark. What should he do now?'''
create_page_story(page4[0], title_text, image[4], "Pet the\nShark", "Fight the\nShark", page3[0], page5[0], page5[1])

title_text='''
The restaurant charged Bop $740 for his wagyu steak. He can’t afford to pay. 
What should Bop do?'''
create_page_story(page4[1], title_text, image[5], "Run\nAway", "Sell all\nBop's assets", page3[0], page5[2], page5[3])

title_text='''
Poor Bop got his car towed away.
He is now carless, what should he do now?'''
create_page_story(page4[2], title_text, image[6], "Steal \na Car", "Run back\nhome", page3[1], page5[4], page5[5])

title_text='''
Bop sprained his ankle rushing to his car to avoid the parking fee. When he tripped, he fractured
his ribs. Remember, medical school taught you nothing, you didn’t graduate and you got broke. How to start?'''
create_page_story(page4[3], title_text, image[7], "Call\n911", "Use your\nKnowledge", page3[1], page5[6], page5[7])

# page5
title_text='''
The shark has made the conscious decision to interpret Bop's following movement as a hostile
one. The cuteness of his appearance belies his unfriendly nature. Poor Bop.'''
create_page_story(page5[0], title_text, image[8], "", "", page4[0], page4[0], page4[0], lastpage=True)

title_text='''
What was Bop thinking?! Oh well, you managed to kill him with your domineering ways. Pray
that Bop finally finds some peace.'''
create_page_story(page5[1], title_text, image[9], "", "", page4[0], page4[0], page4[0], lastpage=True)

title_text='''
Bop might as well be the steak now. 
Rest in peace Bop.'''
create_page_story(page5[2], title_text, image[10], "", "", page4[1], page4[0], page4[0], lastpage=True)

title_text='''
Terrible! Bop sold his one and only valuable item: the ring he stole from the pawn shop.
This might as well be his karma.'''
create_page_story(page5[3], title_text, image[11], "", "", page4[1], page4[0], page4[0], lastpage=True)

title_text='''
Sadly, Bop attempted to rob an undercover cop's car.
What an adventure, Bop!'''
create_page_story(page5[4], title_text, image[12], "", "", page4[2], page4[0], page4[0], lastpage=True)

title_text='''
Bop encountered a cardiac arrest after walking 20km back home. 
What a tragic and unfortunate death.'''
create_page_story(page5[5], title_text, image[13], "", "", page4[2], page4[0], page4[0], lastpage=True)

title_text='''
They didn’t get there on time.
Internal bleeding got Bop dead.'''
create_page_story(page5[6], title_text, image[14], "", "", page4[3], page4[0], page4[0], lastpage=True)

title_text='''
Yucks! You accidentally poked his heart
during the surgery.'''
create_page_story(page5[7], title_text, image[15], "", "", page4[3], page4[0], page4[0], lastpage=True)

#---RAISING PAGE 1 TO START PROGRAM--------
raise_frame(page1)
root.mainloop()