import tkinter as tk
from tkinter import Canvas, messagebox
import random
from PIL import Image, ImageTk  # Requires Pillow library
import json
import os

# Initialize scores
user_score = 0
computer_score = 0
best_scores = {"Easy": 0, "Medium": 0, "Hard": 0}
difficulty = "Easy"

# Set up the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("600x500")
root.config(bg="#f0f8ff")

# Load images
rock_img = ImageTk.PhotoImage(Image.open(r"C:\Users\laksh\OneDrive\Desktop\rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open(r"C:\Users\laksh\OneDrive\Desktop\paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open(r"C:\Users\laksh\OneDrive\Desktop\scissor.png").resize((100, 100)))

# Dictionary to map choices to images
images = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

# Function to save best scores to a JSON file
def save_best_scores():
    with open("best_scores.json", "w") as f:
        json.dump(best_scores, f)

# Function to load best scores from a JSON file
def load_best_scores():
    global best_scores
    if os.path.exists("best_scores.json"):
        with open("best_scores.json", "r") as f:
            best_scores = json.load(f)

# Load best scores at the start
load_best_scores()

# Function to show the start menu
def show_start_menu():
    clear_window()
    tk.Label(root, text="Rock Paper Scissors Game", bg="#f0f8ff", font=("Arial", 24)).pack(pady=20)
    tk.Button(root, text="Start Game", command=show_difficulty_menu, bg="#4682b4", fg="white", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Best Scores", command=show_best_scores, bg="#4682b4", fg="white", font=("Arial", 14)).pack(pady=10)

# Function to show difficulty selection menu
def show_difficulty_menu():
    clear_window()
    tk.Label(root, text="Select Difficulty Level", bg="#f0f8ff", font=("Arial", 18)).pack(pady=20)
    tk.Button(root, text="Easy", command=lambda: start_game("Easy"), bg="#4682b4", fg="white", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Medium", command=lambda: start_game("Medium"), bg="#4682b4", fg="white", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Hard", command=lambda: start_game("Hard"), bg="#4682b4", fg="white", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Back", command=show_start_menu, bg="#ff6347", fg="white", font=("Arial", 12)).pack(pady=10)

# Function to show best scores
def show_best_scores():
    clear_window()
    tk.Label(root, text="Best Scores", bg="#f0f8ff", font=("Arial", 24)).pack(pady=20)
    for level, score in best_scores.items():
        tk.Label(root, text=f"{level}: {score}", bg="#f0f8ff", font=("Arial", 16)).pack(pady=5)
    tk.Button(root, text="Back", command=show_start_menu, bg="#ff6347", fg="white", font=("Arial", 12)).pack(pady=10)

# Function to clear the window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Function to start the game
def start_game(selected_difficulty):
    global user_score, computer_score, difficulty
    difficulty = selected_difficulty
    user_score = 0
    computer_score = 0
    show_game()

# Global canvas variable
canvas = None

# Function to show the game interface
def show_game():
    global canvas
    clear_window()
    canvas = Canvas(root, width=400, height=200, bg="#d3d3d3")
    canvas.pack(pady=20)

    result_label = tk.Label(root, text="Result: ", bg="#f0f8ff", fg="blue", font=("Arial", 12, "bold"))
    result_label.pack()

    user_score_label = tk.Label(root, text="Your Score: 0", bg="#f0f8ff", font=("Arial", 12))
    user_score_label.pack()
    
    computer_score_label = tk.Label(root, text="Computer Score: 0", bg="#f0f8ff", font=("Arial", 12))
    computer_score_label.pack()

    # Frame to center the buttons
    button_frame = tk.Frame(root, bg="#f0f8ff")
    button_frame.pack(pady=20)

    button_bg = "#4682b4"
    button_fg = "white"
    tk.Button(button_frame, text="Rock", command=lambda: determine_winner("Rock", user_score_label, computer_score_label, result_label), bg=button_bg, fg=button_fg, font=("Arial", 12)).pack(side="left", padx=5)
    tk.Button(button_frame, text="Paper", command=lambda: determine_winner("Paper", user_score_label, computer_score_label, result_label), bg=button_bg, fg=button_fg, font=("Arial", 12)).pack(side="left", padx=5)
    tk.Button(button_frame, text="Scissors", command=lambda: determine_winner("Scissors", user_score_label, computer_score_label, result_label), bg=button_bg, fg=button_fg, font=("Arial", 12)).pack(side="left", padx=5)

    tk.Button(root, text="Back", command=show_difficulty_menu, bg="#ff6347", fg="white", font=("Arial", 12)).pack(pady=10)
    tk.Button(root, text="Exit", command=exit_game, bg="#ff6347", fg="white", font=("Arial", 12)).pack(pady=10)

# Determine the winner
def determine_winner(user_choice, user_score_label, computer_score_label, result_label):
    global user_score, computer_score
    computer_choice = computer_play()

    # Update the display
    update_canvas(user_choice, computer_choice)

    # Game logic
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Update result and scores
    result_label.config(text=result)
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    # Check and update best scores
    if user_score > best_scores[difficulty]:
        best_scores[difficulty] = user_score
        save_best_scores()

# Function to determine computer choice based on difficulty
def computer_play():
    if difficulty == "Easy":
        return random.choice(["Rock", "Paper", "Scissors"])
    elif difficulty == "Medium":
        # For medium, give a slight bias towards winning
        return random.choices(["Rock", "Paper", "Scissors"], weights=[0.4, 0.4, 0.2])[0]
    elif difficulty == "Hard":
        # For hard, make a better prediction (here simply counter the user)
        return random.choice(["Rock", "Paper", "Scissors"])  # Ideally should predict better

# Update the canvas with animated hands (functionality here)
def update_canvas(user_choice, computer_choice):
    # Display user's choice
    canvas.delete("all")
    user_hand = canvas.create_image(100, 100, image=images[user_choice])
    computer_hand = canvas.create_image(300, 100, image=images[computer_choice])
    
    # Simple animation (can be made more complex if desired)
    for _ in range(5):
        canvas.move(user_hand, 5, 0)
        canvas.move(computer_hand, -5, 0)
        canvas.update()
        canvas.after(50)
        canvas.move(user_hand, -5, 0)
        canvas.move(computer_hand, 5, 0)
        canvas.update()
        canvas.after(50)

# Reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    show_game()

# Exit the game
def exit_game():
    root.destroy()

# Start the game
show_start_menu()
root.mainloop()
