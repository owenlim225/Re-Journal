from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

# Paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documents\GitHub\Re-Journal\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Initialize window
window = Tk()
window.geometry("926x707")
window.configure(bg="#FFFFFF")

# Center the window on the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width, window_height = 926, 707
x_offset = (screen_width - window_width) // 2
y_offset = (screen_height - window_height) // 3
window.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

# Create canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=707,
    width=926,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

# Add images and buttons
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(463.0, 364.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(465.0, 51.33, image=image_image_2)

button_data = [
    ("button_1.png", 43.0, 115.0, 100.0, 100.0, lambda: print("button_1 clicked")),
    ("button_2.png", 43.0, 235.0, 100.0, 100.0, lambda: print("button_2 clicked")),
    ("button_3.png", 43.0, 355.0, 100.0, 100.0, lambda: print("button_3 clicked")),
    ("button_4.png", 43.0, 475.0, 100.0, 100.0, lambda: print("button_4 clicked")),
    ("button_5.png", 43.0, 595.0, 100.0, 100.0, lambda: print("button_5 clicked")),
    ("button_6.png", 795.0, 14.0, 100.78, 76.0, lambda: print("button_6 clicked")),
    ("button_7.png", 642.0, 13.0, 50.0, 65.0, lambda: print("button_7 clicked")),
    ("button_8.png", 238.0, 15.0, 50.0, 65.0, lambda: print("button_8 clicked")),
]

for image, x, y, w, h, command in button_data:
    button_image = PhotoImage(file=relative_to_assets(image))
    button = Button(
        image=button_image,
        borderwidth=0,
        highlightthickness=0,
        command=command,
        relief="flat",
    )
    button.image = button_image  # Prevent garbage collection
    button.place(x=x, y=y, width=w, height=h)

# Add text
canvas.create_text(
    288.0,
    28.0,
    anchor="nw",
    text="DECEMBER 30, 2024",
    fill="#202020",
    font=("Katibeh Regular", -40),
)

# Prevent resizing
window.resizable(False, False)
window.mainloop()
