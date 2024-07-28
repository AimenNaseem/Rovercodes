import tkinter as tk
from tkinter import font
import random

def getComputerChoice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determineWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif (userChoice == "rock" and computerChoice == "scissors") or \
         (userChoice == "scissors" and computerChoice == "paper") or \
         (userChoice == "paper" and computerChoice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def playGame(userChoice):
    computerChoice = getComputerChoice()
    result = determineWinner(userChoice, computerChoice)
    displayResult(userChoice, computerChoice, result)

def displayResult(userChoice, computerChoice, result):
    result_label.config(text=f"You chose: {userChoice}\nComputer chose: {computerChoice}\n{result}")

def createMainWindow():
    window = tk.Tk()
    window.title("Rock, Paper, Scissors Game")
    window.config(bg="#D4F1F4")
    
    custom_font = font.Font(family="Comic Sans MS", size=16, weight="bold")
    
    title_label = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Comic Sans MS", 24, "bold"), bg="#D4F1F4", fg="#056676")
    title_label.pack(pady=20)

    frame = tk.Frame(window, bg="#D4F1F4")
    frame.pack(pady=20)

    rock_button = tk.Button(frame, text="Rock", font=custom_font, command=lambda: playGame("rock"), bg="#FF6F61", fg="white")
    rock_button.grid(row=0, column=0, padx=20)
    
    paper_button = tk.Button(frame, text="Paper", font=custom_font, command=lambda: playGame("paper"), bg="#6FFFB0", fg="white")
    paper_button.grid(row=0, column=1, padx=20)
    
    scissors_button = tk.Button(frame, text="Scissors", font=custom_font, command=lambda: playGame("scissors"), bg="#6F61FF", fg="white")
    scissors_button.grid(row=0, column=2, padx=20)
    
    global result_label
    result_label = tk.Label(window, text="", font=custom_font, bg="#D4F1F4", fg="#056676", pady=20)
    result_label.pack(pady=20)
    
    tk.Button(window, text="Quit", font=custom_font, bg="#FF6F61", fg="white", command=window.quit).pack(pady=10)
    
    return window

if __name__ == "__main__":
    main_window = createMainWindow()
    main_window.mainloop()

