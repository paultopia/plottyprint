import matplotlib.pyplot as plt
import numpy as np
from .utils import remove_chart_junk, PlottyFig


def boxplot(variables,
            labels,
            title="",
            numticks=3,
            labelsize=14,
            size=(10, 10),
            font="Lato",
            notch=True):
    arrays = [np.sort(np.array(x)) for x in variables]

    fig = plt.figure(figsize=size, FigureClass=PlottyFig)
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(title + '\n',
                 fontsize=labelsize * 1.25,
                 fontname=font)

    ax = remove_chart_junk(ax, numticks, labelsize)

    bp = ax.boxplot(arrays, notch=notch, sym="k.", labels=labels)
    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color="black", linewidth=1.75)
    return fig
