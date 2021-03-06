
def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    column_played = set()
    size = 9
    for i in range(size):
        if isinstance(puzzle[i][column],int): #check if integer
            if puzzle[i][column]>0 and puzzle[i][column]<10: #check if integer is between 1 and 9
                if puzzle[i][column] in column_played:  #check if duplicate
                    print("Column {} not valid".format(column))
                    return
                else:
                    column_played.add(puzzle[i][column])
            else:
                print("Column {} not valid".format(column))
                return
        else:
            print("Column {} not valid".format(column))
            return

    print("Column {} valid".format(column)) #prints valid after passing all if statements

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    row_played = set()
    size = 9
    for i in range(size):
        if isinstance(puzzle[row][i],int):#check if integer
            if puzzle[row][i]>0 and puzzle[row][i]<10: #check if integer is between 1 and 9
                if puzzle[row][i] in row_played: #check if duplicate
                    print ("Row {} not valid".format(row))
                    return
                else:
                    row_played.add(puzzle[row][i])
            else:
                print("Row {} not valid".format(row))
                return
        else:
            print("Row {} not valid".format(row))
            return

    print("Row {} valid".format(row)) #prints valid after passing all if statements

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """        
    #index is used to run for loops for each corresponding subgrid
    #first number is where the column starts, second number is where column ends
    #third number is where the row starts, fourth number is where row ends
    index = [ [0, 3, 0, 3], #subgrid 1
              [3, 6, 0, 3], #subgrid 2
              [6, 9, 0, 3], #subgrid 3
              [0, 3, 3, 6], #..
              [3, 6, 3, 6],
              [6, 9, 3, 6],
              [0, 3, 6, 9],
              [3, 6, 6, 9],
              [6, 9, 6, 9]  #subgrid 9
            ]
    sub_played = set()

    for i in range(index[subgrid][2], index[subgrid][3]): #start from top row of the subgrid to bottom row
        for j in range(index[subgrid][0],index[subgrid][1]): #check each number in the row from left to right

            if isinstance(puzzle[i][j], int): #check if integer
                if puzzle[i][j]>0 and puzzle[i][j]<10: #check if integer is between 1 and 9
                    if puzzle[i][j] in sub_played: #check if duplicate
                        print("Subgrid {} not valid".format(subgrid))
                        return

                    else:
                        sub_played.add(puzzle[i][j])
                else: 
                    print("Subgrid {} not valid".format(subgrid))
                    return
            else:
                print("Subgrid {} not valid".format(subgrid))
                return

    print("Subgrid {} valid".format(subgrid)) #prints valid after passing all if statements

if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 ,1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9 ,1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9 ,1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5]
            ]

    test3 = [ [12, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [25, "A", 5, 4, 7, 3, 9, 1, 67]
            ]
    
    testcase = test3   #modify here for other testcases
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        checkColumn(testcase, col)
    for row in range(SIZE):  #checking all rows
        checkRow(testcase, row)
    for subgrid in range(SIZE):   #checking all subgrids
        checkSubgrid(testcase, subgrid)