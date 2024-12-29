import tkinter as tk


# App Window PopUps
def add_entry_win(self):
    self = tk.Toplevel(self)
    self.title("Add Items")
    self.geometry("926x707")
    self.config(bg="#102C57")
    self.resizable(False, False)
    self.grab_set()

    # Frames
    frame = tk.Frame(
        self,
        bg="#EADBC8",
        width=600,
        height=620
        )
    
    frame.place(x=153, y=126)

    # Add a Text widget to the frame
    text_box = tk.Text(frame, height=30, width=80, font=("Arial", 12))
    text_box.pack(padx=10, pady=10)  # Add some padding around the text box

    # Add a button to demonstrate interactivity
    button = tk.Button(frame, text="Print Text", command=lambda: print(text_box.get("1.0", tk.END)))
    button.pack(pady=10)