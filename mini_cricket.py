import tkinter as tk
from tkinter import messagebox
import random

# Initialize game variables
total_score = 0
wickets = 0
balls_played = 0
total_balls = 30  # 5 overs x 6 balls per over
player_batting = True  # Track which team is batting
target_score = 0  # The target score for the opponent

# Function to handle player's shot
def play_shot(player_choice):
    global total_score, wickets, balls_played, player_batting, target_score

    if balls_played >= total_balls or wickets >= 3:
        return  # Stop if innings is over

    system_choice = random.randint(1, 6)  # System generates a number
    balls_played += 1  # Increase ball count

    if player_choice == system_choice:
        wickets += 1
        result_label.config(text=f"OUT! Wickets: {wickets}/3", fg="red")
    else:
        total_score += player_choice
        result_label.config(text=f"You scored {player_choice} runs!", fg="green")

    # Update score display
    score_label.config(text=f"Score: {total_score} | Wickets: {wickets}/3")
    balls_label.config(text=f"Balls: {balls_played}/{total_balls} (Overs: {balls_played // 6}.{balls_played % 6})")

    # Check if innings is over
    if wickets >= 3 or balls_played >= total_balls:
        if player_batting:
            target_score = total_score + 1  # Opponent needs 1 more than Player's score
            messagebox.showinfo("Innings Over", f"Your innings is over! Target for Opponent: {target_score}")
            start_opponent_innings()
        else:
            check_winner()

# Function to handle opponent's innings
def start_opponent_innings():
    global total_score, wickets, balls_played, player_batting
    player_batting = False
    total_score = 0
    wickets = 0
    balls_played = 0
    result_label.config(text="Opponent's turn to bat! Click 'Opponent Play'.", fg="blue")

# Function for opponent to play shots
def opponent_play():
    global total_score, wickets, balls_played

    if balls_played >= total_balls or wickets >= 3 or total_score >= target_score:
        return

    opponent_choice = random.randint(1, 6)
    system_choice = random.randint(1, 6)
    balls_played += 1

    if opponent_choice == system_choice:
        wickets += 1
        result_label.config(text=f"Opponent OUT! Wickets: {wickets}/3", fg="red")
    else:
        total_score += opponent_choice
        result_label.config(text=f"Opponent scored {opponent_choice} runs!", fg="green")

    # Update score display
    score_label.config(text=f"Opponent Score: {total_score} | Wickets: {wickets}/3")
    balls_label.config(text=f"Balls: {balls_played}/{total_balls} (Overs: {balls_played // 6}.{balls_played % 6})")

    if wickets >= 3 or balls_played >= total_balls or total_score >= target_score:
        check_winner()

# Function to check and declare the winner
def check_winner():
    if total_score >= target_score:
        messagebox.showinfo("Match Over", "Opponent Wins! 🏆")
    elif total_score < target_score and (wickets >= 3 or balls_played >= total_balls):
        messagebox.showinfo("Match Over", "You Win! 🎉")
    else:
        messagebox.showinfo("Match Over", "It's a Draw!")

    restart_game()

# Function to restart the game
def restart_game():
    global total_score, wickets, balls_played, player_batting, target_score
    total_score = 0
    wickets = 0
    balls_played = 0
    target_score = 0
    player_batting = True  # Player bats first
    result_label.config(text="Choose a number between 1 and 6 to play!", fg="white")
    score_label.config(text="Score: 0 | Wickets: 0/3")
    balls_label.config(text="Balls: 0/30 (Overs: 0.0)")

# Create the main window
window = tk.Tk()
window.title("🏏 Cricket Game - Player vs Opponent")
window.geometry("550x500")
window.config(bg="#2C3E50")

# Title Label
tk.Label(window, text="🏏 Cricket Game - Player vs Opponent", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

# Scoreboard Frame
score_frame = tk.Frame(window, bg="#34495E", bd=5, relief="ridge")
score_frame.pack(pady=10, padx=10, fill="x")

score_label = tk.Label(score_frame, text="Score: 0 | Wickets: 0/3", font=("Arial", 14, "bold"), bg="#16A085", fg="white", width=30)
score_label.pack(pady=5, padx=10)

balls_label = tk.Label(score_frame, text="Balls: 0/30 (Overs: 0.0)", font=("Arial", 12), bg="#2980B9", fg="white", width=35)
balls_label.pack(pady=5, padx=10)

# Result Label
result_frame = tk.Frame(window, bg="#2C3E50", bd=3, relief="ridge")
result_frame.pack(pady=10, padx=10, fill="x")

result_label = tk.Label(result_frame, text="Choose a number between 1 and 6 to play!", font=("Arial", 12), bg="#2C3E50", fg="white")
result_label.pack(pady=10)

# Buttons for Player's shot selection
button_frame = tk.Frame(window, bg="#2C3E50")
button_frame.pack(pady=10)
for i in range(1, 7):
    btn = tk.Button(button_frame, text=str(i), font=("Arial", 12, "bold"), width=5, height=2, bg="#F1C40F", fg="black",
                    command=lambda i=i: play_shot(i))
    btn.grid(row=0, column=i-1, padx=5, pady=5)

# Opponent Play Button
opponent_button = tk.Button(window, text="Opponent Play Ball", font=("Arial", 12, "bold"), bg="#E67E22", fg="white",
                            command=opponent_play)
opponent_button.pack(pady=10)

# Restart button
restart_button = tk.Button(window, text="Restart Game", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white",
                           command=restart_game)
restart_button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()
