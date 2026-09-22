import turtle
from tkinter import filedialog
from PIL import Image, ImageTk

def write_to_screen(watermark, x, y):
    '''Write the state at the specified location to the screen'''
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.color('#D3D3D3')
    name.goto(x, y)
    name.write(watermark, align='center', font=('Arial', 20, 'bold'))

image_path = filedialog.askopenfilename(
    title='Select an image to watermark',
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")]
)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 650

if image_path:
    screen = turtle.Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    pil_image = Image.open(image_path)
    
    resized_img = pil_image.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_img)
    
    canvas = screen.getcanvas()
    canvas.create_image(0, 0, image=tk_image, anchor='center')
    
    canvas.image = tk_image
else:
    print("No file selected")

# text_title = "Enter a postion from 1 - 3"
# position = screen.textinput(title=text_title, prompt="Enter a number position for the image\n1 - Bottom Left\n2 - Bottom Right\n3 - Center")

watermark_title = "Watermark"
watermark = screen.textinput(title=watermark_title, prompt="Write your Watermark")

write_to_screen(watermark, 190, -300)


turtle.mainloop()