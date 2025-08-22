# CROSSWORD
Crossword puzzle in python
HOW IT WORKS:
-I first created the 2D grid using nested list
-Then I filled the nested list with empty strings to represent an empty grid
-Then using the random module I let the computer decide random positions  for the first letter of each word and direction the word should go in
-The using a function I created “canplaceWord” the computer decides whether the position is valid
Properties of a valid position
1Not occupied by another input word
2Can fit the entire word depending on the direction the word is going in
3 It can share letters with other words in the list
-Using another function I created “putWord” the program then add each letter of the word into the grid starting from the randomly selected starting position and goes in the randolmly selected direction.

How directions work in the program
-Going horizonatlly comes is caused by changing columns
-So in the program the starting column number is incremented by dirX*I where I is the index of the letter and the dirX is a number that can be (0,1,-1) and determines the direction.
- (0) means no horizontal movement
- (1) shifts the letter to the right
- ( -1) Shifts the letter to the left
For example if it is the third letter of the word and the direction is horizonatal to the right then it means the columnNumber must increase by two units
So columnNumber+1*2=columnNumber + 2
-So logic for vertical movement but I used dirY to represent the direction instead
-After the program finds valid positions for each word the remaining empty cells are filled with random letters completing the grid.
-If a word is longer than 10 it skips to the next word
-It displays a message if it cant find a valid position for a word in 1000 tries
-Combination of horizontal and vertical movements create diagonal movements 
