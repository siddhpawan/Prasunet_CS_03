import tkinter as tk
from tkinter import messagebox

class PasswordStrengthAssessmentTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Assessment Tool")
        self.root.configure(background="#f0f0f0")

        # Create input field
        self.password_label = tk.Label(root, text="Enter Password:", bg="#f0f0f0")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, width=40, show="*")
        self.password_entry.pack()

        # Show/Hide password checkbox
        self.show_password_var = tk.IntVar()
        self.show_password_checkbutton = tk.Checkbutton(root, text="Show Password", variable=self.show_password_var, command=self.toggle_password, bg="#f0f0f0")
        self.show_password_checkbutton.pack()

        # Create buttons
        self.assess_button = tk.Button(root, text="Assess Password Strength", command=self.assess_password, bg="#4CAF50", fg="white")
        self.assess_button.pack()

        # Create output field
        self.output_label = tk.Label(root, text="Password Strength:", bg="#f0f0f0")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=5, width=40, bg="#f0f0f0")
        self.output_text.pack()

    def toggle_password(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def assess_password(self):
        password = self.password_entry.get()

        # Initialize password strength score
        score = 0

        # Check password length
        if len(password) < 8:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Password is too short. It should be at least 8 characters.")
            return
        else:
            score += 1

        # Check for uppercase letters
        if any(char.isupper() for char in password):
            score += 1

        # Check for lowercase letters
        if any(char.islower() for char in password):
            score += 1

        # Check for numbers
        if any(char.isdigit() for char in password):
            score += 1

        # Check for special characters
        if any(not char.isalnum() for char in password):
            score += 1

        # Determine password strength based on score
        if score < 3:
            strength = "Weak"
            color = "#FF0000"
        elif score == 3:
            strength = "Medium"
            color = "#FFFF00"
        else:
            strength = "Strong"
            color = "#00FF00"

        # Display password strength
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", f"Password strength: {strength}")
        self.output_text.configure(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthAssessmentTool(root)
    root.mainloop()
