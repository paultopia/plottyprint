import matplotlib.pyplot as plt
import numpy as np
from .utils import remove_chart_junk, PlottyFig


def timeseries(in_dates,
               events,
               labels=["", ""],
               title="",
               numticks=3,
               labelsize=12,
               size=(10, 10),
               font="Lato"):
    fig = plt.figure(figsize=size, FigureClass=PlottyFig)
    ax = fig.add_subplot(1, 1, 1)
    numticks = 5

    ax.set_title(title + '\n',
                 fontsize=labelsize * 1.25,
                 fontname=font)

    ax = remove_chart_junk(ax, numticks, labelsize)

    dates = np.array(in_dates)
    dates_sorted = (np.sort(dates))
    event1 = np.array(events[0])[np.argsort(dates)]
    p1 = ax.plot(dates_sorted, event1, 'k-', label=labels[0])
    if len(events) > 1:
        event2 = np.array(events[1])[np.argsort(dates)]
        p2 = ax.plot(dates_sorted, event2, color=(0.6, 0.6, 0.6), linestyle='-', label=labels[1])
        leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, framealpha=0)
        leg.get_texts()[1].set_color((0.4, 0.4, 0.4))
    return fig
