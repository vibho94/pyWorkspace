"""
Essentials method and libraries are as follows:-PIL(Python Imaging library) ,TKINTER(GUI Library which helps in creating windows ,labels ,button etc.)
ITERTOOLS(Build in Module which iterate build in Modules like list or tuples),
cycle() :- use to iterate loop infinite times,sleep() :- which allows the image to stop for few seconds

"""


from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk

#Create window for slideshow

root=tk.Tk()
#set the slideshow title
root.title("Image slideshow viewer")
#list of image path
image_paths=[
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download (1).jpg",
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download (2).jpg",
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download (3).jpg",
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download.jpg"
]

#resize the image in 1080*1080

image_size=(1080,1080)
Resized_Image=[Image.open(path).resize(image_size) for path in image_paths]

#Explain:- from PIL import Image

#image_paths = ['img1.jpg', 'img2.jpg', 'img3.jpg']
#image_size = (224, 224)

#images = [Image.open(path).resize(image_size) for path in image_paths]

photo_images=[ImageTk.PhotoImage(image) for image in Resized_Image]

#create the label which help in displaying the text and image in the root window

label=tk.Label(root)
label.pack()


def image_update():
    for photo_image in photo_images:
        label.configure(image=photo_image)
        label.update()
        #time.sleep(3)
        root.after(10,update_image)

#repeat the images as slideshow

slideshow=cycle(photo_images)


def update_image():
    pass


def start_slideshow(image_path=None):
    for _ in range(len(image_paths)):
        update_image()

play_button=tk.Button(root,text="Play slideshow",command=start_slideshow)
play_button.pack()

root.mainloop()




