Mastermind Game
Student: Nguyen Hoang Minh Truong
Course: Programming I - Semester Project
Date: December 24, 2025
What is This?
This is my semester project for Programming I. I made a Mastermind game where you try to guess a secret code made of 4 colors. The computer gives you hints after each guess to help you figure it out.

Files in This Project
mastermind.py - This is the main game file (190 lines of code)
test_mastermind.py - Tests to make sure my code works
USER_GUIDE.docx - Instructions on how to play the game
DEVELOPER_DOCS.docx - Explains how I wrote the code
README.md - This file

How to Run My Game
1.Make sure you have Python installed
2.Put all the files in one folder
3.Open command prompt or terminal
4.Type: python mastermind.py
5.The game window should open

How to Run the Tests
Type: python test_mastermind.py
If everything works, it should say all tests passed.



How to Play
1.Click on the color buttons to pick 4 colors
2.Click Submit to guess
3.The game tells you: 
oBlack = right color in right spot
oWhite = right color but wrong spot
4.Keep guessing until you get it or run out of tries (you get 10 tries)
5.You can click "Get Hint" if you're stuck

What I Learned
Use random to generate a secret code
Make a GUI with tkinter
Write functions with parameters
Use lists to store guesses
Calculate feedback using loops
Test my code with unit tests

What Works
You can play the full game
The feedback is accurate
The hint system suggests valid guesses
You can play again after winning or losing
All my tests pass

Things I Could Add Later
Different difficulty levels (more colors or positions)
A timer
High scores
Better graphics
Sound effects


How My Code is Organized
The code has these main parts:
1.Some constants at the top (COLORS, CODE_LENGTH, etc.)
2.Variables to store game state (secret_code, guess_history, etc.)
3.Functions for game logic (generate_secret_code, calculate_feedback, get_hint)
4.Functions for the GUI buttons (submit_guess, clear_guess, etc.)
5.GUI setup at the bottom (makes the window and buttons)
Check DEVELOPER_DOCS.txt for more details.
