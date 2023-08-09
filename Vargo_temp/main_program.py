from tkinter import *
from functools import partial
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from tktimepicker import SpinTimePickerModern
from datetime import date

import pandas as pd

# frame initiation
root = Tk()
root.geometry("1920x1000")
root.propagate(False)
username_logged_in = ''
user_id = 0

# open image
image = {
    'house':ImageTk.PhotoImage(Image.open('image\\House.png').resize((200,150))),
    'house_select':ImageTk.PhotoImage(Image.open('image\\House Selected.png').resize((200,150))),
    'plate':ImageTk.PhotoImage(Image.open('image\\Plate Symbol.png').resize((200,150))),
    'plate_select':ImageTk.PhotoImage(Image.open('image\\Plate Selected.png').resize((200,150))),
    'heart':ImageTk.PhotoImage(Image.open('image\\Heart Symbol.png').resize((200,150))),
    'heart_select':ImageTk.PhotoImage(Image.open('image\\Heart Selected.png').resize((200,150))),
    'log':ImageTk.PhotoImage(Image.open('image\\Log Book.png').resize((200,150))),
    'log_select':ImageTk.PhotoImage(Image.open('image\\Log Book Selected.png').resize((200,150))),
    'gear':ImageTk.PhotoImage(Image.open('image\\Gear.png').resize((200,150))),
    'gear_select':ImageTk.PhotoImage(Image.open('image\\Gear Selected.png').resize((200,150))),
    'down':ImageTk.PhotoImage(Image.open('image\\Down.png').resize((50,50))),
}

# frame style
style = ttk.Style()

## define the ok.TButton Style
font_style = "Roboto"
style.configure("ok.TButton", font=(font_style,20,"bold"), justify='center')

## define the desc.TLabel Style
style.configure("desc.TLabel", font=(font_style,20))
style.configure("title.TLabel", font=(font_style,30,"bold"), justify="center")

# Define the main window for each page
page1 = {
    'login':ttk.Frame(root),
    'new_user':ttk.Frame(root)
    }

page2 = {
    'main_home':ttk.Frame(root),
    'create_plan':ttk.Frame(root),
    'calculate_bmi':ttk.Frame(root)
    }

page3 = {
    'calories_home':ttk.Frame(root),
    'create_food':ttk.Frame(root),
    'create_drink':ttk.Frame(root),
}

page4 = {
    'exercise':ttk.Frame(root),
}

page5 = {
    'log_exercise':ttk.Frame(root),
}

page6 = {
    'settings':ttk.Frame(root),
}

# Create a function to easily use tkraise method
def raise_frame(frame):
    frame.tkraise()

# Validate the login 
# source: https://pythonexamples.org/python-tkinter-login-form/
def validateLogin(username, password):
    global user_id, username_logged_in
    database_user = pd.read_csv('database_user.csv')
    if (username.get() == "" and password.get() == "") :
        messagebox.showinfo("", "Blank Not allowed")
    elif username.get() in list(database_user['username']):
        data_user = database_user[database_user['username']==username.get()]
        if password.get() in list(data_user['password']):
            messagebox.showinfo("","Login Success")
            user_id = database_user[database_user['username'] == username.get()]['id'].values[0]
            username_logged_in = username.get().title()
            
            main_home()
        else:
            messagebox.showinfo("","Incorrent Password")
    else:
        messagebox.showinfo("","Username not found")

# registering new user
# https://stackoverflow.com/questions/67363342/python-login-verification-tkinter
def register_user(username, password):
    max_id = max(pd.read_csv('database_user.csv')['id'])
    max_id += 1
    file = open("database_user.csv", "a")
    file.write(f"\n{max_id},{username.get()},{password.get()}")
    file.close()
    messagebox.showinfo("","Successfully Registered!")
    raise_frame(page1['login'])

# controller main homepage
def main_home(optionset = 0):
    # global main_home_titleLabel
    main_home_titleLabel = ttk.Label(page2['main_home'], text=f'Hello, {username_logged_in}', style="title.TLabel")
    main_home_titleLabel.grid(column=2,row=0, pady=(0,25))
    
    # global main_home_dropdown, w
    main_home_dropdown = StringVar()
    data = pd.read_csv('database_plan.csv')
    options = data[data['user_id'] == user_id]['plan_name'].values
    if options.size > 0:        
        main_home_dropdown.set(options[optionset]) # default value
    else:
        main_home_dropdown.set("") # default value
    w = OptionMenu(page2['main_home'], main_home_dropdown, *options)
    pos_x = 150
    w.place(x=pos_x+300, y=200)
    
    plan_choosed = data[data['plan_name'] == options[optionset]]
    datefrom_splitted = plan_choosed['datefrom'].values[0].split("/")
    dateto_splitted = plan_choosed['dateto'].values[0].split("/")
    datefrom_splitted[2] = '20' + datefrom_splitted[2] 
    dateto_splitted[2] = '20' + dateto_splitted[2] 
    d0 = date(int(datefrom_splitted[2]), int(datefrom_splitted[0]), int(datefrom_splitted[1]))
    d1 = date(int(dateto_splitted[2]), int(dateto_splitted[0]), int(dateto_splitted[1]))
    delta = d1 - d0
    duration = delta.days
    days_left = (d1 - date.today()).days
    
    main_home_planduration_label = ttk.Label(page2['main_home'], text=f'Plan Duration:{duration}', style="desc.TLabel")
    main_home_daysleft_label = ttk.Label(page2['main_home'], text=f'Days Left:{days_left}', style="desc.TLabel")
    main_home_planduration_label.place(x=pos_x, y=250)
    main_home_daysleft_label.place(x=pos_x, y=300)
    
    progress = ttk.Progressbar(page2['main_home'], orient = HORIZONTAL,length = 525)
    progress['value'] = plan_choosed['calories_get'].values[0]/plan_choosed['calories'].values[0]*100
    progress_label = ttk.Label(page2['main_home'], text=f"{plan_choosed['calories_get'].values[0]}/{plan_choosed['calories'].values[0]} calories burned", style="desc.TLabel")
    progress.place(x=800, y=250)
    progress_label.place(x=800, y=300)
    
    raise_frame(page2['main_home'])

