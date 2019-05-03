
import statistics
from matplotlib import pyplot as plt
import numpy as np

from scipy.interpolate import make_interp_spline, BSpline

graph = []
input_path = "book.txt"

oldx = 5
def norm(x, min):
    global oldx

    if x < min:
        return oldx

    oldx = x
    return x


with open(input_path, 'r') as input_file:
    pages = input_file.read().replace('\n', ' ').replace('  ', ' ').split('*')

    for page in pages:
        lines = page.replace(',', '.').split('.')

        lengths = []

        for line in lines:
            words = line.strip().count(' ') + 1

            lengths.append(words)
            #print(line, words)

        #print(lengths, statistics.mean(lengths))
        graph.append(statistics.mean(lengths))


    graph = np.array([norm(x, 5) for x in graph])

    X = np.arange(graph.shape[0])

    xnew = np.linspace(X.min(), X.max(), 300)  # 300 represents number of points to make between T.min and T.max

    spl = make_interp_spline(X, graph, k=1)  # BSpline object
    power_smooth = spl(xnew)

    plt.plot(xnew, power_smooth)
    plt.xticks(np.arange(10)*10)
    #plt.plot(graph)
    plt.show()
