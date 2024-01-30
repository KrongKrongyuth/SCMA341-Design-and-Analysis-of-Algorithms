
"""
First lecture of SCMA341 Design and Analysis of Algorithms.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RunProgram():
    """
    RunProgram() class --> Contain basic function
    """
    def __init__(self):
        pass

    def run(self):
        """
        run(self) --> print("Running...")
        """
        return print("Running...")
    def end(self):
        """
        end(self) --> print("Ending...")
        """
        return print("Ending...")
    def line_plot(self, data, function = None):
        """
        line_plot(data) --> Build the line plot from data.
        """
        plt.figure(figsize = (8,4), dpi = 200)
        plt.title(label = "Line Plot")
        sns.lineplot(x = range(len(data)), y = data, label = "Main Data")
        plt.xlabel(xlabel = "Number of round")
        plt.ylabel(ylabel = "Time in second")
        if function :
            sns.lineplot(x = range(len(data)), y = function, label = "Function Data")
        plt.show()


if __name__ == "__main__" :
    start = time.time()

    main = RunProgram()
    duration = []

    main.run()
    for k in range(len(np.random.randint(0,101,10000))):
        duration.append(time.time() - start)
    main.line_plot(duration, function = [0.0000001 * x + 0.0002 for x in range(len(duration))])
    main.end()