def main_food(optionset = 0):
    food_tracker_dropdown = StringVar()
    data_food = pd.read_csv('database_mst_food.csv')
    options_food = data_food['food_name'].values
    if options_food.size > 0:        
        food_tracker_dropdown.set(options_food[optionset]) # default value
    else:
        food_tracker_dropdown.set("") # default value
    food_dd = OptionMenu(page3['calories_home'], food_tracker_dropdown, *options_food)
    food_dd.place(x=400, y=350)
    
    drink_tracker_dropdown = StringVar()
    data_drink = pd.read_csv('database_mst_drink.csv')
    options_drink = data_drink['drink_name'].values
    if options_drink.size > 0:        
        drink_tracker_dropdown.set(options_drink[optionset]) # default value
    else:
        drink_tracker_dropdown.set("") # default value
    drink_dd = OptionMenu(page3['calories_home'], drink_tracker_dropdown, *options_drink)
    drink_dd.place(x=400, y=400)
    
    calculatecalories = partial(calculate_calories, food_tracker_dropdown, drink_tracker_dropdown)
    page3calculate_button = ttk.Button(page3['calories_home'], width=18, text='Calculate Calories', style="ok.TButton", command=calculatecalories)
    page3calculate_button.grid(column=1, row=5, pady=(0,0))
    
    raise_frame(page3['calories_home'])

def main_heart():
    raise_frame(page4['exercise'])

def main_log():
    data_calories_income = pd.read_csv('database_log.csv')
    data_calories_income = data_calories_income[data_calories_income['user_id']==user_id]
    logIncomeLabel = {}
    loop_index=0
    for index, income in data_calories_income.iterrows():
        if loop_index < 7:
            logIncomeLabel[loop_index] = ttk.Label(page5['log_exercise'], text=f"{income.date} - {income.time} - {income.food}, {income.drink}: + {income.calories}", style="desc.TLabel")
            logIncomeLabel[loop_index].place(x=50, y=200+loop_index*50)
        else:
            logIncomeLabel[loop_index] = ttk.Label(page5['log_exercise'], text=f"...", style="desc.TLabel")
            logIncomeLabel[loop_index].place(x=50, y=200+loop_index*50)
            break
        loop_index+=1
    
    data_calories_outcome = pd.read_csv('database_log_exercise.csv')
    data_calories_outcome = data_calories_outcome[data_calories_outcome['user_id']==user_id]
    
    logOutcomeLabel = {}
    loop_index = 0
    for index, outcome in data_calories_outcome.iterrows():
        if loop_index < 7:
            logOutcomeLabel[loop_index] = ttk.Label(page5['log_exercise'], text=f"{outcome.date} - {outcome.time} - {outcome.name_exercise}: - {outcome.calories}", style="desc.TLabel")
            logOutcomeLabel[loop_index].place(x=775, y=200+loop_index*50)
        else:
            logOutcomeLabel[loop_index] = ttk.Label(page5['log_exercise'], text=f"...", style="desc.TLabel")
            logOutcomeLabel[loop_index].place(x=775, y=200+loop_index*50)
            break
        loop_index+=1
    
    total_cal = data_calories_income['calories'].sum() - data_calories_outcome['calories'].sum()
    total_cal_label = ttk.Label(page5['log_exercise'], text=f"Total Calories Gained or Burned: {total_cal}", style="desc.TLabel")
    total_cal_label.place(x=500, y=525)
    
    raise_frame(page5['log_exercise'])
    
def main_settings():
    raise_frame(page6['settings'])

#------PAGE 1 Login---------------------

# Create the widgets
width_line = 475
horizontal_line1 = Frame(page1['login'], bg='black', height=1, width=width_line)
horizontal_line2 = Frame(page1['login'], bg='black', height=1, width=width_line)
horizontal_line3 = Frame(page1['login'], bg='black', height=1, width=width_line)

titleLabel = ttk.Label(page1['login'], text='Diet Tracker App', style="title.TLabel")

username = StringVar()
usernameEntry = ttk.Entry(page1['login'], textvariable=username, width=30, font=(font_style,20))
usernameLabel = ttk.Label(page1['login'], text='Username', style="desc.TLabel")

password = StringVar()
passwordEntry = ttk.Entry(page1['login'], textvariable=password, show='*', width=30, font=(font_style,20))
passwordLabel = ttk.Label(page1['login'], text='Password', style="desc.TLabel")
validateLogin = partial(validateLogin, username, password)

page1login_button = ttk.Button(page1['login'], width=30, text='Login', style="ok.TButton", command=validateLogin)
page1create_user = ttk.Button(page1['login'], width=30, text='Create Account', style="ok.TButton", command=lambda:raise_frame(page1['new_user']))

