

import random
from hangmanWords import word_list

from hangmanArt import logo
print(logo,"\n")

from hangmanArt import hangmanStages

chosen_word = random.choice(word_list)


lives = 6
display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(f' your word has {" ".join(display)}')



n=6
wrong = 0

endOfGame = False
guessed_letters = []
while not endOfGame:
    

         
    guess = input("Guess a letter: ").lower()
    
    
    if guess in display :
            print(f"You have already guessed the letter {guess} , go again !")



    for position in range(len(chosen_word)):
        
        if chosen_word[position] == guess :
            display[position]=guess

    if guess not in chosen_word:
        print(f"The guessed letter , '{guess}' is not in the word ,you lose a life")
        lives -= 1
        
        print(hangmanStages[n-lives])
        if lives == 0:
            print("GAME OVER , you lose .")
            print("The word was : "+chosen_word)
            endOfGame = True

    print(" ".join(display))
if "_" not in display:
    endOfGame = True
    print("You Win.")



