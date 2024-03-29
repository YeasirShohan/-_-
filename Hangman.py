import random

def choose_word():
    words = ["lion", "tiger", "elephant","zebra", "rhinoceros", "giraffe", "hippopotamus"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    word_set = set(word)
    guessed_letters = set()
    attempts_left = 7

    print("Welcome to Animal Hangman!")
    print("Try to guess the name of an animal. You have 7 attempts.")

    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.add(guess)
        if guess in word_set:
            word_set.discard(guess)
            print("Correct guess!")
            if not word_set:
                print("Congratulations! You've guessed the animal:", word)
                break
        else:
            attempts_left -= 1
            print("Incorrect guess! Attempts left:", attempts_left)
            if attempts_left == 0:
                print("Sorry, you're out of attempts. The animal was:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing Animal Hangman!")

hangman()