# Place the widgets
page1['login']['padding'] = (50,50)

## initialize place
page1['login'].grid(column=0, row=0, columnspan=3)

titleLabel.grid(column=1,row=0, pady=(0,25))
horizontal_line1.grid(column=0,row=1, pady=(0,100))
horizontal_line2.grid(column=1,row=1, pady=(0,100))
horizontal_line3.grid(column=2,row=1, pady=(0,100))
usernameLabel.grid(column=1, row = 2, pady=(0,25))
usernameEntry.grid(column=1, row = 3, pady=(0,50))
passwordLabel.grid(column=1, row = 4, pady=(0,25))
passwordEntry.grid(column=1, row = 5, pady=(0,200))
page1login_button.grid(column=1, row=6)
page1create_user.grid(column=0, row=6)

#------PAGE 1 Create User---------------------

width_line = 475
new_horizontal_line1 = Frame(page1['new_user'], bg='', height=1, width=width_line)
new_horizontal_line2 = Frame(page1['new_user'], bg='', height=1, width=width_line)
new_horizontal_line3 = Frame(page1['new_user'], bg='', height=1, width=width_line)

new_username = StringVar()
new_usernameEntry = ttk.Entry(page1['new_user'], textvariable=new_username, width=30, font=(font_style,20))
new_usernameLabel = ttk.Label(page1['new_user'], text='New Username', style="desc.TLabel")

new_password = StringVar()
new_passwordEntry = ttk.Entry(page1['new_user'], textvariable=new_password, show='*', width=30, font=(font_style,20))
new_passwordLabel = ttk.Label(page1['new_user'], text='New Password', style="desc.TLabel")
validateReg = partial(register_user, new_username, new_password)

page1new_user_button = ttk.Button(page1['new_user'], width=30, text='Create Account', style="ok.TButton", command=validateReg)

# Place the widgets
page1['new_user']['padding'] = (50,50)

## initialize place
page1['new_user'].grid(column=0, row=0)

new_horizontal_line1.grid(column=0,row=1, pady=(0,100))
new_horizontal_line2.grid(column=1,row=1, pady=(0,100))
new_horizontal_line3.grid(column=2,row=1, pady=(0,100))

new_usernameLabel.grid(column=1, row = 2, pady=(75,25))
new_usernameEntry.grid(column=1, row = 3, pady=(0,50))
new_passwordLabel.grid(column=1, row = 4, pady=(0,25))
new_passwordEntry.grid(column=1, row = 5, pady=(0,200))
page1new_user_button.grid(column=1, row=6)

#------PAGE 2 Main Home---------------------

# Create the widgets
width_line = 285
height_line = 400
main_home_horizontal_line1 = Frame(page2['main_home'], bg='black', height=1, width=width_line)
main_home_horizontal_line2 = Frame(page2['main_home'], bg='black', height=1, width=width_line)
main_home_horizontal_line3 = Frame(page2['main_home'], bg='black', height=1, width=width_line)
main_home_horizontal_line4 = Frame(page2['main_home'], bg='black', height=1, width=width_line)
main_home_horizontal_line5 = Frame(page2['main_home'], bg='black', height=1, width=width_line)
main_home_vertical_line1 = Frame(page2['main_home'], bg='black', height=height_line, width=1)

main_home_image = ttk.Button(page2['main_home'], text='House', image=image['house_select'], command=main_home)
main_home_plate_image = ttk.Button(page2['main_home'], text='Plate', image=image['plate'], command=main_food)
main_home_heart_image = ttk.Button(page2['main_home'], text='Heart', image=image['heart'], command=main_heart)
main_home_log_image = ttk.Button(page2['main_home'], text='Log Book', image=image['log'], command=main_log)
main_home_gear_image = ttk.Button(page2['main_home'], text='Gear', image=image['gear'], command=main_settings)

main_home_dropdown_label = ttk.Label(page2['main_home'], text='Plan Selected', style="desc.TLabel")

page2createplan_button = ttk.Button(page2['main_home'], width=30, text='Create A Plan', style="ok.TButton", command=lambda:raise_frame(page2['create_plan']))
page2calculateBMI_button = ttk.Button(page2['main_home'], width=30, text='Calculate BMI', style="ok.TButton", command=lambda:raise_frame(page2['calculate_bmi']))

# Place the widgets
page2['main_home']['padding'] = (0,0)

# ## initialize place
page2['main_home'].grid(column=0, row=0, columnspan=5)

main_home_horizontal_line1.grid(column=0,row=1, pady=(0,100))
main_home_horizontal_line2.grid(column=1,row=1, pady=(0,100))
main_home_horizontal_line3.grid(column=2,row=1, pady=(0,100))
main_home_horizontal_line4.grid(column=3,row=1, pady=(0,100))
main_home_horizontal_line5.grid(column=4,row=1, pady=(0,100))
main_home_vertical_line1.grid(column=2,row=2, pady=(0,0))

pos_x = 150
main_home_dropdown_label.place(x=pos_x, y=200)
page2createplan_button.place(x=pos_x, y=400)
page2calculateBMI_button.place(x=pos_x, y=450)

main_home_image.grid(column=0, row=5, pady=(25,0))
main_home_plate_image.grid(column=1, row=5, pady=(25,0))
main_home_heart_image.grid(column=2, row=5, pady=(25,0))
main_home_log_image.grid(column=3, row=5, pady=(25,0))
main_home_gear_image.grid(column=4, row=5, pady=(25,0))

