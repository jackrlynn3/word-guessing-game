# Imports used throughout game
import random
import os

# play: function used to play a single game round
#  hidden_word: (str) the word that the user is trying to guess
def play(hidden_word):

    # Initialize game variables
    print("<<< GAME STARTING UP >>>\n")
    guessed_chars = [] # List of already guessed letters
    lives = 7 # Lives left
    round = 1 # Round the player is on
    game_over = False # Game over boolean

    # DEBUG: Uncomment to use
    #print(f'Hidden word: {hidden_word}\n')

    print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')

    # Keeps the player in the game until they win or lose
    while (lives > 0 and not game_over):
        
        # Display meta data for round
        if (lives != 1):
            print(f'ROUND {round}: You have {lives} lives\n')
        else:
            print(f'ROUND {round}: You have {lives} life\n')

        # Get what user wants to do next
        print("Do you want to guess the word or a letter?")
        print("  (1) Guess the word")
        print("  (2) Guess a letter\n")

        # Get user input adn check if valid
        input_1_valid = False
        input_1 = 0
        while (not input_1_valid):
            try:
                input_1 = int(input("  Selection: "))
                if (input_1 == 1 or input_1 == 2): # In correct integer range
                    input_1_valid = True
                    print("\nGood choice!\n")
                else: # Error: Out of correct integer range
                    print("\nPlease select either 1 or 2!\n")
            except: # Error: Not an integer
                print('\nPlease enter an integer!\n')
        
        # Get what progress the user has made on word
        hint = get_known_letters(hidden_word, guessed_chars)
        print(f'Your current working word: {hint}\n')

        # Holds metadata about how round is scored
        lose_pt = False
        win = False

        # Guess a word
        if (input_1 == 1):
            
            # Get user guess
            input_2 = input("Make guess for the word: ")
            print()

            # Check to see if guess is correct
            if (input_2.lower() == hidden_word.lower()): # Case 1: Correct guess
                win = True

            else: # Case 2: Incorrect guess
                lose_pt = True

        # Guess a letter
        else:

            # Get user guess and make sure it hasn't been guessed before 
            input_3_valid = False
            input_3 = 0

            while (not input_3_valid):
                print(f'Letters: {str(guessed_chars)}\n')
                input_3 = input("Make a guess for the letter: ")
                print()

                if (input_3.lower() in guessed_chars): # Error: User already guessed a letter
                    print(f'You\'ve already guessed \'{input_3}\'. Please choose a different character.\n')

                elif (len(input_3) == 1):
                    if (input_3.isalpha()): # Successfuly character guess
                        input_3_valid = True
                        guessed_chars.append(input_3.lower())
                    else: # Error: User guessed a character that is not a letter
                        print(f'Your guess, \'{input_3}\', is not a letter. Please choose an alphabetic character.\n')
                else: # Error: User guessed a string instead of a chacter
                    print("Please enter a character!\n")
            
            # Check to see if guess is correct
            if (get_known_letters(hidden_word, guessed_chars).lower() == hidden_word.lower()): # Case 1: The word is completely revealed
                win = True
            elif input_3.lower() not in hidden_word and input_3.upper() not in hidden_word: # Case 2: Letter is not in word
                lose_pt = True
            else: # Case 3: More of the word is revealed
                print(f'Your guess \'{input_3}\' is in the word: {get_known_letters(hidden_word, guessed_chars)}.\n')
        
        if (lose_pt): # Scenario if user should lose point
            lives -= 1
            if (lives > 1): # Case 1: User still has many points
                print(f'Your guess has resulted in a life lost; you now have {lives} lives!\n')
            elif (lives == 1): # Case 2: User only has one point
                print(f'Your guess has resulted in a life lost; you now have {lives} life! Be careful! You are dangerously close to a loss!\n')
            else: # Case 3: User lost the game
                print(f'You have lost the game! The secret word is: {hidden_word}.\n\nBETTER LUCK NEXT TIME!\n')
        
        if (win): # Scenario if user won the game
            print(f'You have won the game! The secret word is: {hidden_word}.\n\nWONDERFUL JOB!\n')
            game_over = True

        print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')
        
        # Increment rounds
        round += 1
        lose_pt = False
    
    # Game closing procedure
    print("<<< GAME SHUTTING DOWN >>>\n")
    return game_over # True if game was won

# get_known_letters: get a string with all known letters in their correct spots
#   hidden_word: (str) word user is trying to guess
#   guessed_chars: (list(str)) list of letters user has guessed
#   return: (str) formatted string of what letters the user knows, with the rest being underscores
def get_known_letters(hidden_word, guessed_chars):
    revealed_word = ''

    # Iterate through letters to see which are already guessed; all else are _
    for i in range(len(hidden_word)):
        if (hidden_word[i].lower() in guessed_chars):
            revealed_word += hidden_word[i]
        else:
            revealed_word += '_'
    
    # Return revealed word
    return revealed_word

# get_words_list: get a list of words to use in game
#   return: (list(str)) list of potential words to use
def get_words_list():

    os.chdir(os.path.dirname(__file__)) # Change to current directory

    words = open('words-cleaned.txt', 'r').readlines() # Read in words list

    # Strip out newline characters
    for i in range(len(words)):
        words[i] = words[i].strip('\n')

    return words # Return words list

# run_game: starts GUI for running and playing game multiple times
def run_game():

    # Set up game meta stats
    wins = 0
    losses = 0
    words_used = []
    keep_playing = True
    words = get_words_list()

    # DEBUG: Uncomment to use
    #words = ['apple', 'banana', 'orange'] # For debug purposes only

    # Display welcome message
    print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')
    print('WELCOME TO JACK\'S WORD GUESSER GAME!!\n')
    print('The point of this game is to guess the secret word either by guessing the word')
    print('or its characters. You are allowed 7 incorrect attempts before you lose. Are')
    print('you up for the challenge?\n')
    print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')

    # Start game run loop
    while (keep_playing):
        
        # Get current score
        print('SCOREBOARD:')
        print(f'  Wins: {wins}')
        print(f'  Losses: {losses}\n')

        # Get what user wants
        print("What do you want to do next?")
        if (len(words_used) == len(words)):
            print("  (X) Cannot play anymore")
        else:
            print("  (1) Play")
        print("  (2) Exit\n")

        # Get user input
        what_next_valid = False
        what_next = 0

        while (not what_next_valid): # keep going until valid choice is made
            try:
                what_next = int(input("  Selection: ")) # Get input
                print()
                if ((what_next == 1 and len(words_used) != len(words)) or what_next == 2): # Case 1: valid input
                    what_next_valid = True
                else:
                    if (what_next == 1 and len(words_used) == len(words)): # Case 2: user tries to play again, but there are no more games
                        print("There are no more words to play!")
                    else: # Case 3: user selects integer out of range
                        print("Please select either 1 or 2!\n")
            except: # Case 4: input is not integer
                print('Please enter an integer!\n')
        
        # Exit game option
        if (what_next == 2):
            print('Auf Wiedersehen! Play again soon!\n')
            keep_playing = False

        # Play game option
        else:
            new_word = True

            # Keep selecting new words until get one that hasn't been played before
            while (new_word):
                hidden_word = words[random.randint(0, len(words)-1)]
                if (hidden_word not in words_used):
                    new_word = False
            words_used.append(hidden_word)

            # Play game
            win_loss = play(hidden_word)

            # Update scoreboard
            if (win_loss):
                wins += 1
            else:
                losses += 1

        print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')

# Runs the game once python script is called
run_game()