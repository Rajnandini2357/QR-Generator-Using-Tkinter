import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    # Get the text from the entry widget
    data = entry.get()
    
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    # Convert PIL image to Tkinter PhotoImage
    img = ImageTk.PhotoImage(img)
    
    # Update the image on the label
    qr_label.config(image=img)
    qr_label.image = img

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place widgets
entry = tk.Entry(root, font=('Arial', 14))
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run the application
root.mainloop()