#------PAGE 2 Create A Plan---------------------
def create_a_plan(from_cal, to_cal, calories, plan_name):
    date_from = from_cal.get_date()
    date_to = to_cal.get_date()
    data_calories = calories.get()
    
    # database_plan = pd.read_csv('database_plan.csv')
    file = open("database_plan.csv", "a")
    file.write(f"\n{user_id},{plan_name.get()},{date_from},{date_to},{data_calories},0")
    file.close()
    messagebox.showinfo("","Successfully Create A Plan!")

# Create the widgets
width_line = 285
main_home_horizontal_line1 = Frame(page2['create_plan'], bg='black', height=1, width=width_line)
main_home_horizontal_line2 = Frame(page2['create_plan'], bg='black', height=1, width=width_line)
main_home_horizontal_line3 = Frame(page2['create_plan'], bg='black', height=1, width=width_line)
main_home_horizontal_line4 = Frame(page2['create_plan'], bg='black', height=1, width=width_line)
main_home_horizontal_line5 = Frame(page2['create_plan'], bg='black', height=1, width=width_line)
titleLabel = ttk.Label(page2['create_plan'], text='Create A Plan', style="title.TLabel")

plan_name = StringVar()
plan_nameEntry = ttk.Entry(page2['create_plan'], textvariable=plan_name, width=30, font=(font_style,20))
plan_nameLabel = ttk.Label(page2['create_plan'], text='Plan Name', style="desc.TLabel")

create_plan_home_image = ttk.Button(page2['create_plan'], text='House', image=image['house_select'], command=main_home)
create_plan_home_plate_image = ttk.Button(page2['create_plan'], text='Plate', image=image['plate'], command=main_food)
create_plan_home_heart_image = ttk.Button(page2['create_plan'], text='Heart', image=image['heart'], command=main_heart)
create_plan_home_log_image = ttk.Button(page2['create_plan'], text='Log Book', image=image['log'], command=main_log)
create_plan_home_gear_image = ttk.Button(page2['create_plan'], text='Gear', image=image['gear'], command=main_settings)

# Add Calendar
cal_from = Calendar(page2['create_plan'], selectmode = 'day',
               year = 2022, month = 12,
               day = 11)
plan_durationfromLabel = ttk.Label(page2['create_plan'], text='Plan Duration', style="desc.TLabel")
cal_to = Calendar(page2['create_plan'], selectmode = 'day',
               year = 2022, month = 12,
               day = 11)
plan_durationtoLabel = ttk.Label(page2['create_plan'], text='To', style="desc.TLabel")

target_calories = StringVar()
target_caloriesEntry = ttk.Entry(page2['create_plan'], textvariable=target_calories, width=18, font=(font_style,20))
target_caloriesLabel = ttk.Label(page2['create_plan'], text='Target Calories', style="desc.TLabel")

plan_name = StringVar()
plan_nameEntry = ttk.Entry(page2['create_plan'], textvariable=plan_name, width=18, font=(font_style,20))
plan_nameLabel = ttk.Label(page2['create_plan'], text='Plan Name', style="desc.TLabel")
createplan = partial(create_a_plan, cal_from, cal_to, target_calories, plan_name)

page2createplan_button = ttk.Button(page2['create_plan'], width=18, text='Create A Plan', style="ok.TButton", command=createplan)

# Place the widgets
page2['create_plan']['padding'] = (50,50)

## initialize place
page2['create_plan'].grid(column=0, row=0, columnspan=5)

titleLabel.grid(column=2,row=0, pady=(0,25))
main_home_horizontal_line1.grid(column=0,row=1, pady=(0,50))
main_home_horizontal_line2.grid(column=1,row=1, pady=(0,50))
main_home_horizontal_line3.grid(column=2,row=1, pady=(0,50))
main_home_horizontal_line4.grid(column=3,row=1, pady=(0,50))
main_home_horizontal_line5.grid(column=4,row=1, pady=(0,50))

plan_nameLabel.grid(column=1, row=2, pady=(0,25))
plan_nameEntry.grid(column=2, row=2, pady=(0,25))
plan_durationfromLabel.grid(column=1, row=3)
cal_from.grid(column=2, row=3)
cal_to.grid(column=4, row=3)
plan_durationtoLabel.grid(column=3, row=3)
target_caloriesEntry.grid(column=2, row=4, pady=(25,25))
target_caloriesLabel.grid(column=1, row=4, pady=(25,25))
page2createplan_button.grid(column=2, row=5)

create_plan_home_image.grid(column=0, row=6, pady=(25,0))
create_plan_home_plate_image.grid(column=1, row=6, pady=(25,0))
create_plan_home_heart_image.grid(column=2, row=6, pady=(25,0))
create_plan_home_log_image.grid(column=3, row=6, pady=(25,0))
create_plan_home_gear_image.grid(column=4, row=6, pady=(25,0))

#------PAGE 2 Calculate BMi---------------------
def calculate_bmi(age, gender, height, weight):
    bmi = float(weight.get())/(float(height.get())*float(height.get())/10000)
    bmi = round(bmi,2)
    messagebox.showinfo("",f"Your BMI is {bmi}")

