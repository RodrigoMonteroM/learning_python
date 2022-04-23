import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo, stages


print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
count = 0

# Testing Code
print(f'Pssst, the solution is {chosen_word}.')

# Creating Blanks
display = []

for _ in range(word_length):
    display += '_'

while not end_of_game:
    guess = input('Guess the word\n').lower()

    clear()
    # Check guessed letter
    if guess in chosen_word:
        print(f'you choose "{guess}" it is correct')
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'There is not "{guess} in the word"')
        lives -= 1

        if lives <= 0:
            end_of_game = True

            print(f'You lose, the word was {chosen_word}')

    print(f' '.join(display))

    if '_' not in display:
        end_of_game = True
        print('You win')

    print(stages[lives])