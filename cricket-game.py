import tkinter as tk
from tkinter import messagebox
import random

class NumericCricketGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Numeric Cricket Game")
        self.master.geometry("400x300")
        
        self.player_score = 0
        self.out = False
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Choose a number between 1 and 6:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)
        
        self.play_button = tk.Button(self.master, text="Play", command=self.play_game)
        self.play_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)
        
        self.score_label = tk.Label(self.master, text="Your Score: 0")
        self.score_label.pack(pady=10)
        
        self.choices_label = tk.Label(self.master, text="")
        self.choices_label.pack(pady=10)
    
    def play_game(self):
        if self.out:
            messagebox.showinfo("Game Over", "You are out! Your final score is: " + str(self.player_score))
            return
        
        player_choice = self.entry.get()
        if not player_choice.isdigit() or not (1 <= int(player_choice) <= 6):
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 6.")
            self.entry.delete(0, tk.END)  # Clear the entry widget for new input
            return
        
        player_choice = int(player_choice)
        computer_choice = random.randint(1, 6)
        
        self.choices_label.config(text=f"Player chose: {player_choice}, Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            self.out = True
            messagebox.showinfo("Out!", f"You are out! Your final score is: {self.player_score}")
        else:
            self.player_score += player_choice
            self.score_label.config(text="Your Score: " + str(self.player_score))
        
        self.entry.delete(0, tk.END)  # Clear the entry widget for new input
    
    def reset_game(self):
        self.player_score = 0
        self.out = False
        self.entry.delete(0, tk.END)
        self.score_label.config(text="Your Score: 0")
        self.choices_label.config(text="")

# Create the main window
root = tk.Tk()
game = NumericCricketGame(root)
root.mainloop()