# Create the widgets
width_line = 285
main_home_horizontal_line1 = Frame(page2['calculate_bmi'], bg='black', height=1, width=width_line)
main_home_horizontal_line2 = Frame(page2['calculate_bmi'], bg='black', height=1, width=width_line)
main_home_horizontal_line3 = Frame(page2['calculate_bmi'], bg='black', height=1, width=width_line)
main_home_horizontal_line4 = Frame(page2['calculate_bmi'], bg='black', height=1, width=width_line)
main_home_horizontal_line5 = Frame(page2['calculate_bmi'], bg='black', height=1, width=width_line)
titleLabel = ttk.Label(page2['calculate_bmi'], text='Calculate BMI', style="title.TLabel")

age = StringVar()
ageEntry = ttk.Entry(page2['calculate_bmi'], textvariable=age, width=18, font=(font_style,20))
ageLabel = ttk.Label(page2['calculate_bmi'], text='Age', style="desc.TLabel")

bmi_home_dropdown = StringVar()
options_gender = ['Male', 'Female']
bmi_home_dropdown.set(options_gender[0]) # default value
w = OptionMenu(page2['calculate_bmi'], bmi_home_dropdown, *options_gender)
genderLabel = ttk.Label(page2['calculate_bmi'], text='Gender', style="desc.TLabel")

height = StringVar()
heightEntry = ttk.Entry(page2['calculate_bmi'], textvariable=height, width=18, font=(font_style,20))
heightLabel = ttk.Label(page2['calculate_bmi'], text='Height', style="desc.TLabel")

weight = StringVar()
weightEntry = ttk.Entry(page2['calculate_bmi'], textvariable=weight, width=18, font=(font_style,20))
weightLabel = ttk.Label(page2['calculate_bmi'], text='Weight', style="desc.TLabel")

calculatebmi = partial(calculate_bmi, age, bmi_home_dropdown, height, weight)

create_plan_home_image = ttk.Button(page2['calculate_bmi'], text='House', image=image['house_select'], command=main_home)
create_plan_home_plate_image = ttk.Button(page2['calculate_bmi'], text='Plate', image=image['plate'], command=main_food)
create_plan_home_heart_image = ttk.Button(page2['calculate_bmi'], text='Heart', image=image['heart'], command=main_heart)
create_plan_home_log_image = ttk.Button(page2['calculate_bmi'], text='Log Book', image=image['log'], command=main_log)
create_plan_home_gear_image = ttk.Button(page2['calculate_bmi'], text='Gear', image=image['gear'], command=main_settings)

page2calculatebmi_button = ttk.Button(page2['calculate_bmi'], width=18, text='Calculate BMI', style="ok.TButton", command=calculatebmi)

# Place the widgets
page2['calculate_bmi']['padding'] = (50,50)

## initialize place
page2['calculate_bmi'].grid(column=0, row=0, columnspan=5)

titleLabel.grid(column=2,row=0, pady=(0,25))
main_home_horizontal_line1.grid(column=0,row=1, pady=(0,100))
main_home_horizontal_line2.grid(column=1,row=1, pady=(0,100))
main_home_horizontal_line3.grid(column=2,row=1, pady=(0,100))
main_home_horizontal_line4.grid(column=3,row=1, pady=(0,100))
main_home_horizontal_line5.grid(column=4,row=1, pady=(0,100))

ageLabel.grid(column=1, row=2, pady=(0,25))
ageEntry.grid(column=2, row=2, pady=(0,25))
genderLabel.grid(column=1, row=3)
w.grid(column=2, row=3)
heightLabel.grid(column=1, row=4)
heightEntry.grid(column=2, row=4, pady=(25,25))
weightLabel.grid(column=1, row=5, pady=(25,25))
weightEntry.grid(column=2, row=5, pady=(25,25))
page2calculatebmi_button.grid(column=2, row=6)

create_plan_home_image.grid(column=0, row=7, pady=(25,0))
create_plan_home_plate_image.grid(column=1, row=7, pady=(25,0))
create_plan_home_heart_image.grid(column=2, row=7, pady=(25,0))
create_plan_home_log_image.grid(column=3, row=7, pady=(25,0))
create_plan_home_gear_image.grid(column=4, row=7, pady=(25,0))

#------PAGE 3 Main Food---------------------
def add_log(food_name, drink_name, total, cal_date, hour_string, min_string):
    file = open("database_log.csv", "a")
    file.write(f"\n{user_id},{cal_date.get_date()},{hour_string.get()}:{min_string.get()}:00,{food_name},{drink_name},{total}")
    file.close()
    messagebox.showinfo("",f"Data Berhasil Ditambahkan!")
    
def calculate_calories(food_name, drink_name):
    food_name = food_name.get()
    drink_name = drink_name.get()
    data_food = pd.read_csv('database_mst_food.csv')
    data_drink = pd.read_csv('database_mst_drink.csv')
    
    calories_food = data_food[data_food['food_name']==food_name]['amount_calories'].values[0]
    calories_drink = data_drink[data_drink['drink_name']==drink_name]['amount_calories'].values[0]
    
    total = calories_food+calories_drink
    
    caloriesLabel = ttk.Label(page3['calories_home'], text=f'Calories Gained {total}', style="desc.TLabel")
    caloriesLabel.grid(column=4, row=2, padx=(0,0))
    
    addlog = partial(add_log, food_name, drink_name, total, cal_date, hour_string, min_string)
    page3add_log_button = ttk.Button(page3['calories_home'], width=18, text='Add Log', style="ok.TButton", command=addlog)
    page3add_log_button.place(x=1125, y=525)
    
