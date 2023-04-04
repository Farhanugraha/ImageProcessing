import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

def brighten(image, value):
    bright_image = cv2.addWeighted(image, 1.0, image, 0, value)
    return bright_image

def binarize(image, threshold):
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

def flip(image, flip_code):
    flip_image = cv2.flip(image, flip_code)
    return flip_image

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

def scale(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized_image = cv2.resize(image, dim, interpolation=inter)
    return resized_image

def open_image():
    global image
    file_path = filedialog.askopenfilename()
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (600, 400))
    photo = tk.PhotoImage(image=image)
    label.config(image=photo)
    label.image = photo

def save_image():
    global output_image
    file_path = filedialog.asksaveasfilename(defaultextension='lenna.jpg')
    output_image = cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, output_image)

def brighten_image():
    global output_image
    value = int(entry_bright.get())
    output_image = brighten(image, value)
    photo = tk.PhotoImage(image=output_image)
    label.config(image=photo)
    label.image = photo

def binarize_image():
    global output_image
    threshold = int(entry_bin.get())
    output_image = binarize(cv2.cvtColor(image, cv2))


