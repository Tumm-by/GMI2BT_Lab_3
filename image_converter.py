from PIL import Image, ImageTk

def bytes_to_image(image_data):
    from io import BytesIO
    return ImageTk.PhotoImage(Image.open(BytesIO(image_data)),(300,444))

def default_image():
    return ImageTk.PhotoImage(Image.open("NoThingFound.png"))