# Create the widgets
width_line = 285
height_line = 400
food_tracker_horizontal_line1 = Frame(page3['calories_home'], bg='black', height=1, width=width_line)
food_tracker_horizontal_line2 = Frame(page3['calories_home'], bg='black', height=1, width=width_line)
food_tracker_horizontal_line3 = Frame(page3['calories_home'], bg='black', height=1, width=width_line)
food_tracker_horizontal_line4 = Frame(page3['calories_home'], bg='black', height=1, width=width_line)
food_tracker_horizontal_line5 = Frame(page3['calories_home'], bg='black', height=1, width=width_line)
food_tracker_vertical_line1 = Frame(page3['calories_home'], bg='black', height=height_line, width=1)

food_tracker_titleLabel = ttk.Label(page3['calories_home'], text=f'Food Tracker', style="title.TLabel")

# Add Calendar
cal_date = Calendar(page3['calories_home'], selectmode = 'day',
               year = 2022, month = 12,
               day = 11)
cal_dateLabel = ttk.Label(page3['calories_home'], text='Select Date & Time', style="desc.TLabel")

hour_string=StringVar()
min_string=StringVar()
min_sb = Spinbox(
    page3['calories_home'],
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=(font_style,20),
    justify=CENTER
    )
sec_hour = Spinbox(
    page3['calories_home'],
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=(font_style,20),
    width=2,
    justify=CENTER
    )

selectFoodLabel = ttk.Label(page3['calories_home'], text='Select Food', style="desc.TLabel")
selectDrinkLabel = ttk.Label(page3['calories_home'], text='Select Drink', style="desc.TLabel")

food_tracker_image = ttk.Button(page3['calories_home'], text='House', image=image['house'], command=main_home)
food_tracker_plate_image = ttk.Button(page3['calories_home'], text='Plate', image=image['plate_select'], command=main_food)
food_tracker_heart_image = ttk.Button(page3['calories_home'], text='Heart', image=image['heart'], command=main_heart)
food_tracker_log_image = ttk.Button(page3['calories_home'], text='Log Book', image=image['log'], command=main_log)
food_tracker_gear_image = ttk.Button(page3['calories_home'], text='Gear', image=image['gear'], command=main_settings)

# Place the widgets
page3['calories_home']['padding'] = (0,0)

# ## initialize place
page3['calories_home'].grid(column=0, row=0, columnspan=5)

food_tracker_horizontal_line1.grid(column=0,row=1, pady=(0,50))
food_tracker_horizontal_line2.grid(column=1,row=1, pady=(0,50))
food_tracker_horizontal_line3.grid(column=2,row=1, pady=(0,50))
food_tracker_horizontal_line4.grid(column=3,row=1, pady=(0,50))
food_tracker_horizontal_line5.grid(column=4,row=1, pady=(0,50))
food_tracker_vertical_line1.grid(column=3,row=2, pady=(0,0))
food_tracker_titleLabel.grid(column=2,row=0, pady=(0,25))

pos_x = 100
cal_dateLabel.place(x=pos_x, y = 175)
cal_date.place(x=pos_x+300, y = 125)
selectFoodLabel.place(x=pos_x, y=350)
selectDrinkLabel.place(x=pos_x, y=400)
min_sb.place(x=pos_x+600, y = 125)
sec_hour.place(x=pos_x+650, y = 125)
# selectFoodLabel.grid(column=0,row=3, pady=(0,25))
# selectDrinkLabel.grid(column=0,row=4, pady=(0,25))

food_tracker_image.grid(column=0, row=6, pady=(30,0))
food_tracker_plate_image.grid(column=1, row=6, pady=(30,0))
food_tracker_heart_image.grid(column=2, row=6, pady=(30,0))
food_tracker_log_image.grid(column=3, row=6, pady=(30,0))
food_tracker_gear_image.grid(column=4, row=6, pady=(30,0))

#------PAGE 4 Main Exercise---------------------
def add_log_exercise(exerciseName, totalCalories, cal_date, hour_string, min_string):
    file = open("database_log_exercise.csv", "a")
    file.write(f"\n{user_id},{cal_date.get_date()},{hour_string.get()}:{min_string.get()}:00,{exerciseName.get()},{totalCalories.get()}")
    file.close()
    messagebox.showinfo("",f"Data Berhasil Ditambahkan!")

# Create the widgets
width_line = 285
exercise_horizontal_line1 = Frame(page4['exercise'], bg='black', height=1, width=width_line)
exercise_horizontal_line2 = Frame(page4['exercise'], bg='black', height=1, width=width_line)
exercise_horizontal_line3 = Frame(page4['exercise'], bg='black', height=1, width=width_line)
exercise_horizontal_line4 = Frame(page4['exercise'], bg='black', height=1, width=width_line)
exercise_horizontal_line5 = Frame(page4['exercise'], bg='black', height=1, width=width_line)

exercise_titleLabel = ttk.Label(page4['exercise'], text=f'Exercise Record', style="title.TLabel")

# Add Calendar
cal_date_exercise = Calendar(page4['exercise'], selectmode = 'day',
               year = 2022, month = 12,
               day = 11)
cal_dateLabel_exercise = ttk.Label(page4['exercise'], text='Select Date & Time', style="desc.TLabel")

hour_exercise_string=StringVar()
min_exercise_string=StringVar()
min_exercise_sb = Spinbox(
    page4['exercise'],
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_exercise_string,
    width=2,
    state="readonly",
    font=(font_style,20),
    justify=CENTER
    )
