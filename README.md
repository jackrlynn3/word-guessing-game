# Jack's Word Guesser Game
Hello! Do you want to test your ability to guess words on your terminal prompt? Now you can with **Jack's Word Guesser Game**! In this game, you attempt to guess one of several thousand English words, *many of which you've probably never heard of*. Every round you can either guess the word or a new letter, but beware a wrong choice will cause you to lose one of your seven lives. Think Hangman but less gruesome! **Do you think you are up to the challenge?**
*Creator: Jack Lynn (Dev10 Data Associate)*

## How to Run
**Prerequisite:** Requires Python 3.8 or later.
**Step 1:** Download the Git repository from [here](https://github.com/jackrlynn3/word-guessing-game).
**Step 2:** Open your Terminal window or your operating system's equivalent command line.
**Step 3:** Run the following Python command:

    python word-guesser.py

**Step 4:** Enjoy the game!

## File Structure
***word-guesser.py***
All essential game running functions are stored here; run this file using the Python command line to play
***clean-words.py***
Used to clean the words list from ***word.txt***, which is saved as ***words-cleaned.txt***. Cleaning parameters include only using words with alphabetic characters and word lengths between 8 and 15 characters, inclusive.
***words.txt***
Raw list of words taken from [here](https://github.com/dwyl/english-words). Includes English words of all sizes and character compositions.
***words-cleaned.txt***
Words list cleaned using the functions of ***clean-words.py***.
***flowchart.txt*** and ***flowchart.png***
Diagram description of the flow of input for the game. Made using ***flowchart.fun***.

## Important Functions of *word_guesser.py*
**run_game()**: Runs the game for the user. This function allows the player to play the game multiple times while keeping score. This function is implicitly called by ***word_guesser.py***.
**play(hidden_word)**: Holds all of the essential implementation of game for Word Guesser. *hidden_word* is the string of the word that the player is trying to guess. See *flowchart.txt* for game logic flow.
**get_known_letters()**: Used by **play()** to show what characters have been revealed in the game. All other letters are replaced by underscores.
**get_words_list()**: Get a list of all the words that are potential choices for the player to guess to.
