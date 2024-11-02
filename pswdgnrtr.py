import random
import string
import pyperclip  # Requires the pyperclip package (install via pip install pyperclip)
import tkinter as tk
from tkinter import messagebox, IntVar

# Dictionary for creating mnemonic based on password characters
mnemonic_dict = {
    'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog', 'E': 'Elephant',
    'F': 'Fish', 'G': 'Giraffe', 'H': 'Hat', 'I': 'Ice', 'J': 'Jar',
    'K': 'Kite', 'L': 'Lion', 'M': 'Monkey', 'N': 'Nest', 'O': 'Orange',
    'P': 'Panda', 'Q': 'Queen', 'R': 'Rabbit', 'S': 'Sun', 'T': 'Tree',
    'U': 'Umbrella', 'V': 'Van', 'W': 'Whale', 'X': 'Xylophone', 'Y': 'Yak', 'Z': 'Zebra',
    '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
    '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero',
    '!': 'Exclamation', '@': 'At', '#': 'Hash', '$': 'Dollar', '%': 'Percent',
    '^': 'Caret', '&': 'And', '*': 'Star', '(': 'LeftBracket', ')': 'RightBracket'
}

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a random password with specified length and character types."""
    character_pools = []
    if use_upper:
        character_pools.append(string.ascii_uppercase)
    if use_lower:
        character_pools.append(string.ascii_lowercase)
    if use_digits:
        character_pools.append(string.digits)
    if use_symbols:
        character_pools.append(string.punctuation)

    if not character_pools:
        return "Please select at least one character type!"

    # Generate the password by randomly choosing from selected character pools
    all_characters = ''.join(character_pools)
    password = ''.join(random.choices(all_characters, k=length))
    return password

def generate_mnemonic(password):
    """Create a mnemonic based on the generated password."""
    mnemonic = []
    for char in password:
        mnemonic.append(mnemonic_dict.get(char.upper(), char))  # Use word if available, else the char itself
    return ' '.join(mnemonic)

def copy_to_clipboard(password):
    """Copy the generated password to clipboard."""
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")

def generate_and_display():
    """Get user preferences, generate password and mnemonic, and display them."""
    length = length_var.get()
    if length < 4:
        messagebox.showwarning("Warning", "Password length should be at least 4.")
        return

    # Generate password based on user's choices
    password = generate_password(
        length, 
        upper_var.get(), 
        lower_var.get(), 
        digits_var.get(), 
        symbols_var.get()
    )
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Generate and display mnemonic
    mnemonic_text = generate_mnemonic(password)
    mnemonic_entry.delete(0, tk.END)
    mnemonic_entry.insert(0, mnemonic_text)

    # Check password strength
    check_password_strength(password)

    # Copy password to clipboard
    copy_to_clipboard(password)

def check_password_strength(password):
    """Display password strength based on length and character variety."""
    strength = "Weak"
    if len(password) >= 12 and any(c.isupper() for c in password) \
            and any(c.islower() for c in password) and any(c.isdigit() for c in password) \
            and any(c in string.punctuation for c in password):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Moderate"
    
    strength_label.config(text=f"Password Strength: {strength}")

# Set up the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x600")

# Password length selection
tk.Label(root, text="Password Length:").pack(pady=5)
length_var = tk.IntVar(value=12)
length_scale = tk.Scale(root, from_=4, to=32, orient='horizontal', variable=length_var)
length_scale.pack(pady=5)

# Character type options
upper_var = IntVar(value=1)
lower_var = IntVar(value=1)
digits_var = IntVar(value=1)
symbols_var = IntVar(value=1)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

# Generate and display password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display)
generate_button.pack(pady=10)

# Display generated password
tk.Label(root, text="Generated Password:").pack()
password_entry = tk.Entry(root, font=("Arial", 14), justify='center')
password_entry.pack(pady=5)

# Display generated mnemonic
tk.Label(root, text="Mnemonic for Password:").pack()
mnemonic_entry = tk.Entry(root, font=("Arial", 10), justify='center', width=50)
mnemonic_entry.pack(pady=5)

# Display password strength
strength_label = tk.Label(root, text="Password Strength: ", font=("Arial", 12))
strength_label.pack(pady=5)

# Run the GUI loop
root.mainloop()

