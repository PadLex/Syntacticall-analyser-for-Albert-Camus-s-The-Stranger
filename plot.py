import statistics
from matplotlib import pyplot as plt
import numpy as np
import random

from scipy.interpolate import make_interp_spline, BSpline

input_path = "book.txt"

#section_map = {}
#section_map = {"Murder": (1151, 1215, "red"), "Prison": (1215, 1540, "purple"), "Trial": (1540, 2011, "blue")}
#section_map = {"Hot beach": (1151, 1199, "orange"), "Murder": (1199, 1215, "red"), "Lawyer": (1237, 1274, "purple"), "Interrogation": (1274, 1356, "blue")}
section_map = {"Hot beach": (2258, 2288, "green")}

oldx = 5


def norm(x, min):
    global oldx

    if x < min:
        return oldx

    oldx = x
    return x


def sentence_length(lines):
    lengths = []

    for i, line in enumerate(lines):
        words = line.strip().count(' ') + 1

        if words < 2:
            lengths.append(lengths[i - 1])
        else:
            lengths.append(words)

        print(i, line)

    return lengths


def mean(sample_size):
    def mean_func(raw):
        x, y = [], []

        for i in range(len(raw)):

            if i - int(sample_size / 2) > 0 and i + int(sample_size / 2) < len(raw):
                y.append(statistics.mean(raw[i - int(sample_size / 2): i + int(sample_size / 2)]))

        x = np.arange(sample_size / 2, len(y) + sample_size / 2)
        return x, y

    return mean_func


def median(sample_size):
    def median_func(raw):
        x, y = [], []

        for i in range(len(raw)):

            if i - int(sample_size / 2) > 0:
                y.append(statistics.median(raw[i - int(sample_size / 2): i + int(sample_size / 2)]))

        x = np.arange(sample_size / 2, len(y) + sample_size / 2)
        return x, y

    return median_func


def exponential_decay(alpha):
    def exponential_decay_func(raw):
        x, y = [], []

        for i in range(len(raw)):
            exp_average = 0

            for j in range(len(raw)):
                if i == j:
                    exp_average += raw[j]
                else:
                    exp_average += raw[j]/(abs(i-j)**alpha)

            y.append(exp_average)

        y = np.array(y)

        # Scale data approximation
        y *= statistics.mean(raw)/statistics.mean(y)

        x = np.arange(0, len(y))
        return x, y

    return exponential_decay_func


def build_graph(raw_data, moving_average):
    with open(input_path, 'r') as input_file:
        lines = input_file.read().replace('\n', ' ').replace('  ', ' ').replace(';', '.').replace(':', '.').split('.')

        raw = raw_data(lines)

        graph = np.array(moving_average(raw))

        for section in section_map:
            tpl = section_map[section]
            plt.axvspan(tpl[0], tpl[1], color=tpl[2], alpha=0.3)
            #plt.text((tpl[0] + tpl[1]) / 2 - len(section) * 4, graph.max() + 0.3, section)

        plt.locator_params(nbins=40)

        plt.xlabel("Sentence number")
        plt.ylabel("Words per sentence")

        plt.plot(graph[0], graph[1])




#build_graph(sentence_length, exponential_decay(0.9))
build_graph(sentence_length, mean(40))
#build_graph(sentence_length, median(40))

plt.show()