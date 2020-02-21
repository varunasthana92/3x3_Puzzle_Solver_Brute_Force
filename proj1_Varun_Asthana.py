import numpy as np

# defining all possible action set for each position of blank tile
def action(zeroPos):
    actions= {0: np.array([1,3]), 1: np.array([0,2,4]), 2: np.array([1,5]),
          3: np.array([0,4,6]), 4: np.array([1,3,5,7]), 5: np.array([2,4,8]),
          6: np.array([3,7]), 7: np.array([4,6,8]), 8: np.array([5,7]),
         }
    return actions[zeroPos]