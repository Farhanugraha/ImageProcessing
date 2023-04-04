import cv2 as cv
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


pathfile = 'data//lenna.jpg'
contimage = cv.imread(pathfile,cv.IMREAD_COLOR)

window = tk.Tk()
window.configure(bg="white")
window.geometry("800x500")
window.resizable(False,False)
window.title("Digital Image Processing")
#  VARIABLE
FIRST_NAME = tk.StringVar()
LAST_NAME = tk.StringVar()

# COMPONENT
input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill='x',expand=True)

frame_contentlabel = ttk.Label(input_frame,text="First Name :")
frame_contentlabel.pack(padx=10,fill='x',expand=True)

frame_contententry = ttk.Entry(input_frame,textvariable=FIRST_NAME)
frame_contententry.pack(padx=10,fill='x',expand=True)

frame_contentlabel = ttk.Label(input_frame,text="Last Name :")
frame_contentlabel.pack(padx=10,fill='x',expand=True)

frame_contententry = ttk.Entry(input_frame,textvariable=LAST_NAME)
frame_contententry.pack(padx=10,fill='x',expand=True)



# BUTTON
def click_button():
#   print(LAST_NAME.get())
  messages = f"haloo {FIRST_NAME.get()} {LAST_NAME.get()} gantengg"
  showinfo(message=messages)

button_comp = ttk.Button(input_frame,text="input",command=click_button)
button_comp.pack(fill='x',expand=True,padx=10,pady=10)

# Main loop window

window.mainloop()