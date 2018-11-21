import numpy as np

def Tetris(target):
    
    # I do appologise to whoever is looking at this for the length of the code. I did re-write this with recursion, however the running time increased. 
    # As a result I have submitted this code, since it performs better. Each part of this code comes in blocks of 19. 
    # The first part evaluates the options for each value of i and j, the second picks the best one and puts it in, the third goes over the task again to optomise, as explained in that section
    
    
    """Code Thirteen"""
    
    target_row = len(target)
    target_col = len(target[0]) # Getting the height and width of the target
    
    solution = np.zeros((target_row,target_col), dtype='i,i').tolist() # creating a solution of the same size as the target
    
    count = 1 # starting the count at 0, this increases as more pieces are put in. This is essentually the Piece_ID
    
    shape_ID_1_score = 0 # Setting all of the scores to 0 for evaluation in part 2
    shape_ID_2_score = 0
    shape_ID_3_score = 0
    shape_ID_4_score = 0
    shape_ID_5_score = 0
    shape_ID_6_score = 0
    shape_ID_7_score = 0
    shape_ID_8_score = 0
    shape_ID_9_score = 0
    shape_ID_10_score = 0
    shape_ID_11_score = 0
    shape_ID_12_score = 0
    shape_ID_13_score = 0
    shape_ID_14_score = 0
    shape_ID_15_score = 0
    shape_ID_16_score = 0
    shape_ID_17_score = 0
    shape_ID_18_score = 0
    shape_ID_19_score = 0
    
    shape_edge_1_number = 8 # Setting the 'number of edges score' to evaluate the shapes evenly, since shape 1 can only get a score of 8 when others get 10
    shape_edge_other_number = 10
    
    shape_edge_1_score = 0 # Setting the values of the edge scores to 0 
    shape_edge_2_score = 0
    shape_edge_3_score = 0
    shape_edge_4_score = 0
    shape_edge_5_score = 0
    shape_edge_6_score = 0
    shape_edge_7_score = 0
    shape_edge_8_score = 0
    shape_edge_9_score = 0
    shape_edge_10_score = 0
    shape_edge_11_score = 0
    shape_edge_12_score = 0
    shape_edge_13_score = 0
    shape_edge_14_score = 0
    shape_edge_15_score = 0
    shape_edge_16_score = 0
    shape_edge_17_score = 0
    shape_edge_18_score = 0
    shape_edge_19_score = 0
    
    """Section One"""
    
    for i  in range(target_row):
        for j in range(target_col): # A nested for loop to run through each value of i and j moving across and then down the target and solution
            # Shape One
            if i < target_row - 1 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):       # These lines check, firstly, that the shape will be in indexing range and secondly that the shape fits within the task and solution
                            if i == 0:                                                  # If i or j are equal to 0, then the piece is at the edge and we can assume that all of the pieces at this edge are touching and add 2 to the score   
                                shape_edge_1_score += 2 
                            else:
                                if i > 0:                                               # If i is not equal to 0 we have to evaluate the above positions and add one for each one
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0): 
                                        shape_edge_1_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_1_score += 1
                            if j == 0:                                                  # We do the same here for the j values
                                shape_edge_1_score += 2
                            else:
                                if j > 0:                   
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_1_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_1_score += 1
                            if i == target_row - 1:                                     # This is similar to the values of i and j against 0 , except this time I am checking them against the other edges, when i and j are at their maximum
                                shape_edge_1_score += 2
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                        shape_edge_1_score += 1
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_1_score += 1
                            if j == target_col - 1 :
                                shape_edge_1_score += 2
                            else:
                                if j < target_col - 2:
                                    if target[i][j+2] != 1 or solution[i][j+2] != (0,0):
                                        shape_edge_1_score += 1 
                                    if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                        shape_edge_1_score += 1 
            else:
                shape_edge_1_score = 0 # If the shape cannot fit it outputs a score of 0
                
            # Shape Two
            if i < target_row - 3 and target[i][j] == 1 and solution[i][j] == (0,0):      # This is the same as the code for shape one, except adjusted to be for shape two.          
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):                     # All of the below shapes have the same code untill we get to section two at line 846
                    if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                        if target[i+3][j] == 1 and solution[i+3][j] == (0,0):
                            if i == 0:
                                shape_edge_2_score += 1
                            elif i > 0:
                                if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                    shape_edge_2_score += 1
                            if j == 0:
                                shape_edge_2_score += 4 
                            else: 
                                if j > 0: 
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_2_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_2_score += 1
                                    if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                        shape_edge_2_score += 1
                                    if target[i+3][j-1] != 1 or solution[i+3][j-1] != (0,0):
                                        shape_edge_2_score += 1
                            if i == target_row - 3:
                                shape_edge_2_score += 1
                            elif i < target_row - 4:
                                if target[i+4][j] != 1 or solution[i+4][j] != (0,0):
                                    shape_edge_2_score += 1
                            if j == target_col - 1:
                                shape_edge_2_score += 4
                            else:
                                if j < target_col - 1: 
                                    if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                        shape_edge_2_score += 1
                                    if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                        shape_edge_2_score += 1
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_2_score += 1
                                    if target[i+3][j+1] != 1 or solution[i+3][j+1] != (0,0):
                                        shape_edge_2_score += 1
            else:
                shape_edge_2_score = 0
                
            # Shape Three
            if j < target_col - 3 and target[i][j] == 1 and solution[i][j] == (0,0):                
                if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                    if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                        if target[i][j+3] == 1 and solution[i][j+3] == (0,0):
                            if i == 0:
                                shape_edge_3_score += 4
                            else:
                                if i > 0: 
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_3_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_3_score += 1
                                    if target[i-1][j+2] != 1 or solution[i-1][j+2] != (0,0):
                                        shape_edge_3_score += 1
                                    if target[i-1][j+3] != 1 or solution[i-1][j+3] != (0,0):
                                        shape_edge_3_score += 1                                
                            if j == 0:
                                shape_edge_3_score += 1
                            elif j > 0:
                                if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                    shape_edge_3_score != 1
                            if i == target_row - 1:
                                shape_edge_3_score += 4
                            else:
                                if i < target_row - 1: 
                                    if target[i+1][j] != 1 or solution[i+1][j] != (0,0):
                                        shape_edge_3_score += 1
                                    if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                        shape_edge_3_score += 1
                                    if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                        shape_edge_3_score += 1
                                    if target[i+1][j+3] != 1 or solution[i+1][j+3] != (0,0):
                                        shape_edge_3_score += 1
                            if j == target_col - 3:
                                shape_edge_3_score += 1
                            else:
                                if j < target_col - 4:
                                    if target[i][j+4] != 1 or solution[i][j+4] != (0,0):
                                        shape_edge_3_score += 1 
            else:
                shape_edge_3_score = 0   
                
            # Shape Four
            if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):                
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                        if target[i+2][j+1] == 1 and solution[i+2][j+1] == (0,0):
                            if i == 0:
                                shape_edge_4_score += 1
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_4_score += 1
                            if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                shape_edge_4_score += 2
                            if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                shape_edge_4_score += 1
                            if j == 0:
                                shape_edge_4_score += 3
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_4_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_4_score += 1
                                    if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                        shape_edge_4_score += 1
                            if i == target_row - 2:
                                shape_edge_4_score += 2
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j] != 1 or solution[i+3][j] != (0,0):
                                        shape_edge_4_score += 1
                                    if target[i+3][j+1] != 1 or solution[i+3][j+1] != (0,0):
                                        shape_edge_4_score += 1
                            if j == target_col - 1:
                                shape_edge_4_score += 1
                            else:
                                if j < target_col - 2:
                                    if target[i+2][j+2] != 1 or solution[i+2][j+2] != (0,0):
                                        shape_edge_4_score += 1
            else:
                shape_edge_4_score = 0 
                
            # Shape Five
            if i < target_row - 1 and j > 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                        if target[i+1][j-2] == 1 and solution[i+1][j-2] == (0,0):
                            if i == 0:
                                shape_edge_5_score += 1
                            else:
                                if i > 0: 
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_5_score += 1
                            if j == 2:
                                shape_edge_5_score += 1
                            else:
                                if j > 2:
                                    if target[i+1][j-3] != 1 or solution[i+1][j-3] != (0,0):
                                        shape_edge_5_score += 1
                            if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                shape_edge_5_score += 2
                            if target[i][j-2] != 1 or solution[i][j-2] != (0,0):
                                shape_edge_5_score += 1
                            if i == target_row - 2:
                                shape_edge_5_score += 3
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j-2] != 1 or solution[i+2][j-2] != (0,0):
                                        shape_edge_5_score += 1 
                                    if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                        shape_edge_5_score += 1 
                                    if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                        shape_edge_5_score += 1
                            if j == target_col:
                                shape_edge_5_score += 2
                            else: 
                                if j < target_col - 1:
                                    if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                        shape_edge_5_score += 1
                                    if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                        shape_edge_5_score += 1
            else:
                shape_edge_5_score = 0 
                
            # Shape Six
            if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                    if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                        if target[i+2][j+1] == 1 and solution[i+2][j+1] == (0,0):
                            if target[i+1][j] != 1 or solution[i+1][j] != (0,0):
                                shape_edge_6_score += 2
                            if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                shape_edge_6_score += 1
                            if i == 0:
                                shape_edge_6_score += 2
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_6_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_6_score += 1
                            if j == 0:
                                shape_edge_6_score += 1
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_6_score += 1 
                            if i == target_row - 3:
                                shape_edge_6_score += 1
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j+1] != 1 or solution[i+3][j+1] != (0,0):
                                        shape_edge_6_score += 1
                            if j == target_col - 2:
                                shape_edge_6_score += 3
                                if j < target_col - 2:
                                    if target[i][j+2] != 1 or solution[i][j+2] != (0,0):
                                        shape_edge_6_score += 1
                                    if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                        shape_edge_6_score += 1
                                    if target[i+2][j+2] != 1 or solution[i+2][j+2] != (0,0):
                                        shape_edge_6_score += 1
            else:
                shape_edge_6_score = 0  
                
                
            # Shape Seven
            if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):                
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):            
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                            if i == 0: 
                                shape_edge_7_score += 3 
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_7_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_7_score += 1
                                    if target[i-1][j+2] != 1 or solution[i-1][j+2] != (0,0):
                                        shape_edge_7_score += 1
                            if j == 0:
                                shape_edge_7_score += 2
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_7_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_7_score += 1
                            if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                shape_edge_7_score += 2
                            if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                shape_edge_7_score += 1
                            if i == target_row - 1:
                                shape_edge_7_score += 1
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                        shape_edge_7_score += 1
                            if j == target_col - 2:
                                shape_edge_7_score += 1
                            else:
                                if j < target_col - 3:
                                    if target[i][j+3] != 1 or solution[i][j+3] != (0,0):
                                        shape_edge_7_score += 1
            else:
                shape_edge_7_score = 0 
                
                
            # Shape Eight
            if i < target_row - 2 and j > 0 and target[i][j] == 1 and solution[i][j] == (0,0):                
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):            
                    if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                        if target[i+2][j-1] == 1 and solution[i+2][j-1] == (0,0):
                            if i == 0:
                                shape_edge_8_score += 1
                            elif i > 0:
                                if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                    shape_edge_8_score += 1
                            if j == 0:
                                shape_edge_8_score += 1
                            elif j > 0:
                                if target[i+2][j-2] != 1 or solution[i+2][j-2] != (0,0):
                                    shape_edge_8_score += 1
                            if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                shape_edge_8_score += 1
                            if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                shape_edge_8_score += 2
                            if i == target_row - 2:
                                shape_edge_8_score += 2
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j-1] != 1 or solution[i+3][j-1] != (0,0):
                                        shape_edge_8_score += 1
                                    if target[i+3][j] != 1 or solution[i+3][j] != (0,0):
                                        shape_edge_8_score += 1
                            if j == target_col - 1:
                                shape_edge_8_score += 3
                            else:
                                if j < target_col - 1:
                                    if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                        shape_edge_8_score += 1
                                    if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                        shape_edge_8_score += 1
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_8_score += 1 
            else:
                shape_edge_8_score = 0
                
            # Shape Nine
            if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                    if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                        if target[i+1][j+2] == 1 and solution[i+1][j+2] == (0,0):
                            if i == 0:
                                shape_edge_9_score += 3
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_9_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_9_score += 1
                                    if target[i-1][j+2] != 1 or solution[i-1][j+2] != (0,0):
                                        shape_edge_9_score += 1
                            if j == 0:
                                shape_edge_9_score += 1
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_9_score += 1
                            if target[i+1][j] != 1 or solution[i+1][j] != (0,0):
                                shape_edge_9_score += 1 
                            if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                shape_edge_9_score += 2
                            if i == target_row - 1:
                                shape_edge_9_score += 1
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j+2] != 1 or solution[i+2][j+2] != (0,0):
                                        shape_edge_9_score += 1
                            if j == target_col - 2:
                                shape_edge_9_score += 2
                            else:
                                if j < target_col - 3:
                                    if target[i][j+3] != 1 or solution[i][j+3] != (0,0):
                                        shape_edge_9_score += 1
                                    if target[i+1][j+3] != 1 or solution[i+1][j+3] != (0,0):
                                        shape_edge_9_score += 1
            else:
                shape_edge_9_score = 0 
                
            # Shape Ten
            if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):                
                if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                            if i == 0:
                                shape_edge_10_score += 2
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_10_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_10_score += 1
                            if j == 0:
                                shape_edge_10_score += 3
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_10_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_10_score += 1
                                    if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                        shape_edge_10_score += 1
                            if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                shape_edge_10_score += 2
                            if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                shape_edge_10_score += 1
                            if i == target_row - 2:
                                shape_edge_10_score += 1
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j] or solution[i+3][j] != (0,0):
                                        shape_edge_10_score += 1
                            if j == target_col - 1:
                                shape_edge_10_score += 1
                            else:
                                if j < target_col - 2:
                                    if target[i][j+2] != 1 or solution[i][j+2] != (0,0):
                                        shape_edge_10_score += 1
            else:
                shape_edge_10_score = 0
                
            # Shape Eleven
            if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                        if target[i+1][j+2] == 1 and solution[i+1][j+2] == (0,0):
                            if i == 0:
                                shape_edge_11_score += 1
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_11_score += 1
                            if j == 0:
                                shape_edge_11_score += 2
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_11_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_11_score += 1
                            if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                shape_edge_11_score += 2
                            if target[i][j+2] != 1 or solution[i][j+2] != (0,0):
                                shape_edge_11_score += 1
                            if i == target_row - 1:
                                shape_edge_11_score += 3
                            else:
                                if i < target_row - 2: 
                                    if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                        shape_edge_11_score += 1
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_11_score += 1
                                    if target[i+2][j+2] != 1 or solution[i+2][j+2] != (0,0):
                                        shape_edge_11_score += 1
                            if j == target_col - 2:
                                shape_edge_11_score += 1
                            else:
                                if j < target_col - 3: 
                                    if target[i+1][j+3] != 1 or solution[i+1][j+3] != (0,0):
                                        shape_edge_11_score += 1
            else:
                shape_edge_11_score = 0 
                
            # Shape Twelve
            if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):                
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                        if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                            if i == 0:
                                shape_edge_12_score += 1
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_12_score += 1
                            if j == 0:
                                shape_edge_12_score += 3
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_12_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_12_score += 1
                                    if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                        shape_edge_12_score += 1
                            if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                shape_edge_12_score += 2
                            if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                shape_edge_12_score += 2
                            if i == target_row - 2:
                                shape_edge_12_score += 1
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j] != 1 or solution[i+3][j] != (0,0):
                                        shape_edge_12_score += 1
                            if j == target_col - 1:
                                shape_edge_12_score += 1
                            else:
                                if j < target_col - 2:
                                    if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                        shape_edge_12_score += 1
            else:
                shape_edge_12_score = 0 
                
            # Shape Thirteen
            if i < target_row - 1 and 0 < j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                        if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                            if i == 0:
                                shape_edge_13_score += 1
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_13_score += 1
                            if j == 0:
                                shape_edge_13_score += 1
                            else:
                                if j > 0:
                                    if target[i+1][j-2] != 1 or solution[i+1][j-2] != (0,0):
                                        shape_edge_13_score += 1
                            if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                shape_edge_13_score += 2
                            if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                shape_edge_13_score += 2
                            if i == target_row - 1:
                                shape_edge_13_score += 3
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                        shape_edge_13_score += 1
                                    if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                        shape_edge_13_score += 1
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_13_score += 1
                            if j == target_col - 1:
                                shape_edge_13_score += 1
                            else:
                                if j < target_col - 2:
                                    if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                        shape_edge_13_score += 1
            else:
                shape_edge_13_score = 0  
                
            # Shape Fourteen
            if i < target_row - 2 and j > 0 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                        if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                            if i == 0:
                                shape_edge_14_score += 1
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_14_score += 1
                            if j == 1:
                                shape_edge_14_score += 1
                            else:
                                if j > 1:
                                    if target[i+1][j-2] != 1 or solution[i+1][j-2] != (0,0):
                                        shape_edge_14_score += 1
                            if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                shape_edge_14_score += 2
                            if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                shape_edge_14_score += 2
                            if i == target_row - 2:
                                shape_edge_14_score += 1
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j] != 1 or solution[i+3][j] != (0,0):
                                        shape_edge_14_score += 1
                            if j == target_col:
                                shape_edge_14_score += 3
                            else:
                                if j < target_col - 1:
                                    if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                        shape_edge_14_score += 1
                                    if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                        shape_edge_14_score += 1
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_14_score += 1
                                
            else:
                shape_edge_14_score = 0 
                
            # Shape Fithteen 
            if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                    if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                        if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                            if i == 0:
                                shape_edge_15_score += 3
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_15_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_15_score += 1
                                    if target[i-1][j+2] != 1 or solution[i-1][j+2] != (0,0):
                                        shape_edge_15_score += 1
                            if j == 0:
                                shape_edge_15_score += 1
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_15_score += 1
                            if target[i+1][j] != 1 or solution[i+1][j] != (0,0):
                                shape_edge_15_score += 2
                            if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                shape_edge_15_score += 2
                            if i == target_row - 1:
                                shape_edge_15_score += 1
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_15_score += 1
                            if j == target_col - 2:
                                shape_edge_15_score += 1
                            else:
                                if j < target_col - 3:
                                    if target[i][j+3] != 1 or solution[i][j+3] != (0,0):
                                        shape_edge_15_score += 1
            else:
                shape_edge_15_score = 0  
                
            # Shape Sixteen
            if i < target_row - 1 and 0 < j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                            if i == 0:
                                shape_edge_16_score += 2
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_16_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_16_score += 1    
                            if j == 1:
                                shape_edge_16_score += 1
                            else:
                                if j > 1:
                                    if target[i+1][j-2] != 1 or solution[i+1][j-2] != (0,0):
                                        shape_edge_16_score += 1 
                            if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                shape_edge_16_score += 2
                            if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                shape_edge_16_score += 2
                            if j == target_col - 1:
                                shape_edge_16_score += 1
                            else:
                                if j < target_col - 2:
                                    if target[i][j+2] != 1 or solution[i][j+2] != (0,0):
                                        shape_edge_16_score += 1
                            if i == target_row - 1:
                                shape_edge_16_score += 2
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j-1] != 1 or solution[i+2][j-1] != (0,0):
                                        shape_edge_16_score += 1
                                    if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                        shape_edge_16_score += 1
            else:
                shape_edge_16_score = 0  
                
            # Shape Seventeen
            if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                        if target[i+2][j+1] == 1 and solution[i+2][j+1] == (0,0):
                            if i == 0:
                                shape_edge_17_score += 1
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_17_score += 1
                            if j == 0:
                                shape_edge_17_score += 2
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_17_score += 1
                                    if target[i+1][j-1] != 1 or solution[i+1][j-1] != (0,0):
                                        shape_edge_17_score += 1
                            if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                shape_edge_17_score += 2
                            if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                shape_edge_17_score += 2
                            if i == target_row - 3:
                                shape_edge_17_score += 1
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j+1] != 1 or solution[i+3][j+1] != (0,0):
                                        shape_edge_17_score += 1
                            if j == target_col - 2:
                                shape_edge_17_score += 2
                            else:
                                if j < target_col - 2:
                                    if target[i+1][j+2] != 1 or solution[i+1][j+2] != (0,0):
                                        shape_edge_17_score += 1
                                    if target[i+2][j+2] != 1 or solution[i+2][j+2] != (0,0):
                                        shape_edge_17_score += 1
            else:
                shape_edge_17_score = 0

            # Shape Eighteen
            if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                    if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                        if target[i+1][j+2] == 1 and solution[i+1][j+2] == (0,0):
                            if i == 0:
                                shape_edge_18_score += 2
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_18_score += 1
                                    if target[i-1][j+1] != 1 or solution[i-1][j+1] != (0,0):
                                        shape_edge_18_score += 1
                            if j == 0:
                                shape_edge_18_score += 1
                            else:
                                if j > 0:
                                    if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                        shape_edge_18_score += 1
                            if target[i][j+2] != 1 or solution[i][j+2] != (0,0):
                                shape_edge_18_score += 2
                            if target[i+1][j] != 1 or solution[i+1][j] != (0,0):
                                shape_edge_18_score += 2
                            if i == target_row - 1:
                                shape_edge_18_score += 2
                            else:
                                if i < target_row - 2:
                                    if target[i+2][j+1] != 1 or solution[i+2][j+1] != (0,0):
                                        shape_edge_18_score += 1
                                    if target[i+2][j+2] != 1 or solution[i+2][j+2] != (0,0):
                                        shape_edge_18_score += 1
                            if j == target_col - 2:
                                shape_edge_18_score += 1
                            else:
                                if j < target_col - 3:
                                    if target[i+1][j+3] != 1 or solution[i+1][j+3] != (0,0):
                                        shape_edge_18_score += 1
            else:
                shape_edge_18_score = 0  
                
            # Shape Nineteen
            if i < target_row - 2 and 0 < j and target[i][j] == 1 and solution[i][j] == (0,0):
                if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                    if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                        if target[i+2][j-1] == 1 and solution[i+2][j-1] == (0,0):
                            if i == 0:
                                shape_edge_19_score += 1
                            else:
                                if i > 0:
                                    if target[i-1][j] != 1 or solution[i-1][j] != (0,0):
                                        shape_edge_19_score += 1
                            if target[i][j-1] != 1 or solution[i][j-1] != (0,0):
                                shape_edge_19_score += 2
                            if target[i+2][j] != 1 or solution[i+2][j] != (0,0):
                                shape_edge_19_score += 2
                            if j == 1:
                                shape_edge_19_score += 2
                            else:
                                if j > 1:
                                    if target[i+1][j-2] != 1 or solution[i+1][j-2] != (0,0):
                                        shape_edge_19_score += 1
                                    if target[i+2][j-2] != 1 or solution[i+2][j-2] != (0,0):
                                        shape_edge_19_score += 1
                            if i == target_row - 1:
                                shape_edge_19_score += 1
                            else:
                                if i < target_row - 3:
                                    if target[i+3][j-1] != 1 or solution[i+3][j-1] != (0,0):
                                        shape_edge_19_score += 1
                            if j == target_col:
                                shape_edge_19_score += 2
                            else:
                                if j < target_col - 1:
                                    if target[i][j+1] != 1 or solution[i][j+1] != (0,0):
                                        shape_edge_19_score += 1
                                    if target[i+1][j+1] != 1 or solution[i+1][j+1] != (0,0):
                                        shape_edge_19_score += 1
            else:
                shape_edge_19_score = 0

            """Section Two"""
            
            # This section of my code runs the same values of i and j, except it evaluates the scores and picks the best option

            shape_ID_1_score = shape_edge_1_number - shape_edge_1_score         # these lines are here to give the square equal chance, as mentioned above the square has 2 less possible sides so these 
            shape_ID_2_score = shape_edge_other_number - shape_edge_2_score     # remove that problem. The ideal value here is 0, since that means all sides are in contact, and in almost all places this
            shape_ID_3_score = shape_edge_other_number - shape_edge_3_score     # will be the case
            shape_ID_4_score = shape_edge_other_number - shape_edge_4_score
            shape_ID_5_score = shape_edge_other_number - shape_edge_5_score
            shape_ID_6_score = shape_edge_other_number - shape_edge_6_score
            shape_ID_7_score = shape_edge_other_number - shape_edge_7_score
            shape_ID_8_score = shape_edge_other_number - shape_edge_8_score
            shape_ID_9_score = shape_edge_other_number - shape_edge_9_score
            shape_ID_10_score = shape_edge_other_number - shape_edge_10_score
            shape_ID_11_score = shape_edge_other_number - shape_edge_11_score
            shape_ID_12_score = shape_edge_other_number - shape_edge_12_score
            shape_ID_13_score = shape_edge_other_number - shape_edge_13_score
            shape_ID_14_score = shape_edge_other_number - shape_edge_14_score
            shape_ID_15_score = shape_edge_other_number - shape_edge_15_score
            shape_ID_16_score = shape_edge_other_number - shape_edge_16_score
            shape_ID_17_score = shape_edge_other_number - shape_edge_17_score
            shape_ID_18_score = shape_edge_other_number - shape_edge_18_score
            shape_ID_19_score = shape_edge_other_number - shape_edge_19_score
            
            # Next i create a list of all of the shapes
            
            score_list = [shape_ID_1_score, shape_ID_2_score,  shape_ID_3_score,  shape_ID_4_score,  shape_ID_5_score,  shape_ID_6_score,  shape_ID_7_score,  shape_ID_8_score,  shape_ID_9_score,  shape_ID_10_score,  shape_ID_11_score,  shape_ID_12_score,  shape_ID_13_score,  shape_ID_14_score,  shape_ID_15_score,  shape_ID_16_score,  shape_ID_17_score,  shape_ID_18_score,  shape_ID_19_score]
            
            # the next line sorts the list
            
            score_list.sort()  
            
            if shape_ID_16_score == score_list[0]:      # This part of the code checks to see if the shape ID has the lowest score on the list, if it does it double checks that it fits and puts it in.
                if i < target_row - 1 and 0 < j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                            if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                                solution[i][j] = (16, count)        # These lines place the pieces, using the count
                                solution[i][j+1] = (16, count)
                                solution[i+1][j] = (16, count)
                                solution[i+1][j-1] = (16, count)
                                count += 1                          # After a piece is inserted the count increases
                 
            if shape_ID_17_score == score_list[0]:                  # Again, the next set of code is the same as that used above. The next section of code begins at line 1088
                if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                            if target[i+2][j+1] == 1 and solution[i+2][j+1] == (0,0):
                                solution[i][j] = (17, count)
                                solution[i+1][j] = (17, count)
                                solution[i+1][j+1] = (17, count)
                                solution[i+2][j+1] = (17, count)
                                count += 1 
                
            if shape_ID_18_score == score_list[0]: 
                if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                            if target[i+1][j+2] == 1 and solution[i+1][j+2] == (0,0):
                                solution[i][j] = (18, count)
                                solution[i][j+1] = (18, count)
                                solution[i+1][j+1] = (18, count)
                                solution[i+1][j+2] = (18, count)
                                count += 1 
                  
            if shape_ID_19_score == score_list[0]: 
                if i < target_row - 2 and 0 < j and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                            if target[i+2][j-1] == 1 and solution[i+2][j-1] == (0,0):
                                solution[i][j] = (19, count)
                                solution[i+1][j] = (19, count)
                                solution[i+1][j-1] = (19, count)
                                solution[i+2][j-1] = (19, count)
                                count += 1
                  
            if shape_ID_12_score == score_list[0]: 
                if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                            if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                                solution[i][j] = (12, count)
                                solution[i+1][j] = (12, count)
                                solution[i+1][j+1] = (12, count)
                                solution[i+2][j] = (12, count)
                                count += 1
                   
            if shape_ID_13_score == score_list[0]: 
                if i < target_row - 1 and 0 < j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                            if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                                solution[i][j] = (13, count)
                                solution[i+1][j] = (13, count)
                                solution[i+1][j+1] = (13, count)
                                solution[i+1][j-1] = (13, count)
                                count += 1
                
            if shape_ID_14_score == score_list[0]: 
                if i < target_row - 2 and j > 0 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                            if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                                solution[i][j] = (14, count)
                                solution[i+1][j] = (14, count)
                                solution[i+1][j-1] = (14, count)
                                solution[i+2][j] = (14, count)
                                count += 1
                
            if shape_ID_15_score == score_list[0]: 
                if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                            if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                                solution[i][j] = (15, count)
                                solution[i][j+1] = (15, count)
                                solution[i+1][j+1] = (15, count)
                                solution[i][j+2] = (15, count)
                                count += 1
                
            if shape_ID_4_score == score_list[0]: 
                if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                            if target[i+2][j+1] == 1 and solution[i+2][j+1] == (0,0):
                                solution[i][j] = (4, count)
                                solution[i+1][j] = (4, count)
                                solution[i+2][j] = (4, count)
                                solution[i+2][j+1] = (4, count)
                                count += 1
                   
            if shape_ID_5_score == score_list[0]: 
                if i < target_row - 1 and j > 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j-1] == 1 and solution[i+1][j-1] == (0,0):
                            if target[i+1][j-2] == 1 and solution[i+1][j-2] == (0,0):
                                solution[i][j] = (5, count)
                                solution[i+1][j] = (5, count)
                                solution[i+1][j-1] = (5, count)
                                solution[i+1][j-2] = (5, count)
                                count += 1
                
            if shape_ID_6_score == score_list[0]: 
                if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                            if target[i+2][j+1] == 1 and solution[i+2][j+1] == (0,0):
                                solution[i][j] = (6, count)
                                solution[i][j+1] = (6, count)
                                solution[i+1][j+1] = (6, count)
                                solution[i+2][j+1] = (6, count)
                                count += 1 
               
            if shape_ID_7_score == score_list[0]: 
                if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):            
                        if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                            if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                                solution[i][j] = (7, count)
                                solution[i+1][j] = (7, count)
                                solution[i][j+1] = (7, count)
                                solution[i][j+2] = (7, count)
                                count += 1
                   
            if shape_ID_8_score == score_list[0]: 
                if i < target_row - 2 and j > 0 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):            
                        if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                            if target[i+2][j-1] == 1 and solution[i+2][j-1] == (0,0):
                                solution[i][j] = (8, count)
                                solution[i+1][j] = (8, count)
                                solution[i+2][j] = (8, count)
                                solution[i+2][j-1] = (8, count)
                                count += 1
                     
            if shape_ID_9_score == score_list[0]: 
                if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                            if target[i+1][j+2] == 1 and solution[i+1][j+2] == (0,0):
                                solution[i][j] = (9, count)
                                solution[i][j+1] = (9, count)
                                solution[i][j+2] = (9, count)
                                solution[i+1][j+2] = (9, count)
                                count += 1
                     
            if shape_ID_10_score == score_list[0]: 
                if i < target_row - 2 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                            if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                                solution[i][j] = (10, count)
                                solution[i][j+1] = (10, count)
                                solution[i+1][j] = (10, count)
                                solution[i+2][j] = (10, count)
                                count += 1
               
            if shape_ID_11_score == score_list[0]: 
                if i < target_row - 1 and j < target_col - 2 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):
                            if target[i+1][j+2] == 1 and solution[i+1][j+2] == (0,0):
                                solution[i][j] = (11, count)
                                solution[i+1][j] = (11, count)
                                solution[i+1][j+1] = (11, count)
                                solution[i+1][j+2] = (11, count)
                                count += 1
                  
            if shape_ID_2_score == score_list[0]:                 
                if i < target_row - 3 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):            
                        if target[i+2][j] == 1 and solution[i+2][j] == (0,0):
                            if target[i+3][j] == 1 and solution[i+3][j] == (0,0):                
                                solution[i][j] = (2, count)
                                solution[i+1][j] = (2, count)
                                solution[i+2][j] = (2, count)
                                solution[i+3][j] = (2, count)
                                count += 1

            if shape_ID_3_score == score_list[0]: 
                if j < target_col - 3 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                        if target[i][j+2] == 1 and solution[i][j+2] == (0,0):
                            if target[i][j+3] == 1 and solution[i][j+3] == (0,0):
                                solution[i][j] = (3, count)
                                solution[i][j+1] = (3, count)
                                solution[i][j+2] = (3, count)
                                solution[i][j+3] = (3, count)
                                count += 1

            if shape_ID_1_score == score_list[0]:                
                if i < target_row - 1 and j < target_col - 1 and target[i][j] == 1 and solution[i][j] == (0,0):
                    if target[i+1][j] == 1 and solution[i+1][j] == (0,0):
                        if target[i][j+1] == 1 and solution[i][j+1] == (0,0):
                            if target[i+1][j+1] == 1 and solution[i+1][j+1] == (0,0):            
                                solution[i][j] = (1, count)
                                solution[i+1][j] = (1, count)
                                solution[i][j+1] = (1, count)
                                solution[i+1][j+1] = (1, count)
                                count += 1
                         
            shape_edge_1_score = 0      # These lines of code set the scores back to 0 after evaluation
            shape_edge_2_score = 0
            shape_edge_3_score = 0
            shape_edge_4_score = 0
            shape_edge_5_score = 0
            shape_edge_6_score = 0
            shape_edge_7_score = 0
            shape_edge_8_score = 0
            shape_edge_9_score = 0
            shape_edge_10_score = 0
            shape_edge_11_score = 0
            shape_edge_12_score = 0
            shape_edge_13_score = 0
            shape_edge_14_score = 0
            shape_edge_15_score = 0
            shape_edge_16_score = 0
            shape_edge_17_score = 0
            shape_edge_18_score = 0
            shape_edge_19_score = 0
            
    for i in range(target_row):         # Here we run a second nested for loop to run through the code again
        for j in range(target_col):
            shape_1_three = 0           # These set the new scores to 0 
            shape_2_three = 0
            shape_3_three = 0
            shape_4_three = 0
            shape_5_three = 0
            shape_6_three = 0
            shape_7_three = 0
            shape_8_three = 0
            shape_9_three = 0
            shape_10_three = 0
            shape_11_three = 0
            shape_12_three = 0
            shape_13_three = 0
            shape_14_three = 0
            shape_15_three = 0
            shape_16_three = 0
            shape_17_three = 0
            shape_18_three = 0
            shape_19_three = 0
            
            """Section Three"""
            
            # This section looks for areas of three and then fills them. This gives 2 wrong squares instead of 4 and optomises my accuracy. This again, is a greedy algorithm.
            
            if i < target_row - 1 and j < target_col - 1 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j+1] == (0,0): 
                # The above line of code checks that there is room in the solution for the shape
                if target[i][j] == 1:       # next the code checks for areas where this overlaps with the target and adds one to the score.
                    shape_1_three += 1
                if target[i+1][j] == 1:
                    shape_1_three += 1
                if target[i][j+1] == 1:
                    shape_1_three += 1
                if target[i+1][j+1] == 1:
                    shape_1_three += 1 
                if shape_1_three >= 3:      # If the score is high enough, or three, it adds the shape as in the previous section
                    solution[i][j] = (1, count)
                    solution[i+1][j] = (1, count)
                    solution[i][j+1] = (1, count)
                    solution[i+1][j+1] = (1, count)
                    count += 1
                    shape_1_three = 0 
                    
            # The below lines are again, the same as above
            
            if i < target_row - 3 and  solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0) and solution[i+3][j] == (0,0):
                if target[i][j] == 1:
                    shape_2_three += 1
                if target[i+1][j] == 1:
                    shape_2_three += 1
                if target[i+2][j] == 1:
                    shape_2_three += 1
                if target[i+3][j] == 1:
                    shape_2_three += 1
                if shape_2_three >= 3:
                    solution[i][j] = (2, count)
                    solution[i+1][j] = (2, count)
                    solution[i+2][j] = (2, count)
                    solution[i+3][j] = (2, count)
                    count += 1
                    shape_2_three = 0
                            
            if j < target_col - 3 and solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i][j+2] == (0,0) and solution[i][j+3] == (0,0):
                if target[i][j] == 1:
                    shape_3_three += 1
                if target[i][j+1] == 1:
                    shape_3_three += 1
                if target[i][j+2] == 1:
                    shape_3_three += 1
                if target[i][j+3] == 1:
                    shape_3_three += 1
                if shape_3_three >= 3:
                    solution[i][j] = (3, count)
                    solution[i][j+1] = (3, count)
                    solution[i][j+2] = (3, count)
                    solution[i][j+3] = (3, count)
                    count += 1 
                    shape_3_three = 0
                    
            if i < target_row - 2 and j < target_col - 1 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0) and solution[i+2][j+1] == (0,0):
                if target[i][j] == 1:
                    shape_4_three += 1
                if target[i+1][j] == 1:
                    shape_4_three += 1
                if target[i+2][j] == 1:
                    shape_4_three += 1
                if target[i+2][j+1] == 1:
                    shape_4_three += 1
                if shape_4_three >= 3:
                    solution[i][j] = (4, count)
                    solution[i+1][j] = (4, count)
                    solution[i+2][j] = (4, count)
                    solution[i+2][j+1] = (4, count)
                    count += 1
                    shape_4_three = 0
                    
            if i < target_row - 1 and j > 2 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+1][j-2] == (0,0):
                if target[i][j] == 1:
                    shape_5_three += 1
                if target[i+1][j] == 1:
                    shape_5_three += 1
                if target[i+1][j-1] == 1:
                    shape_5_three += 1
                if target[i+1][j-2] == 1:
                    shape_5_three += 1
                if shape_5_three >= 3:
                    solution[i][j] = (5, count)
                    solution[i+1][j] = (5, count)
                    solution[i+1][j-1] = (5, count)
                    solution[i+1][j-2] = (5, count)
                    count += 1
                    shape_5_three = 0
                    
            if i < target_row - 2 and j < target_col - 1 and solution[i+2][j+1] == (0,0) and solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j+1] == (0,0):
                if target[i][j] == 1:
                    shape_6_three += 1
                if target[i][j+1] == 1:
                    shape_6_three += 1
                if target[i+1][j+1] == 1:
                    shape_6_three += 1
                if target[i+2][j+1] == 1:
                    shape_6_three += 1
                if shape_6_three >= 3:
                    solution[i][j] = (6, count)
                    solution[i][j+1] = (6, count)
                    solution[i+1][j+1] = (6, count)
                    solution[i+2][j+1] = (6, count)
                    count += 1
                    shape_6_three = 0
                            
            if i < target_row - 1 and j < target_col - 2 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i][j+2] == (0,0):
                if target[i][j] == 1:
                    shape_7_three += 1
                if target[i+1][j] == 1:
                    shape_7_three += 1
                if target[i][j+1] == 1:
                    shape_7_three += 1
                if target[i][j+2] == 1:
                    shape_7_three += 1
                if shape_7_three >= 3:
                    solution[i][j] = (7, count)
                    solution[i+1][j] = (7, count)
                    solution[i][j+1] = (7, count)
                    solution[i][j+2] = (7, count)
                    count += 1
                    shape_7_three = 0
                            
            if i < target_row - 2 and j > 1 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0) and solution[i+2][j-1] == (0,0):
                if target[i][j] == 1:
                    shape_8_three += 1
                if target[i+1][j] == 1:  
                    shape_8_three += 1
                if target[i+2][j] == 1:
                    shape_8_three += 1
                if target[i+2][j-1] == 1:
                    shape_8_three += 1
                if shape_8_three >= 3:
                    solution[i][j] = (8, count)
                    solution[i+1][j] = (8, count)
                    solution[i+2][j] = (8, count)
                    solution[i+2][j-1] = (8, count)
                    count += 1
                    shape_8_three = 0
                            
            if i < target_row - 1 and j < target_col - 2 and solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i][j+2] == (0,0) and solution[i+1][j+2] == (0,0):
                if target[i][j] == 1:
                    shape_9_three += 1
                if target[i][j+1] == 1:
                    shape_9_three += 1
                if target[i][j+2] == 1:
                    shape_9_three += 1
                if target[i+1][j+2] == 1:
                    shape_9_three += 1
                if shape_9_three >= 3:
                    solution[i][j] = (9, count)
                    solution[i][j+1] = (9, count)
                    solution[i][j+2] = (9, count)
                    solution[i+1][j+2] = (9, count)
                    count += 1
                    shape_9_three = 0
                            
            if i < target_row - 2 and j < target_col - 1 and solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j] == (0,0) and solution[i+2][j] == (0,0):
                if target[i][j] == 1:
                    shape_10_three += 1
                if target[i][j+1] == 1:
                    shape_10_three += 1
                if target[i+1][j] == 1:
                    shape_10_three += 1
                if target[i+2][j] == 1:
                    shape_10_three += 1
                if shape_10_three >= 3:
                    solution[i][j] = (10, count)
                    solution[i][j+1] = (10, count)
                    solution[i+1][j] = (10, count)
                    solution[i+2][j] = (10, count)
                    count += 1
                    shape_10_three = 0
                            
            if i < target_row - 1 and j < target_col - 2 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+1][j+2] == (0,0):
                if target[i][j] == 1:
                    shape_11_three += 1
                if target[i+1][j] == 1:
                    shape_11_three += 1
                if target[i+1][j+1] == 1:
                    shape_11_three += 1
                if target[i+1][j+2] == 1:
                    shape_11_three += 1
                if shape_11_three >= 3:
                    solution[i][j] = (11, count)
                    solution[i+1][j] = (11, count)
                    solution[i+1][j+1] = (11, count)
                    solution[i+1][j+2] = (11, count)
                    count += 1
                    shape_11_three = 0
                            
            if i < target_row - 2 and j < target_col - 1 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+2][j] == (0,0):
                if target[i][j] == 1:
                    shape_12_three += 1
                if target[i+1][j] == 1:
                    shape_12_three += 1
                if target[i+1][j+1] == 1:
                    shape_12_three += 1
                if target[i+2][j] == 1:
                    shape_12_three += 1
                if shape_12_three >= 3:
                    solution[i][j] = (12, count)
                    solution[i+1][j] = (12, count)
                    solution[i+1][j+1] = (12, count)
                    solution[i+2][j] = (12, count)
                    count += 1
                    shape_12_three = 0
                            
            if i < target_row - 1 and 1 < j < target_col - 1 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+1][j-1] == (0,0):
                if target[i][j] == 1:
                    shape_13_three += 1
                if target[i+1][j] == 1:
                    shape_13_three += 1
                if target[i+1][j+1] == 1:
                    shape_13_three += 1
                if target[i+1][j-1] == 1:
                    shape_13_three += 1
                if shape_13_three >= 3:
                    solution[i][j] = (13, count)
                    solution[i+1][j] = (13, count)
                    solution[i+1][j+1] = (13, count)
                    solution[i+1][j-1] = (13, count)
                    count += 1
                    shape_13_three = 0
                            
            if i < target_row - 2 and j > 1 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+2][j] == (0,0):
                if target[i][j] == 1:
                    shape_14_three += 1
                if target[i+1][j] == 1:
                    shape_14_three += 1
                if target[i+1][j-1] == 1:
                    shape_14_three += 1
                if target[i+2][j] == 1:
                    shape_14_three += 1
                if shape_14_three >= 3:
                    solution[i][j] = (14, count)
                    solution[i+1][j] = (14, count)
                    solution[i+1][j-1] = (14, count)
                    solution[i+2][j] = (14, count)
                    count += 1
                    shape_14_three = 0
                            
            if i < target_row - 1 and j < target_col - 2 and solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i][j+2] == (0,0):
                if target[i][j] == 1:
                    shape_15_three += 1
                if target[i][j+1] == 1:
                    shape_15_three += 1
                if target[i+1][j+1] == 1:
                    shape_15_three += 1
                if target[i][j+2] == 1:
                    shape_15_three += 1
                if shape_15_three >= 3:
                    solution[i][j] = (15, count)
                    solution[i][j+1] = (15, count)
                    solution[i+1][j+1] = (15, count)
                    solution[i][j+2] = (15, count)
                    count += 1
                    shape_15_three = 0
                            
            if i < target_row - 1 and 1 < j < target_col - 1 and solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j-1] == (0,0):
                if target[i][j] == 1:
                    shape_16_three += 1
                if target[i][j+1] == 1:
                    shape_16_three += 1
                if target[i+1][j] == 1:
                    shape_16_three += 1
                if target[i+1][j-1] == 1:
                    shape_16_three += 1
                if shape_16_three >= 3:
                    solution[i][j] = (16, count)
                    solution[i][j+1] = (16, count)
                    solution[i+1][j] = (16, count)
                    solution[i+1][j-1] = (16, count)
                    count += 1
                    shape_16_three = 0
                            
            if i < target_row - 2 and j < target_col - 1 and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+2][j+1] == (0,0):
                if target[i][j] == 1:
                    shape_1_three += 1
                if target[i+1][j] == 1:
                    shape_17_three += 1
                if target[i+1][j+1] == 1:
                    shape_17_three += 1
                if target[i+2][j+1] == 1:
                    shape_17_three += 1
                if shape_17_three >= 3:
                    solution[i][j] = (17, count)
                    solution[i+1][j] = (17, count)
                    solution[i+1][j+1] = (17, count)
                    solution[i+2][j+1] = (17, count)
                    count += 1
                    shape_17_three = 0
                            
            if i < target_row - 1 and j < target_col - 2 and solution[i][j] == (0,0) and solution[i][j+1] == (0,0) and solution[i+1][j+1] == (0,0) and solution[i+1][j+2] == (0,0):
                if target[i][j] == 1:
                    shape_18_three += 1
                if target[i][j+1] == 1:
                    shape_18_three += 1
                if target[i+1][j+1] == 1:
                    shape_18_three += 1
                if target[i+1][j+2] == 1:
                    shape_18_three += 1
                if shape_18_three >= 3:
                    solution[i][j] = (18, count)
                    solution[i][j+1] = (18, count)
                    solution[i+1][j+1] = (18, count)
                    solution[i+1][j+2] = (18, count)
                    count += 1
                    shape_18_three = 0
                            
            if i < target_row - 2 and 1 < j and solution[i][j] == (0,0) and solution[i+1][j] == (0,0) and solution[i+1][j-1] == (0,0) and solution[i+2][j-1] == (0,0):
                if target[i][j] == 1:
                    shape_19_three += 1
                if target[i+1][j] == 1:
                    shape_19_three += 1
                if target[i+1][j-1] == 1:
                    shape_19_three += 1
                if target[i+2][j-1] == 1:
                    shape_19_three += 1
                if shape_19_three >= 3:
                            solution[i][j] = (19, count)
                            solution[i+1][j] = (19, count)
                            solution[i+1][j-1] = (19, count)
                            solution[i+2][j-1] = (19, count)
                            count += 1
                            shape_19_three = 0
                                         
    return solution # outputting the solution
    
