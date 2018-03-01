import matplotlib
def remove_chart_junk(axis, numticks, labelsize):

    # reduce ticks
    axis.locator_params(nbins=numticks)

    # remove unnecessary borders
    axis.spines['top'].set_visible(False)
    axis.spines['right'].set_visible(False)
    axis.spines['left'].set_color((0.1, 0.1, 0.1, 0.2))
    axis.spines['bottom'].set_color((0.1, 0.1, 0.1, 0.2))

    # prettify tick labels
    axis.tick_params(axis='both',
                     which='both',
                     length=0,
                     labelsize=labelsize,
                     pad=labelsize * 0.66,
                     labelcolor=(0.25, 0.25, 0.25))
    return axis

class PlottyFig(matplotlib.figure.Figure):
    def change_title(self, title):
        self._axstack.as_list()[0].set_title(title)

    def get_main_plot(self):
        return self._axstack.as_list()[0]
