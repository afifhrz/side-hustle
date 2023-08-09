from tkinter import ttk
def createRoute(root):
    # Define the main window for each page
    frames = {}
    frames['page1'] = {
        'login':ttk.Frame(root),
        'new_user':ttk.Frame(root)
        }

    frames['page2'] = {
        'main_home':ttk.Frame(root),
        'create_plan':ttk.Frame(root),
        'calculate_bmi':ttk.Frame(root)
        }

    frames['page3'] = {
        'calories_home':ttk.Frame(root),
        'create_food':ttk.Frame(root),
        'create_drink':ttk.Frame(root),
    }

    frames['page4'] = {
        'exercise':ttk.Frame(root),
    }

    frames['page5'] = {
        'log_exercise':ttk.Frame(root),
    }

    frames['page6'] = {
        'settings':ttk.Frame(root),
    }
    return frames