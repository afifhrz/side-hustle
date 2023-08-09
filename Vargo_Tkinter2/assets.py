from PIL import Image, ImageTk
def load_image():
    image = {}
    data_image = [
        'house',
        'house_select',
        'plate',
        'plate_select',
        'heart',
        'heart_select',
        'log',
        'log_select',
        'gear',
        'gear_select',
        'down'
    ]
    for key in data_image:
        # open image
        image[key] = ImageTk.PhotoImage(Image.open('image\\'+key+'.png').resize((200,150)))
    return image