"""# 🎮 Guess The Number Game

A simple Python number guessing game built on Day 1 of my 28-day coding journey.

## 🎯 How to Play
1. Computer picks a random number between 1-100
2. You guess the number
3. Get "higher" or "lower" hints
4. Try to guess in as few attempts as possible!

## 🛠️ What I Learned
- Random number generation
- While loops and conditionals
- User input handling
- Error handling
- Functions and code organization

## 🚀 How to Run
```bash
python game.py
```

## 📸 Screenshot
[Add a screenshot of the game running]

## 🔮 Future Improvements
- [ ] Add difficulty levels
- [ ] Save high scores to file
- [ ] Add a GUI with tkinter
- [ ] Multiplayer mode
"""
import random

def play_game():
    #generate a random number
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess The Number Game!")
    print("I am thinking of a number between 1 and 100...")
    print("Try to guess the number.")

    while True:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1

            if guess == number:
                print("You guessed the number!")
                return attempts
            elif guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
        except ValueError:
            print("Please enter a valid number.")
def main():
    high_score = None
    while True:
        score = play_game()
        if high_score is None or score > high_score:
            high_score = score
            print("New high score!")
        else:
            print("High score is the same")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again != "y":
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main()