sec_exercise_hour = Spinbox(
    page4['exercise'],
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_exercise_string,
    font=(font_style,20),
    width=2,
    justify=CENTER
    )

exerciseName = StringVar()
exerciseNameEntry = ttk.Entry(page4['exercise'], textvariable=exerciseName, width=18, font=(font_style,20))
exerciseNameLabel = ttk.Label(page4['exercise'], text='Exercise Name', style="desc.TLabel")

totalCalories = StringVar()
totalCaloriesEntry = ttk.Entry(page4['exercise'], textvariable=totalCalories, width=18, font=(font_style,20))
totalCaloriesLabel = ttk.Label(page4['exercise'], text='Total Calories', style="desc.TLabel")

addlog_exercise = partial(add_log_exercise, exerciseName, totalCalories, cal_date_exercise, hour_exercise_string, min_exercise_string)
page4add_log_button = ttk.Button(page4['exercise'], width=18, text='Add Log', style="ok.TButton", command=addlog_exercise)

exercise_image = ttk.Button(page4['exercise'], text='House', image=image['house'], command=main_home)
exercise_plate_image = ttk.Button(page4['exercise'], text='Plate', image=image['plate'], command=main_food)
exercise_heart_image = ttk.Button(page4['exercise'], text='Heart', image=image['heart_select'], command=main_heart)
exercise_log_image = ttk.Button(page4['exercise'], text='Log Book', image=image['log'], command=main_log)
exercise_gear_image = ttk.Button(page4['exercise'], text='Gear', image=image['gear'], command=main_settings)

# Place the widgets
page4['exercise']['padding'] = (0,0)

# ## initialize place
page4['exercise'].grid(column=0, row=0, columnspan=5)

exercise_horizontal_line1.grid(column=0,row=1, pady=(0,100))
exercise_horizontal_line2.grid(column=1,row=1, pady=(0,100))
exercise_horizontal_line3.grid(column=2,row=1, pady=(0,100))
exercise_horizontal_line4.grid(column=3,row=1, pady=(0,100))
exercise_horizontal_line5.grid(column=4,row=1, pady=(0,100))
exercise_titleLabel.grid(column=2,row=0, pady=(0,25))

# pos_x = 100
# cal_dateLabel_exercise.place(x=pos_x, y = 175)
# cal_date_exercise.place(x=pos_x+300, y = 125)
# exerciseNameLabel.place(x=pos_x, y=350)
# exerciseNameEntry.place(x=pos_x+300, y=350)
# totalCaloriesLabel.place(x=pos_x, y=400)
# totalCaloriesEntry.place(x=pos_x+300, y=400)
# page4add_log_button.place(x=1125, y=525)

pos_x = 100
cal_dateLabel_exercise.grid(column=1, row=2, pady=(0,25))
cal_date_exercise.grid(column=2, row=2, pady=(0,25))
min_exercise_sb.grid(column=3, row=2, pady=(0,25), padx=(0,25))
sec_exercise_hour.grid(column=3, row=2, pady=(0,25), padx=(100,0))
exerciseNameLabel.grid(column=1, row=3, pady=(0,25))
exerciseNameEntry.grid(column=2, row=3, pady=(0,25))
totalCaloriesLabel.grid(column=1, row=4, pady=(0,25))
totalCaloriesEntry.grid(column=2, row=4, pady=(0,25))
page4add_log_button.grid(column=2, row=5, pady=(0,25))

exercise_image.grid(column=0, row=6, pady=(25,0))
exercise_plate_image.grid(column=1, row=6, pady=(25,0))
exercise_heart_image.grid(column=2, row=6, pady=(25,0))
exercise_log_image.grid(column=3, row=6, pady=(25,0))
exercise_gear_image.grid(column=4, row=6, pady=(25,0))

#------PAGE 5 Main Log---------------------

# Create the widgets
width_line = 285
height_line = 375
log_horizontal_line1 = Frame(page5['log_exercise'], bg='black', height=1, width=width_line)
log_horizontal_line2 = Frame(page5['log_exercise'], bg='black', height=1, width=width_line)
log_horizontal_line3 = Frame(page5['log_exercise'], bg='black', height=1, width=width_line)
log_horizontal_line4 = Frame(page5['log_exercise'], bg='black', height=1, width=width_line)
log_horizontal_line5 = Frame(page5['log_exercise'], bg='black', height=1, width=width_line)
log_vertical_line1 = Frame(page5['log_exercise'], bg='black', height=height_line, width=1)

log_titleLabel = ttk.Label(page5['log_exercise'], text=f'Log Record', style="title.TLabel")
incomeNameLabel = ttk.Label(page5['log_exercise'], text='Consumed', style="desc.TLabel")
lossNameLabel = ttk.Label(page5['log_exercise'], text='Loss', style="desc.TLabel")

# totalCalories = StringVar()
# totalCaloriesEntry = ttk.Entry(page5['log_exercise'], textvariable=totalCalories, width=18, font=(font_style,20))
# totalCaloriesLabel = ttk.Label(page5['log_exercise'], text='Total Calories', style="desc.TLabel")

log_image = ttk.Button(page5['log_exercise'], text='House', image=image['house'], command=main_home)
log_plate_image = ttk.Button(page5['log_exercise'], text='Plate', image=image['plate'], command=main_food)
log_heart_image = ttk.Button(page5['log_exercise'], text='Heart', image=image['heart'], command=main_heart)
log_log_image = ttk.Button(page5['log_exercise'], text='Log Book', image=image['log_select'], command=main_log)
log_gear_image = ttk.Button(page5['log_exercise'], text='Gear', image=image['gear'], command=main_settings)

