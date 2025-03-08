import tkinter as tk
import random
from tkinter import messagebox

WORDS = {
    'PYTHON': 'A popular programming language',
    'HANGMAN': 'A classic word-guessing game',
    'PROGRAMMING': 'Writing code to create software',
    'COMPUTER': 'An electronic device for processing data',
    'SCIENCE': 'The study of the natural world',
    'DATABASE': 'A collection of organized data',
    'INTERNET': 'A global network of computers'
}

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x700")
        self.root.configure(bg="#000000")

        self.guessed_letters = set()
        self.word = ""
        self.hint = ""
        self.guessed_word = []
        self.attempts = 6
        self.time_left = 30  

        self.label_word = tk.Label(root, text="", font=("Arial", 24), bg="#f0f0f0", fg="black")
        self.label_word.pack(pady=20)

        self.label_attempts = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0", fg="red")
        self.label_attempts.pack()

        self.label_guessed = tk.Label(root, text="Guessed Letters: ", font=("Arial", 14), bg="#f0f0f0", fg="blue")
        self.label_guessed.pack()

        self.entry = tk.Entry(root, font=("Arial", 16), width=5)
        self.entry.pack(pady=10)

        self.button_guess = tk.Button(root, text="Guess", command=self.guess_letter, bg="lightblue", fg="black")
        self.button_guess.pack()

        self.hint_button = tk.Button(root, text="Hint", command=self.show_hint, bg="lightgreen", fg="black")
        self.hint_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Restart", command=self.reset_game, bg="lightcoral", fg="black")
        self.reset_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=300, height=20, bg="white")
        self.time_bar = self.canvas.create_rectangle(0, 0, 300, 20, fill="red")
        self.canvas.pack()

        self.update_time()
        self.reset_game()

    def update_time(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.canvas.coords(self.time_bar, 0, 0, self.time_left * 10, 20)
            self.root.after(1000, self.update_time)
        else:
            messagebox.showinfo("Time's up!", "You ran out of time!")
            self.reset_game()

    def guess_letter(self):
        letter = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter!")
            return

        if letter in self.guessed_letters:
            messagebox.showwarning("Already Guessed", "You already guessed this letter!")
            return

        self.guessed_letters.add(letter)
        self.label_guessed.config(text=f"Guessed Letters: {', '.join(sorted(self.guessed_letters))}")

        if letter in self.word:
            for idx, char in enumerate(self.word):
                if char == letter:
                    self.guessed_word[idx] = letter
        else:
            self.attempts -= 1

        self.label_word.config(text=" ".join(self.guessed_word))
        self.label_attempts.config(text=f"Attempts left: {self.attempts}")

        if "_" not in self.guessed_word:
            messagebox.showinfo("Congratulations!", "You won!")
            self.reset_game()
        elif self.attempts == 0:
            messagebox.showerror("Game Over", f"You lost! The word was: {self.word}")
            self.reset_game()

    def reset_game(self):
        self.word, self.hint = random.choice(list(WORDS.items()))
        self.guessed_word = ["_" for _ in self.word]
        self.attempts = 6
        self.time_left = 30  # Reset time
        self.guessed_letters.clear()

        # Update UI
        self.label_word.config(text=" ".join(self.guessed_word))
        self.label_attempts.config(text=f"Attempts left: {self.attempts}")
        self.label_guessed.config(text="Guessed Letters: ")

    def show_hint(self):
        messagebox.showinfo("Hint", self.hint)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
