import numpy as np
import scipy as scipy


class Game:
    def __init__(self, density, nbColumns, nbRows):
        # 2D Matrix of every cell
        self.cells = None

        # Number of neighbors of every cell
        self.neighborCounts = None

        # Comparison matrix for the 2d convolution
        self.comparisonMatrix = np.ones((3, 3))
        # The center cell is set to zero so the current cell doesn't count itself as a neighbor
        self.comparisonMatrix[1][1] = 0

        self.buildCells(density, nbColumns, nbRows)

    def buildCells(self, density, nbColumns, nbRows):
        self.cells = np.random.choice([1, 0], nbColumns*nbRows, p=[density/100, 1-density/100]).reshape(nbColumns, nbRows)

    def clearCells(self, nbColumns, nbRows):
        self.cells = np.zeros((nbColumns, nbRows))

    def compute(self):
        self.neighborCounts = scipy.signal.convolve2d(self.cells, self.comparisonMatrix, mode='same')

    def cycle(self):
        # Compute neighbors for every cell
        self.compute()

        # Iterate through the whole board
        for x in range(len(self.neighborCounts)):
            for y in range(len(self.neighborCounts[0])):

                # Rule 1: if a cell is living and is surrounded by 2 or 3 living cells, it survives
                if self.cells[x][y] == 1:
                    if self.neighborCounts[x][y] == 2 or self.neighborCounts[x][y] == 3:
                        pass
                    else:
                        self.cells[x][y] = 0

                # Rule 2: if a cell is dead and is surrounded by 3 living cells, it comes back to life
                elif self.cells[x][y] == 0:
                    if self.neighborCounts[x][y] == 3:
                        self.cells[x][y] = 1

                # If no rule is respected, the cell is dead upon the next iteration

