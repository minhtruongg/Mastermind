"""
Mastermind Game - Programming I Semester Project

A simple color guessing game where the player tries to guess a secret code.
The game gives hints after each guess and can suggest moves.
"""

import tkinter as tk
from tkinter import messagebox
import random

# Game settings
COLORS = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']
CODE_LENGTH = 4
MAX_ATTEMPTS = 10

# Store game data
secret_code = []
guess_history = []
current_attempt = 0
current_guess = []

def generate_secret_code():
    """
    Generate a random secret code for the game.
    
    Returns:
        list: A list of random colors of length CODE_LENGTH
    """
    code = []
    for i in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def calculate_feedback(guess, secret):
    """
    Calculate black and white pegs for a guess.
    
    Args:
        guess (list): The player's guess
        secret (list): The secret code
        
    Returns:
        tuple: (black_pegs, white_pegs)
               black_pegs = correct color in correct position
               white_pegs = correct color in wrong position
    """
    black_pegs = 0
    white_pegs = 0
    
    # Count black pegs (exact matches)
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            black_pegs = black_pegs + 1
    
    # Count white pegs (color exists but wrong position)
    for color in COLORS:
        guess_count = guess.count(color)
        secret_count = secret.count(color)
        min_count = min(guess_count, secret_count)
        white_pegs = white_pegs + min_count
    
    white_pegs = white_pegs - black_pegs
    
    return black_pegs, white_pegs

def get_hint():
    """
    Suggest a possible guess based on previous attempts.
    Uses simple strategy: find colors that match previous feedback.
    
    Returns:
        list: A suggested guess
    """
    # If no history, suggest random guess
    if len(guess_history) == 0:
        hint = []
        for i in range(CODE_LENGTH):
            hint.append(random.choice(COLORS))
        return hint
    
    # Try to find a guess that matches all previous feedback
    possible_codes = []
    
    # Generate some random possibilities
    for attempt in range(100):
        test_code = []
        for i in range(CODE_LENGTH):
            test_code.append(random.choice(COLORS))
        
        # Check if this code fits all previous feedback
        is_valid = True
        for old_guess, old_black, old_white in guess_history:
            test_black, test_white = calculate_feedback(old_guess, test_code)
            if test_black != old_black or test_white != old_white:
                is_valid = False
                break
        
        if is_valid:
            possible_codes.append(test_code)
            if len(possible_codes) >= 10:
                break
    
    if len(possible_codes) > 0:
        return random.choice(possible_codes)
    else:
        # If nothing found, return random
        hint = []
        for i in range(CODE_LENGTH):
            hint.append(random.choice(COLORS))
        return hint

def add_color_to_guess(color):
    """Add a color to the current guess."""
    global current_guess
    if len(current_guess) < CODE_LENGTH:
        current_guess.append(color)
        update_guess_display()

def clear_current_guess():
    """Clear the current guess."""
    global current_guess
    current_guess = []
    update_guess_display()

def update_guess_display():
    """Update the display showing current guess."""
    for i in range(CODE_LENGTH):
        circle = guess_circles[i]
        circle.delete("all")
        if i < len(current_guess):
            color = current_guess[i]
            if color == 'Red':
                circle.create_oval(5, 5, 35, 35, fill='red')
            elif color == 'Blue':
                circle.create_oval(5, 5, 35, 35, fill='blue')
            elif color == 'Green':
                circle.create_oval(5, 5, 35, 35, fill='green')
            elif color == 'Yellow':
                circle.create_oval(5, 5, 35, 35, fill='yellow')
            elif color == 'Orange':
                circle.create_oval(5, 5, 35, 35, fill='orange')
            elif color == 'Purple':
                circle.create_oval(5, 5, 35, 35, fill='purple')

def show_hint_popup():
    """Show a hint to the player."""
    hint = get_hint()
    hint_text = ""
    for i in range(len(hint)):
        hint_text = hint_text + hint[i]
        if i < len(hint) - 1:
            hint_text = hint_text + ", "
    messagebox.showinfo("Hint", "Try this: " + hint_text)

def submit_guess():
    """Process the player's guess."""
    global current_attempt, current_guess, guess_history
    
    # Check if guess is complete
    if len(current_guess) != CODE_LENGTH:
        messagebox.showwarning("Error", "Please select " + str(CODE_LENGTH) + " colors!")
        return
    
    # Calculate feedback
    black, white = calculate_feedback(current_guess, secret_code)
    
    # Save to history
    guess_history.append((current_guess[:], black, white))
    current_attempt = current_attempt + 1
    
    # Show in history
    add_guess_to_history(current_guess, black, white)
    
    # Update attempt counter
    attempt_label.config(text="Attempt: " + str(current_attempt) + "/" + str(MAX_ATTEMPTS))
    
    # Check win condition
    if black == CODE_LENGTH:
        show_game_over(True)
    elif current_attempt >= MAX_ATTEMPTS:
        show_game_over(False)
    else:
        current_guess = []
        update_guess_display()

