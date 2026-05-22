import random

# List of predefined words
words = ["apple", "tiger", "house", "robot", "chair"]

# Randomly choose a word
secret_word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while incorrect_guesses < max_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Take input from user
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining chances:", max_guesses - incorrect_guesses)

# If player loses
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)