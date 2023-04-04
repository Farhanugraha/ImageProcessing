# author @farhan nugraha
import tkinter as tk
import PIL
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    global original_image
    file_path = filedialog.askopenfilename()
    original_image = Image.open(file_path)
    display_image(original_image)

def flip_horizontally():
    global original_image, processed_image
    processed_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    display_image(processed_image)

def flip_vertically():
    global original_image, processed_image
    processed_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)
    display_image(processed_image)

def display_image(img):
    global image_label
    image = ImageTk.PhotoImage(img)
    image_label.config(image=image)
    image_label.image = image

root = tk.Tk()
root.title("Flipping Image")

original_image = None
processed_image = None

open_image_button = tk.Button(root, text="Open Image", command=open_image)
open_image_button.pack(pady=10)

flip_horizontally_button = tk.Button(root, text="Flip Horizontally", command=flip_horizontally)
flip_horizontally_button.pack(pady=10)

flip_vertically_button = tk.Button(root, text="Flip Vertically", command=flip_vertically)
flip_vertically_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()