# Place the widgets
page5['log_exercise']['padding'] = (0,0)

# ## initialize place
page5['log_exercise'].grid(column=0, row=0, columnspan=5)

log_horizontal_line1.grid(column=0,row=1, pady=(0,100))
log_horizontal_line2.grid(column=1,row=1, pady=(0,100))
log_horizontal_line3.grid(column=2,row=1, pady=(0,100))
log_horizontal_line4.grid(column=3,row=1, pady=(0,100))
log_horizontal_line5.grid(column=4,row=1, pady=(0,100))
log_vertical_line1.grid(column=2, row = 2, pady=(0,25))
log_titleLabel.grid(column=2,row=0, pady=(0,25))
incomeNameLabel.grid(column=1, row=1,padx=(0,110), pady=(25,0))
lossNameLabel.grid(column=3, row=1,padx=(110,0), pady=(25,0))

log_image.grid(column=0, row=6, pady=(25,0))
log_plate_image.grid(column=1, row=6, pady=(25,0))
log_heart_image.grid(column=2, row=6, pady=(25,0))
log_log_image.grid(column=3, row=6, pady=(25,0))
log_gear_image.grid(column=4, row=6, pady=(25,0))

#------PAGE 6 Main Settings---------------------
def apply_settings(username_new, password_new):
    username_new = username_new.get()
    password_new = password_new.get()
    
    database_user = pd.read_csv('database_user.csv')
    database_user.loc[database_user['id']==user_id, 'username'] = username_new
    database_user.loc[database_user['id']==user_id, 'password'] = password_new
    
    database_user.to_csv('database_user.csv', index=False)
    messagebox.showinfo("",f"Settings Applied! Logout to see the changes!")
    
# Create the widgets
width_line = 285
settings_horizontal_line1 = Frame(page6['settings'], bg='black', height=1, width=width_line)
settings_horizontal_line2 = Frame(page6['settings'], bg='black', height=1, width=width_line)
settings_horizontal_line3 = Frame(page6['settings'], bg='black', height=1, width=width_line)
settings_horizontal_line4 = Frame(page6['settings'], bg='black', height=1, width=width_line)
settings_horizontal_line5 = Frame(page6['settings'], bg='black', height=1, width=width_line)

settings_titleLabel = ttk.Label(page6['settings'], text=f'Settings', style="title.TLabel")

changeusername = StringVar()
changeusernameEntry = ttk.Entry(page6['settings'], textvariable=changeusername, width=18, font=(font_style,20))
changeusernameLabel = ttk.Label(page6['settings'], text='New Username', style="desc.TLabel")

changepassword = StringVar()
changepasswordLabel = ttk.Label(page6['settings'], text='New Password', style="desc.TLabel")
changepasswordEntry = ttk.Entry(page6['settings'], textvariable=changepassword, show='*', width=18, font=(font_style,20))

applySettings = partial(apply_settings, changeusername, changepassword)
apply_button = ttk.Button(page6['settings'], text='Apply', style="ok.TButton", width=18, command=applySettings)
style.configure(
    "logout.TLabel", 
    background='red', 
    font=(font_style,20), 
    justify='center',
    anchor='nswe')
style.map('logout.TLabel', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])
logout_button = ttk.Button(page6['settings'], style="logout.TLabel", text='Logout', width=18, command=lambda:raise_frame(page1['login']))

settings_image = ttk.Button(page6['settings'], text='House', image=image['house'], command=main_home)
settings_plate_image = ttk.Button(page6['settings'], text='Plate', image=image['plate'], command=main_food)
settings_heart_image = ttk.Button(page6['settings'], text='Heart', image=image['heart'], command=main_heart)
settings_log_image = ttk.Button(page6['settings'], text='Log Book', image=image['log'], command=main_log)
settings_gear_image = ttk.Button(page6['settings'], text='Gear', image=image['gear_select'], command=main_settings)

# Place the widgets
page6['settings']['padding'] = (25,0)

# ## initialize place
page6['settings'].grid(column=0, row=0, columnspan=5)

settings_horizontal_line1.grid(column=0,row=1, pady=(0,100))
settings_horizontal_line2.grid(column=1,row=1, pady=(0,100))
settings_horizontal_line3.grid(column=2,row=1, pady=(0,100))
settings_horizontal_line4.grid(column=3,row=1, pady=(0,100))
settings_horizontal_line5.grid(column=4,row=1, pady=(0,100))
settings_titleLabel.grid(column=2,row=0, pady=(25,25))

changeusernameLabel.grid(column=1, row=2, pady=(0,25))
changeusernameEntry.grid(column=2, row=2, pady=(0,25))
changepasswordLabel.grid(column=1, row=3, pady=(0,25))
changepasswordEntry.grid(column=2, row=3, pady=(0,25))
apply_button.grid(column=2, row=4, pady=(0,25))
logout_button.grid(column=2, row=5, pady=(100,45))

settings_image.grid(column=0, row=6, pady=(25,0))
settings_plate_image.grid(column=1, row=6, pady=(25,0))
settings_heart_image.grid(column=2, row=6, pady=(25,0))
settings_log_image.grid(column=3, row=6, pady=(25,0))
settings_gear_image.grid(column=4, row=6, pady=(25,0))

# raise_frame(page5['log_exercise'])
raise_frame(page1['login'])
root.mainloop()