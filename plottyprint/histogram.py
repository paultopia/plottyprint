import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from utils import remove_chart_junk

def histogram(variable,
              bins="auto",
              density=False,
              title="",
              numticks=5,
              labelsize=15,
              size=(10, 10),
              add_kde=False,
              kernel_param=0.4,
              show_n=True):
    var = np.sort(np.array(variable))

    fig = plt.figure(figsize=size)
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(title + '\n',
                 fontsize=labelsize * 1.25,
                 fontname='Lato')

    ax = remove_chart_junk(ax, numticks, labelsize)

    if show_n:
        ax.set_xlabel("n = " + str(var.size),
                      fontsize=labelsize,
                      labelpad=labelsize * 0.7,
                      color=(0.15, 0.15, 0.15),
                      fontname='Lato')
    if add_kde:
        density = True
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

    return fig