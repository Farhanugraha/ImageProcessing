import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter

# @author Farhan Nugraha
# image convolution with OOP and GUI tkinter

class Convolution:
    def __init__(self, master):
        self.master = master
        self.master.title("Convolution")
        
        self.browse_button = tk.Button(self.master, text="Search Image", command=self.load)
        self.browse_button.pack()
        
        self.sharpening_button = tk.Button(self.master, text="Sharpening", command=self.sharpening)
        self.sharpening_button.pack()
        
        self.deblurring_button = tk.Button(self.master, text="Deblurring", command=self.deblurring)
        self.deblurring_button.pack()
        
        self.soft_edge_detection_button = tk.Button(self.master, text="Soft Edge Detection", command=self.soft_edge_detection)
        self.soft_edge_detection_button.pack()
        
    def load(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path).convert("L")
        
    def sharpening(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.image.show()
        
    def deblurring(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.image.show()
        
    def soft_edge_detection(self):
        self.image = self.image.filter(ImageFilter.FIND_EDGES)
        self.image.show()
        
        # main class to execute the program
if __name__ == "__main__":
    window = tk.Tk()
    app = Convolution(window)
    window.mainloop()
