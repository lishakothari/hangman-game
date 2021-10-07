import random
from hangman_words import word_list

#using word list from hangman module
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

#Testing code
#print(f'the solution is {chosen_word}.')

#Creating blanks
display = []
for _ in range(word_length-1):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

  
    if guess in display:
      print(f"you have already guessed {guess}")

    #Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Checking if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f" The correct answer was:{chosen_word}")

    #Joining all the elements in the list into a String.
    print(f"{' '.join(display)}")

    #Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    from hangman_art import stages
    print(stages[lives])