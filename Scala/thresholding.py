# author @farhan nugraha

import tkinter as tk
import cv2
import numpy as np
import tkinter.filedialog as fd


class thresholdings:
    
    def __init__(self, master):
        self.master = master
        self.master.title('Thresholding')
        

        self.image = None
        self.threshold_value = tk.IntVar(value=128)

        self.open_button = tk.Button(self.master, text='Open', command=self.open_image)
        self.open_button.pack(side='left')

        self.threshold_scale = tk.Scale(self.master, from_=0, to=255, orient='horizontal', variable=self.threshold_value, label='Threshold')
        self.threshold_scale.pack(side='left')

        self.status = tk.Label(self.master, text='Image: None')
        self.status.pack(side='right')

    def open_image(self):
        file_path = fd.askopenfilename(filetypes=[('Image files', '*.jpg;*.jpeg;*.png;*.bmp')])
        if file_path:
            self.image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.status.config(text=f'Image: {file_path}')
            self.update_image()

    def update_image(self):
        if self.image is not None:
            threshold_value = self.threshold_value.get()
            _, self.image = cv2.threshold(self.image, threshold_value, 255, cv2.THRESH_BINARY)
            cv2.imshow('Image', self.image)

if __name__ == '__main__':
    window = tk.Tk()
    app = thresholdings(window)
    window.mainloop()
