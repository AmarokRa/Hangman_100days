
import random

import Hangman_Dictionary
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

incorerrect_letters = []

end_of_game = False
lives = 6

from Hangman_log import logo, stages 
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You're already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    print("Incorrect letters:", ' '.join(incorerrect_letters))
    if "_" not in display:
        end_of_game = True
        print("You win.")
        break

    print(stages[lives])