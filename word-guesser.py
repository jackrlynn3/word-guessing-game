import random
import os

def play(hidden_word):

    # Initialize game variables
    print("<<< GAME STARTING UP >>>\n")
    guessed_chars = [] # List of already guessed letters
    lives = 7 # Lives left
    round = 1 # Round the player is on
    game_over = False # Game over boolean
    #print(f'Hidden word: {hidden_word}\n') # FOR DEBUG PURPOSES ONLY

    print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')

    while (lives > 0 and not game_over):
        
        # Display meta data for round
        if (lives != 1):
            print(f'ROUND {round}: You have {lives} lives\n')
        else:
            print(f'ROUND {round}: You have {lives} life\n')

        # Get what user wants
        print("Do you want to guess the word or a letter?")
        print("  (1) Guess the word")
        print("  (2) Guess a letter\n")

        # Get user input
        input_1_valid = False
        input_1 = 0
        while (not input_1_valid):
            try:
                input_1 = int(input("  Selection: "))
                if (input_1 == 1 or input_1 == 2):
                    input_1_valid = True
                    print("\nGood choice!\n")
                else:
                    print("\nPlease select either 1 or 2!\n")
            except:
                print('\nPlease enter an integer!\n')
        
        # Get current revealed word
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
            if (input_2.lower() == hidden_word.lower()):
                win = True
            else:
                lose_pt = True

        # Guess a word
        else:

            # Get user guess and make sure it hasn't been guessed before 
            input_3_valid = False
            input_3 = 0
            while (not input_3_valid):
                print(f'Letters: {str(guessed_chars)}\n')
                input_3 = input("Make a guess for the letter: ")
                print()
                if (input_3.lower() in guessed_chars):
                    print(f'You\'ve already guessed \'{input_3}\'. Please choose a different character.\n')
                elif (len(input_3) == 1):
                    if (input_3.isalpha()):
                        input_3_valid = True
                        guessed_chars.append(input_3.lower())
                    else:
                        print(f'Your guess, \'{input_3}\', is not a letter. Please choose an alphabetic character.\n')
                else:
                    print("Please enter a character!\n")
            
            # Check to see if guess is correct
            if (get_known_letters(hidden_word, guessed_chars).lower() == hidden_word.lower()):
                win = True
            elif input_3.lower() not in hidden_word and input_3.upper() not in hidden_word:
                lose_pt = True
            else:
                print(f'Your guess \'{input_3}\' is in the word: {get_known_letters(hidden_word, guessed_chars)}.\n')
        
        if (lose_pt):
            lives -= 1
            if (lives > 1):
                print(f'Your guess has resulted in a life lost; you now have {lives} lives!\n')
            elif (lives == 1):
                print(f'Your guess has resulted in a life lost; you now have {lives} life! Be careful! You are dangerously close to a loss!\n')
            else:
                print(f'You have lost the game! The secret word is: {hidden_word}.\n\nBETTER LUCK NEXT TIME!\n')
        
        if (win):
            print(f'You have won the game! The secret word is: {hidden_word}.\n\nWONDERFUL JOB!\n')
            game_over = True

        print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')
        
        round += 1
        lose_pt = False
    
    print("<<< GAME SHUTTING DOWN >>>\n")

    return game_over # True if game was won

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

def get_words_list():
    os.chdir(os.path.dirname(__file__))
    words = open('words-cleaned.txt', 'r').readlines()
    # Strip out newline characters
    for i in range(len(words)):
        words[i] = words[i].strip('\n')
    return words

def run_game():

    # Set up game meta stats
    wins = 0
    losses = 0
    words_used = []
    keep_playing = True
    words = get_words_list()
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
        while (not what_next_valid):
            try:
                what_next = int(input("  Selection: "))
                print()
                if ((what_next == 1 and len(words_used) != len(words)) or what_next == 2):
                    what_next_valid = True
                else:
                    if (what_next == 1 and len(words_used) == len(words)):
                        print("There are no more words to play!")
                    else:
                        print("Please select either 1 or 2!\n")
            except:
                print('Please enter an integer!\n')
        
        # Exit game option
        if (what_next == 2):
            print('Auf Wiedersehen! Play again soon!\n')
            keep_playing = False

        # Play game option
        else:
            new_word = True
            while (new_word):
                hidden_word = words[random.randint(0, len(words)-1)]
                if (hidden_word not in words_used):
                    new_word = False
            words_used.append(hidden_word)
            win_loss = play(hidden_word)
            if (win_loss):
                wins += 1
            else:
                losses += 1

        print('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')


run_game()