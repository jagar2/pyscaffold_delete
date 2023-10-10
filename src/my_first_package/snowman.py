import random
import pyfiglet

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(words)

def display(word, guesses):
    return ''.join([char if char in guesses else '_' for char in word])

def game():
    word = choose_word()
    attempts = 6
    guesses = []

    print(pyfiglet.figlet_format("Word Guess"))

    while attempts > 0:
        print(f"Remaining attempts: {attempts}")
        print("Word: " + display(word, guesses))

        guess = input("Guess a letter: ").lower()

        if guess in guesses:
            print("You've already guessed this letter.")
            continue

        guesses.append(guess)

        if guess in word:
            print("Correct!")
            if all([char in guesses for char in word]):
                print(f"You've guessed the word: {word}")
                break
        else:
            print("Incorrect!")
            attempts -= 1

    if attempts == 0:
        print(f"Game over! The word was {word}")

if __name__ == "__main__":
    game()
