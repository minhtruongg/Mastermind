Developer Documentation
What Problem Am I Solving?
I need to make a Mastermind game where:
The computer picks a secret code with 4 colors
The player tries to guess it
After each guess, the game tells the player how close they were
The player has 10 tries to guess it right

How My Code Works
The Main Parts
1.Variables at the top - These store the game colors, how many tries you get, etc.
2.Functions for game logic - These do the actual game stuff like checking if your guess is right
3.Functions for the buttons - These make the buttons work when you click them
4.GUI setup at the bottom - This makes the window and all the buttons show up

Important Functions
generate_secret_code()
This makes a random code with 4 colors
It uses a for loop and random.choice() to pick colors
calculate_feedback(guess, secret)
This is the most important function
It counts how many colors are in the right spot (black pegs)
It counts how many colors are right but in wrong spot (white pegs)
First I count the black pegs by checking if guess[i] == secret[i]
Then I count how many times each color appears in both lists
Finally I subtract the black pegs from the total to get white pegs
get_hint()
This suggests a guess that might work
If you haven't guessed yet, it just gives random colors
If you have guessed before, it tries 100 random codes and checks if they match your previous feedback
It's not perfect but it works pretty well.  
submit_guess()
This runs when you click Submit
It checks if you picked 4 colors
Calls calculate_feedback() to see how good your guess was
Adds your guess to the history
Checks if you won or lost
How the Data Flows
1.Game starts and makes a secret code
2.You click colors to build your guess
3.When you have 4 colors, you click Submit
4.The game calculates black and white pegs
5.Your guess gets added to the history list
6.If you got all 4 right, you win
7.If you used all 10 guesses, you lose
8.Otherwise you guess again


How to Test It
Run test_mastermind.py to test if the functions work right. I made tests for:
Does the secret code have 4 colors?
Does feedback work when you guess perfectly?
Does feedback work when nothing matches?
Does feedback work with duplicate colors?
All my tests pass so the game logic works correctly.
