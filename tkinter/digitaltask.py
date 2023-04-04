import cv2 as cv
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


filepath = 'data//lenna.jpg'
contimage = cv.imread(filepath,cv.IMREAD_COLOR)


window = tk.Tk()
window.geometry("400x200")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill='x',expand=True)

# BUTTON
originalPic = tk.StringVar()
# VARIABL
   
    

button_comp = ttk.Button(input_frame,text="Original Lenna",command=click_button)
button_comp.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()
