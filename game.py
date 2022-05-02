import random 

# make 3 functions
# one is a welcome statement
# one is a random word generator
# the last one is the game function


def welcome():
    print('Welcome to the Letter-Guessing-Game!')

#use this if you ever want to replace letters with a certain character
def secrets():
    # make a list
     my_list = ['ADORE', 'BLESS', 'DREAM', 'FOCUS','HELLO', 'EAGER', 'TRASH', 'HEART', 'HUMAN', 'LEARN']
     # use random.choice() method to call a word from the list
     secret_word = list(random.choice(my_list))
     # use list comprehension to make code easier and faster
     underscores = ['_' for letter in secret_word]
     print(' '.join(underscores))
     return secret_word


# this is the game. find a way to call both functions within game function

def game():
    welcome()
    secret_word = secrets()
    underscores = ['_' for letter in secret_word]
    turns = 7
# the start of loop. Everything revolves around user having 7 turns
    while turns > 0:
        user_input = input('Guess a letter!: ').upper()
# used upper() to make user input upper to match list
# Need to focus on: 
#what happens if user input isnt in the secret word
# what happens if user runs out of turns?
# make sure User loses turns for wrong guesses
# what happens if user guesses a letter right
# what happens when user gets all the words right
        if user_input not in secret_word:
            turns -= 1
            print(f'Letter not in word. Keep Going! You have {turns} left!')
        if turns == 0:
            print(f'You Lost! Better luck next time! The word was {"".join(secret_word)}')
            break
# have to use "in"
# for a value in the range of the length of (secret word)
# had help for line 51 thru 56

        if user_input in secret_word:
            print('Good job.')
            for i in range(len(secret_word)):
                if list(secret_word)[i] == user_input:
                    underscores[i] = user_input
            print(' '.join(underscores))
        
        if underscores == secret_word:
            print('You win!')
            break

game()