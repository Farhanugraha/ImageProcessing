# author @farhan nugraha

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

# function browse
def browseimage():
    global imgs
    file_path = filedialog.askopenfilename()
    imgs = Image.open(file_path)
    render = ImageTk.PhotoImage(imgs)
    image_label.config(image=render)
    image_label.image = render

def rotateimage():
    global imgs
    angle = int(angle_entry.get())
    imgs = imgs.rotate(angle)
    render = ImageTk.PhotoImage(imgs)
    image_label.config(image=render)
    image_label.image = render


root = tk.Tk()
root.title("Image Rotator")

browse_button = tk.Button(text="Browse Image", command=browseimage)
browse_button.pack()

angle_label = tk.Label(text="Set rotation angle:")
angle_label.pack()

angle_entry = tk.Entry()
angle_entry.pack()

rotate_button = tk.Button(text="Rotate Image", command=rotateimage)
rotate_button.pack()


image_label = tk.Label()
image_label.pack()

root.mainloop()
