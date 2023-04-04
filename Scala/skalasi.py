# author @farhan
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# skalasi function
def skalasi():
    skala = int(entry.get())
    img = Image.open(filename)
    img = img.resize((int(img.width*skala/100), int(img.height*skala/100)))
    img = ImageTk.PhotoImage(img)
    label_img.configure(image=img)
    label_img.image = img

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", title = "Pilih img", filetypes = (("img Files", "*.jpg;*.jpeg;*.png;*.bmp"), ("Semua Files", "*.*")))
    if filename:
        try:
            img = Image.open(filename)
            img = ImageTk.PhotoImage(img)
            label_img.configure(image=img)
            label_img.image = img
        except:
            messagebox.showerror("Error", "cannot open file")

root = tk.Tk()
root.title("Skalasi img")

frame_img = tk.Frame(root)
frame_img.pack(pady=10)

label_img = tk.Label(frame_img)
label_img.pack()

frame_skala = tk.Frame(root)
frame_skala.pack()

label_skala = tk.Label(frame_skala, text="Skala %")
label_skala.pack(side="left")

entry = tk.Entry(frame_skala, width=10)
entry.pack(side="left")
entry.insert(0, "100")

button_browse = tk.Button(root, text="select image", command=browseFiles)
button_browse.pack(pady=5)

button_skalasi = tk.Button(root, text="Skalasi", command=skalasi)
button_skalasi.pack(pady=5)

root.mainloop()