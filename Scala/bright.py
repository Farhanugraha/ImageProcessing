# author @farhan nugraha

import cv2 as cv
import tkinter as tk
import numpy as np
import tkinter.filedialog as fd

class bright:
    
    def __init__(self, master):
        self.master = master
        self.master.title('Brightnes')

        self.image = None
        self.bright_value = tk.IntVar(value=0)

        self.open_button = tk.Button(self.master, text='Open', command=self.open_image)
        self.open_button.pack(side='left')

        self.bright_scale = tk.Scale(self.master, from_=-255, to=255, orient='horizontal', variable=self.bright_value, label='Brightness')
        self.bright_scale.pack(side='left')

        self.status = tk.Label(self.master, text='Image: None')
        self.status.pack(side='right')

    def open_image(self):
        file_path = fd.askopenfilename(filetypes=[('Image files', '*.jpg;*.jpeg;*.png;*.bmp')])
        if file_path:
            self.image = cv.imread(file_path)
            self.status.config(text=f'Image: {file_path}')
            self.update_image()

    def update_image(self):
        if self.image is not None:
            bright_value = self.bright_value.get()
            self.image = np.clip(self.image + bright_value, 0, 255).astype('uint8')
            cv.imshow('Image', self.image)

if __name__ == '__main__':
    window = tk.Tk()
    app = bright(window)
    
    # main loop
    window.mainloop()
