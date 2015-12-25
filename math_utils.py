import numpy as np
import matplotlib.pyplot as plt


class Vector():
    """
    This class stores a vector
    """
    def __init__(self, x, y):
        self.tuple = np.array([x, y])

    def plot(self, title):
        #todo make axis lines appear
        soa = np.array([[0, 0, self.tuple[0], self.tuple[1]]])
        X, Y, U, V = zip(*soa)

        fig = plt.figure()
        # Add title to the plot
        fig.suptitle(title, fontsize=15, fontweight="bold")
        fig.canvas.set_window_title(title)

        ax = plt.gca()

        #  grid lines
        ax.grid(True, which="both")

        # Show x and y axes
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()

        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        # Give the line arrowheads for the tip of the vector
        ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)

        # Set bounds of plot
        if abs(self.tuple[0]) >= abs(self.tuple[1]):
            limit = abs(self.tuple[0]) + 1
        else:
            limit = abs(self.tuple[1]) + 1
        ax.set_xlim([-limit, limit])
        ax.set_ylim([-limit, limit])

        plt.draw()
        plt.show()

class Matrix():
    """
    This class stores a matrix
    """
    def __init__(self, a, b, c, d):
        self.matrix = np.matrix([
                [a, b],
                [c, d]
            ])

    def printMatrix(self):
        print(self.matrix)


