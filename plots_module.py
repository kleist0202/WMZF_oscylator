import matplotlib.pyplot as plt
import numpy as np


def make_plot(wybrane_poloz, wybrane_ener):
    colors = ["g", "b", "y", "r", "c"]
    j = 0
    plt.subplot(211)
    plt.title("Wykres polozenia od czasu")
    plt.xlabel('t')
    plt.ylabel('x')
    for names,values in wybrane_poloz.items():
        plt.plot(values[0], values[1], color=colors[j], lw = 1, label=names)
        j += 1
    plt.legend()

    j = 0
    plt.subplot(212)
    plt.title("Wykres spadku energii calkowitej od czasu")
    plt.xlabel('t')
    plt.ylabel('E')
    for names,values in wybrane_ener.items():
        plt.plot(values[0], values[1], color=colors[j], lw = 1, label=names)
        j += 1
    plt.legend()

    plt.show()
