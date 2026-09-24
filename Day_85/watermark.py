import turtle
from tkinter import filedialog, Button
from PIL import Image, ImageTk, ImageDraw, ImageFont

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 650

positioning = {
    "1": (40, WINDOW_HEIGHT - 60),    # Bottom Left
    "2": (WINDOW_WIDTH - 110, WINDOW_HEIGHT - 60),  # Bottom Right
    "3": (WINDOW_WIDTH // 2 - 20, WINDOW_HEIGHT // 2)  # Center
}

def draw_watermark_on_image(pil_img, watermark, position_key):
    """Draw watermark text directly onto the PIL image."""
    img_copy = pil_img.copy()  # Working on a copy so original stays clean
    draw = ImageDraw.Draw(img_copy)

    # Try catch
    try:
        font = ImageFont.truetype("arial.ttf", 25)
    except IOError:
        font = ImageFont.load_default()

    x, y = positioning.get(position_key, (WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT // 2))

    # Draw the watermark text with a light gray color
    draw.text((x, y), watermark, fill=(211, 211, 211, 180), font=font)

    return img_copy  # Return the watermarked image

def update_canvas(watermarked_pil_img):
    """Refresh the turtle canvas to show the watermarked image."""
    global tk_image
    tk_image = ImageTk.PhotoImage(watermarked_pil_img)
    canvas.create_image(0, 0, image=tk_image, anchor='center')
    canvas.image = tk_image

def save_action():
    save_path = filedialog.asksaveasfilename(
        title="Save Watermarked Image As",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("GIF Image", "*.gif")]
    )
    if save_path:
        watermarked_img.save(save_path)
        print(f"Image successfully saved to: {save_path}")
    else:
        print("Save operation cancelled.")

# ── Main flow ──

image_path = filedialog.askopenfilename(
    title='Select an image to watermark',
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")]
)

if image_path:
    screen = turtle.Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

    pil_image = Image.open(image_path).convert("RGBA")
    resized_img = pil_image.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.Resampling.LANCZOS)

    # Display the original image first
    tk_image = ImageTk.PhotoImage(resized_img)
    canvas = screen.getcanvas()
    canvas.create_image(0, 0, image=tk_image, anchor='center')
    canvas.image = tk_image

    # Get user inputs
    position = screen.textinput(
        title="Choose Position",
        prompt="Enter a number position for the watermark:\n1 - Bottom Left\n2 - Bottom Right\n3 - Center"
    )
    watermark = screen.textinput(title="Watermark", prompt="Write your Watermark text:")

    if watermark:
        watermarked_img = draw_watermark_on_image(resized_img, watermark, position) # Draw watermark on image
        update_canvas(watermarked_img)
    else:
        watermarked_img = resized_img  # No watermark entered, save clean image

    save = Button(text="Save Image", command=save_action) # Save button
    save.pack()

else:
    print("No file selected.")

turtle.mainloop()