# Plottyprint

(TODO: convert this to reStructuredText, get image examples in, test a bit more, maybe tweak density option in hist and boxplot opts then pypi it up)

##The Goal

Make simple data visualizations in Python that are **easy**, **attractive**, and most importantly **appropriate for dead-tree printing** (like in academic journals, conference posters, or newspapers), with a bias toward greyscale in case color printing is expensive.

This very small library is targeted at the easiest 60% or so of plots that social scientists and student journalists and other light-to-moderate data users will want to produce. 

Right now, the amount of effort it takes to go from from no plots at all or really ugly plots to simple but attractive plots is *much* longer than the amount of effort from simple but attractive plots to really complex plots. This strikes me as unacceptable. If you want to produce a 4-d contour plot overlaid on a map of the world with color representing time, I can't help you. But if you want to produce a basic scatterplot, maybe with a least squares fit on top of it, and then slap it into your journal submission to impress the peer reviewers, I'm here for you. 

## The Challenges

1.  Default matplotlib plotting is ugly, and making attractive plots is difficult.

2.  There are many Python packages that make it easy create beautiful plots on top of matplotlib, such as [seaborn](https://seaborn.pydata.org), [bokeh](https://bokeh.pydata.org/en/latest/), and [plotly](https://plot.ly/python/).  However, they are built for web or interactive use, not for printing. They have lots of colors, default proportions appropriate for screen usage, and often interactive elements that don't make sense on paper.  While it's possibly to convince those libraries to make plots for print, it's a lot of work.  (If you want to do that, I recommend using the Python port of [ggplot](http://ggplot.yhathq.com). 

## The Plottyprint Solution

This very small library aims to provide a handful of basic and attractive printable plots that will work out of the box with sensible defaults for the most simple use cases.  Right now, it supplies three workhorse plots: 

1.  A **scatterplot** between two variables. By default, the scatterplot has a least squares line through it, and a confidence region around that line, but this is easy to turn off.

2.  A **histogram** of one variable. If you want to get really fancy to impress the peer reviewers, you can stick a kernel density estimator line on top of it. 

3.  A **boxplot** with the standard frills (whiskers, notches, all that good stuff). This one is kind of rudimentary, and I'd like to make it more attractive later.

This, obviously, represents the science communicator's basic toolkit for displaying the relationship between two variables, the shape of one variable, and the relationship between mean, interquartile range, and outliers for several variables, respectively.

Each of these elements is presented in high-contrast greyscale, and has all of matplotlib's default [chart junk](https://en.m.wikipedia.org/wiki/Chartjunk) ruthlessly ripped out. 

In this 0.1 release, there are only a handful of customization options, but over time I plan to add more plot types and add a bit more customization. Moreover, every plot returns a matplotlib figure, so if you know matplotlib you can always do your own customization after the fact. 

Here are some examples.  

Scatterplot, with fit line and confidence region. 

[IMAGE GOES HERE]

Histogram, no KDE estimator.

[IMAGE GOES HERE]

Histogram, with KDE estimator

[IMAGE GOES HERE]

Boxplot

[IMAGE GOES HERE]

## Installation

`pip install plottyprint` 

[BUT NOT YET, ON PYPI SOON]

## Usage

There are three functions, each corresponding to a plot.  Each takes one or more numpy arrays, or anything that can be cast into a numpy array with `np.array()` without going wrong (lists, Pandas `DataFrame` columns, etc.), plus some configuration, and returns a matplotlib `Figure` which you can save or modify to your heart's content. 

**scatterplot(x, y, title="", xlabel="", ylabel="", numticks=3, labelsize=15, dotsize=8, ylabel_wrapping=6, size=(10, 10), fit_line=True, confidence=True, alpha=0.05)**

x and y are, obviously,  your data.

title is, obviously, the title of the plot

xlabel and ylabel are, obviously, the labels for your data.

numticks are (wait for it) the number of ticks to show on each axis. For mysterious reasons, sometimes matplotlib likes to give you a little more or fewer than the number asked for, but at any rate the default is a nice small number that will show the scale of the data without overwhelming the reader with noise. 

labelsize is the size of the axis labels. The title will be scaled up a little from this.

dotsize is the size of the individual points in the plot.

ylabel_wrapping is the number of characters in the y label before it wraps to another line. (Making y labels attractive is a bit difficult.)

size is a tuple representing the size in inches

fit_line is a boolean representing whether or not to put a least squares line in the plot.

confidence is a boolean representing whether or not to put a confidence interval around the least squares line. Obviously, this won't do anything if you don't have a least squares line in there.

alpha is the width of your confidence interval. The default represents the good old fashioned 95% interval.

**histogram(variable, bins="auto", density = False, title="", numticks=5, labelsize=15, size=(10, 10), add_kde=False, kernel_param = 0.4, show_n = True)**

variable is, obviously, your variable.

bins can be a number of bins, or "auto" to let numpy come up with something for you

density you probably don't need to mess with (and I may remove it in a future version), but if you set it for true you'll get a histogram in the form of a probability density. See [the matplot lib docs](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hist.html) for more. This strikes me as a bad choice for most basic use cases: usually you'll want counts.

add_kde controls whether you want to slap a kernel density estimator plot on top of your histogram. If you do want to do this, it'll change the scale of the histogram: it will become density rather than counts, and, since the y label on a density histogram is anywhere between confusing and outright deceptive, it gets removed.  Call me paternalistic.

kernel_param is a parameter that goes into the kernel density estimator. Scipy does [a lot of fancy math](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html) with this, but you can think of it as kind of similar to the bandwidth parameter in the [R kde function](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/density.html).  For practical purposes, larger numers should produce smoother plots, but it's probably worth playing with interactively. 

show_n is a boolean determining whether to have a y axis with the number of observations per bin or not. As noted above, this is automatically turned off if you add a kernel density estimator. 

Everything else is the same as in `scatterplot`.

**boxplot(variables, labels, title="", numticks=3, labelsize=12, size=(10, 10))**

Everything here is the same as in `scatterplot` except that variables is a list of, well, variables (numpy arrays etc.), and labels is a list of labels.  You can put as many variables in here as you can squeeze in.

## Possible Glitches

I created this with a recent Python 3 release.  I haven't tested it in Python 2, but I think it should work. If it breaks in Python 2 it's probably because I did something silly like rely on modern division or the latest fancy string formatting, file an issue and I'll fix it. 

Fonts are a problem with matplotlib, and if you run into font difficulties then see [this blog post](http://andresabino.com/2015/08/18/fonts-and-matplotlib/) for a fix. 