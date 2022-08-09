import random
from hangman_words import word_list
from hangman_stages import stages
from hangman_logo import logo

chosen_word = random.choice(word_list)
lower_case_chosen_word = chosen_word.lower()

size_of_word = len(chosen_word)

print(logo)
print(stages[0])


blank_array = []

for num in range(0, size_of_word):
    blank_array.append("_")

#print(blank_array)

#print(lower_case_chosen_word)

#print(blank_array)

endgame = False
lives_left = 6
already_guessed = []

while not endgame:
    guessed_char = input("Guess a letter: \n").lower()

    if guessed_char in already_guessed:
        print("You have already guessed the letter.")

    for num in range(0, size_of_word):
        if guessed_char == lower_case_chosen_word[num]:
            blank_array[num] = guessed_char
            already_guessed.append(guessed_char)

    if guessed_char not in lower_case_chosen_word and guessed_char not in already_guessed:
        lives_left -= 1
        already_guessed.append(guessed_char)
        print(f"You guessed the letter {guessed_char}. This letter is not present in the word. You lose a life :(")
        print(stages[6 - lives_left])

    print(blank_array)

    if "_" not in blank_array:
        endgame = True
        print("You won")

    if lives_left == 0:
        endgame = True
        print("You lost")
