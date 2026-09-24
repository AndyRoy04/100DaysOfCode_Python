import turtle
from tkinter import filedialog, Button
from PIL import Image, ImageTk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 650

positioning = {
    "1": [-190, -300],
    "2": [190, -300],
    "3": [0, 0]
}

def write_to_screen(watermark, x, y):
    '''Write the state at the specified location to the screen'''
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.color('#D3D3D3')
    name.goto(x, y)
    name.write(watermark, align='center', font=('Arial', 16, 'bold'))

def save_action(resized_img):
    # 4. Ask user WHERE to save the new image
    save_path = filedialog.asksaveasfilename(
        title="Save Resized Image As",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("GIF Image", "*.gif")]
    )
    
    # 5. Save the file if they didn't cancel the dialog
    if save_path:
        resized_img.save(save_path)
        print(f"Image successfully saved to: {save_path}")
    else:
        print("Save operation cancelled.")
        
        

image_path = filedialog.askopenfilename(
    title='Select an image to watermark',
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")]
)

if image_path:
    screen = turtle.Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    pil_image = Image.open(image_path)
    
    resized_img = pil_image.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_img)
    
    canvas = screen.getcanvas()
    canvas.create_image(0, 0, image=tk_image, anchor='center')
    
    canvas.image = tk_image
    
    text_title = "Enter a postion from 1 - 3"
    position = screen.textinput(title=text_title, prompt="Enter a number position for the image\n1 - Bottom Left\n2 - Bottom Right\n3 - Center")

    watermark_title = "Watermark"
    watermark = screen.textinput(title=watermark_title, prompt="Write your Watermark")

    if position not in positioning.keys():
        write_to_screen(watermark, 0, 0)
    else:
        write_to_screen(watermark, positioning[position][0], positioning[position][1])
        
    # clicked_ok = messagebox.askokcancel(
    # title="Watermark Action", 
    # message="Click OK to apply the watermark or Cancel to skip."
    # )
    
    # if clicked_ok:
    #     save_action(resized_img)
    # else:
    #     print("User clicked Cancel. Skipping action.")
    save = Button(text="Save Image", command=lambda: save_action(resized_img))
    save.pack()   
    

else:
    print("No file selected")


turtle.mainloop()