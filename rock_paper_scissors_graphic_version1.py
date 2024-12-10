import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        self.player_score = 0
        self.computer_score = 0
        self.current_round = 1
        self.rounds = 3

        
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e2f")  

        
        self.title_label = tk.Label(self.root, text="Rock Paper Scissors Game", font=("Helvetica", 18, "bold"), fg="#f8f8f2", bg="#1e1e2f")
        self.title_label.pack(pady=20)

        
        self.player_choice_label = tk.Label(self.root, text="Your choice: ", font=("Helvetica", 14), fg="#8be9fd", bg="#1e1e2f")
        self.player_choice_label.pack()

        self.computer_choice_label = tk.Label(self.root, text="Computer's choice: ", font=("Helvetica", 14), fg="#ffb86c", bg="#1e1e2f")
        self.computer_choice_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"), fg="#50fa7b", bg="#1e1e2f")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14), fg="#bd93f9", bg="#1e1e2f")
        self.score_label.pack(pady=10)

        
        self.button_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(self.button_frame, text="Rock", font=("Helvetica", 12), bg="#6272a4", fg="#f8f8f2", command=lambda: self.play('r'))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", font=("Helvetica", 12), bg="#6272a4", fg="#f8f8f2", command=lambda: self.play('p'))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=("Helvetica", 12), bg="#6272a4", fg="#f8f8f2", command=lambda: self.play('s'))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        
        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Helvetica", 12), bg="#44475a", fg="#f8f8f2", command=self.restart_game)
        self.restart_button.pack(pady=20)
        self.restart_button.pack_forget()  

        
        self.root.mainloop()

    def play(self, player_choice):
        if self.current_round > self.rounds:
            return

        computer_choice = random.choice(list(self.choices.keys()))

        
        if player_choice == computer_choice:
            result = "It's a draw!"
        elif (
            (player_choice == 'r' and computer_choice == 's') or
            (player_choice == 'p' and computer_choice == 'r') or
            (player_choice == 's' and computer_choice == 'p')
        ):
            result = "You won this round!"
            self.player_score += 1
        else:
            result = "You lost this round!"
            self.computer_score += 1

        self.current_round += 1

        
        self.player_choice_label.config(text=f"Your choice: {self.choices[player_choice]}")
        self.computer_choice_label.config(text=f"Computer's choice: {self.choices[computer_choice]}")
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}")

        
        if self.current_round > self.rounds:
            self.end_game()

    def end_game(self):
        if self.player_score > self.computer_score:
            final_result = "Congratulations! You won the game!"
        elif self.player_score < self.computer_score:
            final_result = "Game over! You lost the game!"
        else:
            final_result = "It's a draw!"

        self.result_label.config(text=final_result)
        self.restart_button.pack(pady=20)  

    def restart_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.current_round = 1

        
        self.player_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer's choice: ")
        self.result_label.config(text="")
        self.score_label.config(text="Score - You: 0, Computer: 0")

        self.restart_button.pack_forget()  


RockPaperScissorsGame()
