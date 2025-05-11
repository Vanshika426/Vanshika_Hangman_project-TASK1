import random

# Word list
words = ["python", "hangman", "developer", "keyboard", "function"]
word = random.choice(words)

# Game setup
guessed = ["_"] * len(word)
max_attempts = 6
wrong_guesses = 0

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_attempts and "_" in guessed:
    print("\nCurrent Word: ", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print(f"Wrong! Attempts left: {max_attempts - wrong_guesses}")

# Final result
if "_" not in guessed:
    print("\nCongratulations! You won. The word was:", word)
else:
    print("\nGame Over! You lost. The word was:", word)