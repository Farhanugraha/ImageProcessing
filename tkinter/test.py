import tkinter as tk
import tkinter.filedialog as fd
import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, master):
        self.master = master
        self.master.title('Image Processor')

        self.image = None

        self.bright_value = tk.IntVar(value=0)
        self.threshold_value = tk.IntVar(value=128)
        self.scale_width = tk.IntVar(value=0)
        self.scale_height = tk.IntVar(value=0)
        self.rotate_angle = tk.IntVar(value=0)

        self.open_button = tk.Button(self.master, text='Open', command=self.open_image)
        self.open_button.pack(side='left')

        self.save_button = tk.Button(self.master, text='Save', command=self.save_image)
        self.save_button.pack(side='left')

        self.bright_scale = tk.Scale(self.master, from_=-255, to=255, orient='horizontal', variable=self.bright_value, label='Brightness')
        self.bright_scale.pack(side='left')

        self.threshold_scale = tk.Scale(self.master, from_=0, to=255, orient='horizontal', variable=self.threshold_value, label='Threshold')
        self.threshold_scale.pack(side='left')

        self.scale_width_entry = tk.Entry(self.master, textvariable=self.scale_width)
        self.scale_width_entry.pack(side='left')

        self.scale_height_entry = tk.Entry(self.master, textvariable=self.scale_height)
        self.scale_height_entry.pack(side='left')

        self.rotate_entry = tk.Entry(self.master, textvariable=self.rotate_angle)
        self.rotate_entry.pack(side='left')

        self.flip_x_button = tk.Button(self.master, text='Flip X', command=lambda: self.flip_image(0))
        self.flip_x_button.pack(side='left')

        self.flip_y_button = tk.Button(self.master, text='Flip Y', command=lambda: self.flip_image(1))
        self.flip_y_button.pack(side='left')

        self.status = tk.Label(self.master, text='Image: None')
        self.status.pack(side='right')

    def open_image(self):
        file_path = fd.askopenfilename(filetypes=[('lenna.jpg', '*.jpg;*.jpeg;*.png;*.bmp')])
        if file_path:
            self.image = cv2.imread(file_path)
            self.status.config(text=file_path)
