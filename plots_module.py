import matplotlib.pyplot as plt
import numpy as np

#wybrane = {"wodor":Amplitudy(8.9e-6), "azot":Amplitudy(17.76e-6), "tlen":Amplitudy(20.64e-6), "fluor":Amplitudy(23.16e-6), "chlor":Amplitudy(13.4e-6)}

def make_amplitude_plot(wybrane):
    colors = ["g", "b", "y", "r", "c"]
    j = 0
    for names,values in wybrane.items():
        plt.plot(values[0], values[1], color=colors[j], lw = 1, label=names)
        j += 1

    plt.xlabel('t')
    plt.ylabel('A')
    plt.legend()
    plt.show()

def make_energy_plot(wybrane):
    colors = ["g", "b", "y", "r", "c"]
    j = 0
    for names,values in wybrane.items():
        plt.plot(values[0], values[1], color=colors[j], lw = 1, label=names)
        j += 1

    plt.xlabel('t')
    plt.ylabel('A')
    plt.legend()
    plt.show()

