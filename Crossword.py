import random
import sys
import string
#Variable to hold the grid size.
GRIDSIZE=10
#Function to check whether the position chosen randomly is valid.
def canplaceWord(rowNumber,columnNumber,grid,dirX,dirY,word):
    for i in range(len(word)):
        #Checks if the word would go out of bounds if placed in that position
        if 0>rowNumber+dirY*i or rowNumber+dirY*i>=GRIDSIZE  or  0>columnNumber+dirX*i or columnNumber+dirX*i>=GRIDSIZE:
            return False
        #Checks if the position is occupied by another letter not part of the word
        if grid[rowNumber+dirY*i][columnNumber+dirX*i]!="" and grid[rowNumber+(dirY*i)][columnNumber+(dirX*i)]!=word[i]:
            return False
    return True
#Function to randomly put letters of each word in appropriate positions
def putWord(rowNumber,columnNumber,grid,dirX,dirY,word):
    for i,char in enumerate(word):
        grid[rowNumber+dirY*i][columnNumber+dirX*i]=char+"_"+"|"+"_"

def generate_word_search(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # WRITE YOUR CODE HERE
    #Initially fills the grid with empty strings
    grid=[["" for j in range(GRIDSIZE)] for i in range(GRIDSIZE)]
    #List to hold directions of the words
    directions=[
        (1,1),# Ascending-right diagonal
        (1,0),#Horizontal-right
        (0,1),#Vertical(top-bottom)
        (-1,-1),#Descending-left diagonal
        (-1,0),#Horizontal-left
        (0,-1),#Vertical(bottom-top)
        (1,-1),#Descending-right diagonal
        (-1,1),#Ascending-left diagonal
    ]
    for word in words:
        word=word.upper()
        if len(word)>GRIDSIZE:
            print(f"{word} is too large for grid")
        #Variable to keep track of whether word was placed in the grid.
        successful=False
        #Loop Tries up to 1000 different random positions for each word until it finds a valid one.
        for _ in range(1000):
            #Choosing directions
            dirX,dirY=random.choice(directions)
            #Choosing Positions
            rowNumber=random.randint(0,GRIDSIZE-1)
            columnNumber=random.randint(0,GRIDSIZE-1)
            #Checks Validity of position
            if canplaceWord(rowNumber,columnNumber,grid,dirX,dirY,word):
                putWord(rowNumber,columnNumber,grid,dirX,dirY,word)
                successful=True
                break
        if not successful:
            print(f"Could not form grid with {word} please try again with different word combinations")

    #Fills remaining empty cells with random letters
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=="":
                grid[i][j]=random.choice(string.ascii_uppercase)+"_"+"|"+"_"

    return grid




# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = generate_word_search(words)
        
        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
