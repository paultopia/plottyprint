import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from .utils import remove_chart_junk, PlottyFig

def histogram(variable,
              bins="auto",
              title="",
              numticks=5,
              labelsize=15,
              size=(10, 10),
              add_kde=False,
              kernel_param=0.4,
              show_n=True,
              font="Lato"):
    var = np.sort(np.array(variable))

    fig = plt.figure(figsize=size, FigureClass=PlottyFig)
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(title + '\n',
                 fontsize=labelsize * 1.25,
                 fontname=font)

    ax = remove_chart_junk(ax, numticks, labelsize)

    if add_kde:
        density = True
    else:
        density = False

    if show_n:
        ax.set_xlabel("n = " + str(var.size),
                      fontsize=labelsize,
                      labelpad=labelsize * 0.7,
                      color=(0.15, 0.15, 0.15),
                      fontname=font)

    ax.hist(var, bins=bins, density=density, lw=0)

    # fix bar colors
    bars = [x for x in ax.get_children() if type(x) is matplotlib.patches.Rectangle]
    for idx, bar in enumerate(bars):
        if idx % 2 == 0:
            bar.set_color((0.1, 0.1, 0.1, 0.3))
        else:
            bar.set_color((0.4, 0.4, 0.4, 0.3))
    bars[-1].set_color("white")

    if add_kde:
        ds = gaussian_kde(var)
        mx = np.max(var)
        mn = np.min(var)
        ls = np.linspace(mn, mx)
        ds.covariance_factor = lambda : kernel_param
        ds._compute_covariance()
        dy = ds(ls)
        ax.plot(ls, dy, color=(0.1, 0.1, 0.1, 0.8))
        ax.set_yticks([])
        ax.spines['left'].set_visible(False)

    return fig
