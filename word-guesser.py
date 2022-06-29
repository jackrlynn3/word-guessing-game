def word_guesser():
    
    # Initialize game variables\
    print("<<< GAME STARTING UP >>>\n")
    guessed_chars = [] # List of already guessed letters
    lives = 7 # Lives left
    round = 1 # Round the player is on
    game_over = False # Game over boolean
    hidden_word = "Bananas" # Word that user is trying to guess

    while (lives > 0 and not game_over):
        
        # Display meta data for round
        if (lives != 1):
            print(f'ROUND {round}: You have {lives} lives\n')
        else:
            print(f'ROUND {round}: You have {lives} life\n')

        # Get if user wants
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
            input_2 = input("Make guess for word: ")
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
                input_3 = input("  Selection: ")
                print()
                if (input_3.lower() in guessed_chars):
                    print(f'You\'ve already guessed \'{input_3}\'. Please choose a different character.\n')
                elif (len(input_3) == 1):
                    if (input_3.isalpha()):
                        input_3_valid = True
                        print("Good choice!\n")
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
        
        round += 1
        lose_pt = False
    
    print("<<< GAME SHUTTING DOWN >>>")

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

word_guesser()