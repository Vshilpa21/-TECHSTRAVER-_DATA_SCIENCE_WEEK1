import tkinter as tk
from tkinter import messagebox, filedialog
import pyqrcode
import io
from PIL import Image, ImageTk

# Function to generate the QR code
def generate_qr():
    text = input_entry.get()
    if not text:
        result_label.config(text="Please enter text or URL.")
        return

    # Generate QR code
    qr = pyqrcode.create(text)

    # Create an in-memory image
    buffer = io.BytesIO()
    qr.png(buffer, scale=6)
    buffer.seek(0)

    # Display the QR code in the GUI
    qr_image = Image.open(buffer)
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    # Enable the save button
    save_button.config(state=tk.NORMAL)

    result_label.config(text="QR Code Generated. You can now save it.")

# Function to save the QR code as a PNG file
def save_qr():
    text = input_entry.get()
    if not text:
        result_label.config(text="Please generate the QR code first.")
        return

    # Ask the user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save QR Code")
    if file_path:
        # Generate and save the QR code
        qr = pyqrcode.create(text)
        qr.png(file_path, scale=6)
        result_label.config(text=f"QR Code saved at: {file_path}")
    else:
        result_label.config(text="Save operation canceled.")

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("400x500")  # Set window size

# Create and configure widgets
input_label = tk.Label(window, text="Enter URL or Text:")
input_entry = tk.Entry(window, width=40)
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr)
save_button = tk.Button(window, text="Save QR Code", command=save_qr, state=tk.DISABLED)  # Initially disabled
qr_label = tk.Label(window)  # Label to display the QR code
result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=300)

# Place widgets in the window
input_label.pack(pady=10)
input_entry.pack(pady=5)
generate_button.pack(pady=10)
qr_label.pack(pady=10)
save_button.pack(pady=10)
result_label.pack(pady=20)

# Start the Tkinter main loop
window.mainloop()
