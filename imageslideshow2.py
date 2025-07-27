from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

# Create window for slideshow
root = tk.Tk()
root.title("Image slideshow viewer")

# List of image paths
image_paths = [
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download (1).jpg",
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download (2).jpg",
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download (3).jpg",
    r"C:\Users\vibhor.singhal\PycharmProjects\pyWorkspace\Image viewer\download.jpg"
]

# Resize the images
image_size = (720, 720)
resized_images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in resized_images]

# Cycle through images
slideshow = cycle(photo_images)

# Label to display images
label = tk.Label(root)
label.pack()

def update_image():
    # Get the next image from the cycle and update the label
    next_image = next(slideshow)
    label.config(image=next_image)
    label.image = next_image  # prevent garbage collection
    root.after(3000, update_image)  # update every 3 seconds

def start_slideshow():
    update_image()

# Play button to start slideshow
play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