def add_guess_to_history(guess, black, white):
    """Add a guess to the history display."""
    row = tk.Frame(history_frame)
    row.pack(pady=2)
    
    # Show colors
    for color in guess:
        canvas = tk.Canvas(row, width=25, height=25)
        if color == 'Red':
            canvas.create_oval(2, 2, 23, 23, fill='red')
        elif color == 'Blue':
            canvas.create_oval(2, 2, 23, 23, fill='blue')
        elif color == 'Green':
            canvas.create_oval(2, 2, 23, 23, fill='green')
        elif color == 'Yellow':
            canvas.create_oval(2, 2, 23, 23, fill='yellow')
        elif color == 'Orange':
            canvas.create_oval(2, 2, 23, 23, fill='orange')
        elif color == 'Purple':
            canvas.create_oval(2, 2, 23, 23, fill='purple')
        canvas.pack(side=tk.LEFT, padx=2)
    
    # Show feedback
    feedback_text = "  Black: " + str(black) + "  White: " + str(white)
    tk.Label(row, text=feedback_text).pack(side=tk.LEFT, padx=10)

def show_game_over(won):
    """Show game over message."""
    secret_text = ""
    for i in range(len(secret_code)):
        secret_text = secret_text + secret_code[i]
        if i < len(secret_code) - 1:
            secret_text = secret_text + ", "
    
    if won:
        message = "You won in " + str(current_attempt) + " attempts!\n"
        message = message + "Secret code: " + secret_text
        messagebox.showinfo("Congratulations!", message)
    else:
        message = "Game Over!\n"
        message = message + "Secret code was: " + secret_text
        messagebox.showinfo("Game Over", message)
    
    # Ask to play again
    play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if play_again:
        reset_game()
    else:
        window.quit()

def reset_game():
    """Reset the game to play again."""
    global secret_code, guess_history, current_attempt, current_guess
    
    secret_code = generate_secret_code()
    guess_history = []
    current_attempt = 0
    current_guess = []
    
    # Clear displays
    for widget in history_frame.winfo_children():
        widget.destroy()
    
    update_guess_display()
    attempt_label.config(text="Attempt: 0/" + str(MAX_ATTEMPTS))

# Create the window
window = tk.Tk()
window.title("Mastermind Game")
window.geometry("400x600")

# Title
title_label = tk.Label(window, text="MASTERMIND", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Attempt counter
attempt_label = tk.Label(window, text="Attempt: 0/" + str(MAX_ATTEMPTS), font=("Arial", 12))
attempt_label.pack()

# Current guess area
tk.Label(window, text="Current Guess:", font=("Arial", 10)).pack(pady=5)
guess_frame = tk.Frame(window)
guess_frame.pack()

guess_circles = []
for i in range(CODE_LENGTH):
    circle = tk.Canvas(guess_frame, width=40, height=40, bg='lightgray')
    circle.grid(row=0, column=i, padx=5)
    guess_circles.append(circle)

# Color buttons
tk.Label(window, text="Select Colors:", font=("Arial", 10)).pack(pady=5)
color_frame = tk.Frame(window)
color_frame.pack()

for color in COLORS:
    btn_color = color.lower()
    btn = tk.Button(color_frame, text=color, bg=btn_color, width=8,
                    command=lambda c=color: add_color_to_guess(c))
    btn.pack(side=tk.LEFT, padx=2)

# Action buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

clear_btn = tk.Button(button_frame, text="Clear", width=10, command=clear_current_guess)
clear_btn.pack(side=tk.LEFT, padx=5)

hint_btn = tk.Button(button_frame, text="Get Hint", width=10, command=show_hint_popup)
hint_btn.pack(side=tk.LEFT, padx=5)

submit_btn = tk.Button(button_frame, text="Submit", width=10, bg='lightgreen', command=submit_guess)
submit_btn.pack(side=tk.LEFT, padx=5)

# History area
tk.Label(window, text="Previous Guesses:", font=("Arial", 12, "bold")).pack(pady=10)
history_frame = tk.Frame(window)
history_frame.pack()

# Start the game
secret_code = generate_secret_code()

# Run the game
window.mainloop()