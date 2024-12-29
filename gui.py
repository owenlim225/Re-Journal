from pathlib import Path
from datetime import datetime, timedelta
from tkinter import Canvas, Button, PhotoImage, messagebox
import tkinter as tk


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Path directory to access assets
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets"

        # Initialize window
        self.geometry("926x707")
        self.configure(bg="#F0F0F0")
        self.title("Re-Journal")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.exit_confirmation)

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width, window_height = 926, 707
        x_offset = (screen_width - window_width) // 2
        y_offset = (screen_height - window_height) // 3

        self.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

        # Initialize canvas
        self.initialize_canvas()

    def exit_confirmation(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.destroy()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def initialize_canvas(self):
        self.canvas = Canvas(
            self,
            bg="#F0F0F0",
            height=707,
            width=926,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        # Main background image
        self.bg_img = PhotoImage(file=self.relative_to_assets("bg_img.png"))
        self.canvas.create_image(463.0, 364.0, image=self.bg_img)

        # Top frame image
        self.top_frame_img = PhotoImage(file=self.relative_to_assets("top_frame_img.png"))
        self.canvas.create_image(465.0, 51.33, image=self.top_frame_img)

        # Date Label
        self.current_date = tk.StringVar()
        self.current_date.set(datetime.now().strftime("%B %d, %Y"))

        self.lbl_date = tk.Label(
            self.canvas,
            textvariable=self.current_date,
            font=("katibeh", 25, "bold"),
            fg="#1E1F1E",
            bg="#F0F0F0",
        )
        self.lbl_date.place(x=310.0, y=25.0, anchor="nw")

        # Date forward button
        self.btn_date_forward_img = PhotoImage(
            file=self.relative_to_assets("btn_date_forward.png")
        )
        self.btn_date_forward = Button(
            image=self.btn_date_forward_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_date_forward,
            relief="flat",
            cursor="hand2",
        )
        self.btn_date_forward.place(x=642.0, y=13.0, width=50.0, height=65.0)

        # Date backward button
        self.btn_date_backward_img = PhotoImage(
            file=self.relative_to_assets("btn_date_backward.png")
        )
        self.btn_date_backward = Button(
            image=self.btn_date_backward_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_date_backward,
            relief="flat",
            cursor="hand2",
        )
        self.btn_date_backward.place(x=238.0, y=13.0, width=50.0, height=65.0)

        # Buttons for actions
        self.create_buttons()

    def create_buttons(self):
        self.btn_past_img = PhotoImage(file=self.relative_to_assets("btn_past.png"))
        self.btn_past = Button(
            image=self.btn_past_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_past,
            relief="flat",
            cursor="hand2",
        )
        self.btn_past.place(x=795.0, y=14.0, width=100.78, height=76.0)

        self.btn_date_img = PhotoImage(file=self.relative_to_assets("btn_date.png"))
        self.btn_date = Button(
            image=self.btn_date_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_date,
            relief="flat",
            cursor="hand2",
        )
        self.btn_date.place(x=43.0, y=115.0, width=100.0, height=100.0)

        self.btn_search_img = PhotoImage(file=self.relative_to_assets("btn_search.png"))
        self.btn_search = Button(
            image=self.btn_search_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_search,
            relief="flat",
            cursor="hand2",
        )
        self.btn_search.place(x=43.0, y=235.0, width=100.0, height=100.0)

        self.btn_write_img = PhotoImage(file=self.relative_to_assets("btn_write.png"))
        self.btn_write = Button(
            image=self.btn_write_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_write,
            relief="flat",
            cursor="hand2",
        )
        self.btn_write.place(x=43.0, y=355.0, width=100.0, height=100.0)

        self.btn_location_img = PhotoImage(
            file=self.relative_to_assets("btn_location.png")
        )
        self.btn_location = Button(
            image=self.btn_location_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_location,
            relief="flat",
            cursor="hand2",
        )
        self.btn_location.place(x=43.0, y=475.0, width=100.0, height=100.0)

        self.btn_export_img = PhotoImage(file=self.relative_to_assets("btn_export.png"))
        self.btn_export = Button(
            image=self.btn_export_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.command_btn_export,
            relief="flat",
            cursor="hand2",
        )
        self.btn_export.place(x=43.0, y=595.0, width=100.0, height=100.0)

    def command_btn_date(self):
        print("btn_date clicked")

    def command_btn_search(self):
        print("btn_search clicked")

    def command_btn_write(self):
        print("btn_write clicked")

    def command_btn_location(self):
        print("btn_location clicked")

    def command_btn_export(self):
        print("btn_export clicked")

    def command_btn_past(self):
        print("btn_past clicked")

    def command_btn_date_forward(self):
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current + timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))

    def command_btn_date_backward(self):
        current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
        new_date = current - timedelta(days=1)
        self.current_date.set(new_date.strftime("%B %d, %Y"))


# Start the program
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
