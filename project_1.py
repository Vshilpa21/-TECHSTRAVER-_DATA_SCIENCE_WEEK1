import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length_str = length_entry.get()

    # Validate that the input is not empty and consists of digits
    if not password_length_str.isdigit():
        result_label.config(text="Please enter a valid password length (a positive integer).")
        return

    password_length = int(password_length_str)

    # Ensure the password length is at least 2
    if password_length < 2:
        result_label.config(text="Password length should be at least 2.")
        return

    # Retrieve user preferences for character inclusion
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase if include_lowercase else ''
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine all selected character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        result_label.config(text="Please select at least one character type.")
        return

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(password_length))
    result_label.config(text=f"Generated Password: {password}")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")  # Set window size

# Create and configure widgets
length_label = tk.Label(window, text="Password Length:")
length_entry = tk.Entry(window)

# Boolean variables for user preferences
lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(window, text="Include Lowercase Letters", variable=lowercase_var)
uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
digits_var = tk.IntVar()
digits_check = tk.Checkbutton(window, text="Include Digits", variable=digits_var)
special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=300)

# Place widgets in the window
length_label.pack(pady=10)
length_entry.pack(pady=5)
lowercase_check.pack()
uppercase_check.pack()
digits_check.pack()
special_chars_check.pack()
generate_button.pack(pady=10)
result_label.pack(pady=20)

# Start the Tkinter main loop
window.mainloop()
