
import statistics
from matplotlib import pyplot as plt
import numpy as np
import random

from scipy.interpolate import make_interp_spline, BSpline

graph = []
input_path = "book.txt"


section_map = {"Interrogation": (1278, 1356, "yellow"), "Trial": (1540, 2011, "red")}


oldx = 5
def norm(x, min):
    global oldx

    if x < min:
        return oldx

    oldx = x
    return x


def build_graph():
    with open(input_path, 'r') as input_file:
        lines = input_file.read().replace('\n', ' ').replace('  ', ' ').replace('*\n', '').replace(';', '.').replace(':', '.').split('.')

        lengths = []

        graph = []

        sample_size = 400

        for i, line in enumerate(lines):
            words = line.strip().count(' ') + 1

            if words < 2:
                lengths.append(lengths[i - 1])
            else:
                lengths.append(words)

            print(i, line)
            '''
            if i > sample_size:
                graph.append(statistics.mean(lengths[i-sample_size:i]))
            '''

        #'''
        for i, line in enumerate(lines):

            if i - int(sample_size/2) > 0:
                graph.append(statistics.mean(lengths[i - int(sample_size/2): i + int(sample_size/2)]))
            #else:
                #graph.append(statistics.mean(lengths[0:int(sample_size/2)]))
        #'''



        #graph = np.array([norm(x, 5) for x in graph])

        graph = np.array(graph)

        '''
        X = np.arange(graph.shape[0])
    
        xnew = np.linspace(X.min(), X.max(), 300)  # 300 represents number of points to make between T.min and T.max
    
        spl = make_interp_spline(X, graph, k=1)  # BSpline object
        power_smooth = spl(xnew)
    
        plt.plot(xnew, power_smooth)
        plt.xticks(np.arange(10)*10)
        '''

        for section in section_map:
            tpl = section_map[section]
            plt.axvspan(tpl[0], tpl[1], color=tpl[2], alpha=0.4)
            plt.text((tpl[0] + tpl[1])/2 - len(section)*4, graph.max()+0.3, section)

        plt.locator_params(nbins=40)

        plt.xlabel("Sentence number")
        plt.ylabel("Words per sentence")

        plt.plot(np.arange(sample_size/2, len(graph) + sample_size/2), graph)

        plt.show()
