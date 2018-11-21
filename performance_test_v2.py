# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: PERFORMANCE TEST
# Authors: Liuqing Chen, Feng Shi, 
#          and Isaac Engel (13th September 2017)
# Last updated: 2nd December 2017
# ####################################################

from main import Tetris
import utils
import timeit
from copy import deepcopy

# Example target shape
#target = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]  # NOTE: in your test, you may not use this example.

# Uncomment the following line to generate a random target shape
target = utils.generate_target(width=500, height=500, density=0.8)  # NOTE: it is recommended to keep density below 0.8

solution = Tetris(deepcopy(target))

valid, missing, excess, error_pieces = utils.check_solution(target, solution)  # checks if the solution is valid

if not valid:

    print("The solution is not valid!")

else:  # if the solution is valid, test time performance and accuracy

    # TIME PERFORMANCE
    # There will be three different values of the parameter 'target' with increasing complexity in real test.

    time_set = timeit.timeit('Tetris({})'.format(target), 'from main import Tetris', number=1)

    if time_set > 600:

        print("Time is over 10 minutes! The solution is not valid")

    else:

        print("Time performance")
        print("----------------")
        print("The running time was {:.5f} seconds.\n".format(time_set))

        # ACCURACY

        print("Accuracy")
        print("--------")

        if len(error_pieces) == 0:
            print('All pieces are labelled with correct shapeID and pieceID.')
        else:
            print('WARNING: {} pieces have a wrong shapeID. They are labelled in image of the solution, and they are: {}.'
                  .format(len(error_pieces), error_pieces))

        total_blocks = sum([sum(row) for row in target])
        total_blocks_solution = total_blocks - missing + excess

        print("The number of blocks in the TARGET is {:.0f}.".format(total_blocks))
        print("The number of blocks in the SOLUTION is {:.0f}.".format(total_blocks_solution))
        print("There are {} MISSING blocks ({:.4f}%) and {} EXCESS blocks ({:.4f}%).\n".format
              (missing, 100 * missing / total_blocks, excess, 100 * excess / total_blocks))

        # VISUALISATION
        # NOTE: for large sizes (e.g., 100x100), visualisation will take several seconds and might not be that helpful.
        # Feel free to comment out the following lines if you don't need the visual feedback.

        print("Displaying solution...")
        utils.visualisation(target, solution)
