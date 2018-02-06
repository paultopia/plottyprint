import matplotlib.pyplot as plt
import numpy as np
from utils import remove_chart_junk


def boxplot(variables,
            labels,
            title="",
            numticks=3,
            labelsize=12,
            size=(10, 10),):
    arrays = [np.sort(np.array(x)) for x in variables]

    fig = plt.figure(figsize=size)
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(title + '\n',
                 fontsize=labelsize * 1.25,
                 fontname='Lato')

    ax = remove_chart_junk(ax, numticks, labelsize)

    bp = ax.boxplot(arrays, notch=True, sym="k.", labels=labels)
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color="black")
    return fig
