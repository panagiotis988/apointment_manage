from PIL import ImageTk, Image
import tkinter as tk


class ImageHandler:

    @staticmethod
    def open_image():
        global image
        global label

        images = ImageTk.PhotoImage(Image.open("image.png"))
        label = tk.Label(image=images)

        label.image = images
        label.place(x=1000, y=100)

    @staticmethod
    def close_image():
        label.destroy()