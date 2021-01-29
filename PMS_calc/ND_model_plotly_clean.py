# When I forget the math behind this shit: MU( utorrent letter) = mode, median; SIGMA( apple) = standard dev

import numpy as np
import plotly.graph_objects as go
import plotly.express as plt
import scipy.stats as stats


# Dist as class
class Process:

    def __init__(self, mu, sigma, n, lower, upper):
        self.mu = mu
        self.sigma = sigma
        self.n = n
        self.lower = lower
        self.upper = upper


# Cycle Distribution
Cycle = Process(28, 3, 100000, 21, 35)

# Duration Distribution
duration = Process(5, 1, 100000, 2, 7)


def scatter_plot(array, no1, no2):  # if needed
    fig = plt.scatter(x=array[no1], y=array[no2])
    fig.show()


def create_array_cont():
    def normal(x, mu, sigma):
        return (2. * np.pi * sigma ** 2.) ** -.5 * np.exp(-.5 * (x - mu) ** 2. / sigma ** 2.)

    # Cycle Array

    X = stats.truncnorm.rvs(
        (Cycle.lower - Cycle.mu) / Cycle.sigma, (Cycle.upper - Cycle.mu) / Cycle.sigma, loc=Cycle.mu, scale=Cycle.sigma,
        size=Cycle.n)
    Y = normal(X, Cycle.mu, Cycle.sigma)

    # Plot: ND allied to Cycle will assume conventional form, even when truncated
    # fig = plt.scatter(x=X, y=Y)
    # fig.show()

    # Duration Array

    d_X = stats.truncnorm.rvs(
        (duration.lower - duration.mu) / duration.sigma, (duration.upper - duration.mu) / duration.sigma,
        loc=duration.mu, scale=duration.sigma, size=duration.n)
    d_Y = normal(d_X, duration.mu, duration.sigma)

    # Plot: ND allied to Duration will not assume conventional form as MU has a +1 displacement

    Z = Y * d_Y

    return X, d_X, Z, d_Y, Y


def plot_cont(array):
    # X Y Z as 1D-array
    fig = go.Figure(data=[go.Mesh3d(x=array[0],
                                    y=array[1],
                                    z=array[2],
                                    opacity=0.5,
                                    color='rgba(186,26,26,1)'
                                    )])

    # Set axis range
    fig.update_layout(
        scene=dict(
            xaxis=dict(nticks=1, range=[Cycle.lower, Cycle.upper], ticks='outside',
                       tick0=Cycle.lower, dtick=1, tickwidth=0.01),
            yaxis=dict(nticks=1, range=[duration.lower, duration.upper], ticks='outside',
                       tick0=duration.lower, dtick=1, tickwidth=0.01),
            zaxis=dict(nticks=1, range=[0, 0.07], ticks='outside',
                       tick0=0, dtick=0.01, tickwidth=0.01), ), ),

    # Custom name
    fig.update_layout(scene=dict(
        xaxis_title='Cycle',
        yaxis_title='Duration',
        zaxis_title='Probability'),
        width=1980,
        margin=dict(r=20, b=10, l=10, t=10))

    fig.show()


plot_cont(create_array_cont())

#   scatter_plot(create_array_cont(), 0, 4)
#   scatter_plot(create_array_cont(), 1, 3)
