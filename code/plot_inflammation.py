import glob
import numpy
import matplotlib.pyplot

def generate_graph(data):
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    avg_axes = fig.add_subplot(1, 3, 1)
    max_axes = fig.add_subplot(1, 3, 2)
    min_axes = fig.add_subplot(1, 3, 3)

    avg_axes.set_ylabel('average')
    avg_axes.plot(numpy.mean(data, axis=0))

    max_axes.set_ylabel('max')
    max_axes.plot(numpy.max(data, axis=0))

    min_axes.set_ylabel('min')
    min_axes.plot(numpy.min(data, axis=0))

    fig.tight_layout()

    return fig

filenames = sorted(glob.glob('../data/inflammation*.csv'))
for f in filenames:
    data = numpy.loadtxt(fname=f, delimiter=',')

    figure = generate_graph(data)

    figure.savefig(f + '.png')
