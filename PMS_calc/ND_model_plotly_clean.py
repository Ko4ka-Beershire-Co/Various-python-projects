# When I forget the math behind this shit: MU( utorrent letter) = mode, median; SIGMA( apple) = standard dev


import numpy as np
import plotly.graph_objects as go
import plotly.express as plt
import scipy.stats as stats

# Cycle Distribution
mu, sigma, n = 28, 3, 100000
lower, upper = 21, 35

# Duration Distribution
d_mu, d_sigma, d_n = 5, 1, 100000
d_lower, d_upper = 2, 7


def create_array_cont():
    # Cycle Distribution
    mu, sigma, n = 28, 3, 100000
    lower, upper = 21, 35

    # Duration Distribution
    d_mu, d_sigma, d_n = 5, 1, 100000
    d_lower, d_upper = 2, 7

    def normal(x, mu, sigma):
        return (2. * np.pi * sigma ** 2.) ** -.5 * np.exp(-.5 * (x - mu) ** 2. / sigma ** 2.)

    # Cycle Array

    X = stats.truncnorm.rvs(
        (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=n)
    Y = normal(X, mu, sigma)

    # Plot: ND allied to Cycle will assume conventional form, even when truncated
    # fig = plt.scatter(x=X, y=Y)
    # fig.show()

    # Duration Array

    d_X = stats.truncnorm.rvs(
        (d_lower - d_mu) / d_sigma, (d_upper - d_mu) / d_sigma, loc=d_mu, scale=d_sigma, size=d_n)
    d_Y = normal(d_X, d_mu, d_sigma)

    # Plot: ND allied to Duration will not assume conventional form as MU has a +1 displacement
    # fig = plt.scatter(x=d_X, y=d_Y)
    # fig.show()

    Z = Y * d_Y

    return X, d_X, Z


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
            xaxis=dict(nticks=1, range=[lower, upper], ticks='outside',
                       tick0=lower, dtick=1, tickwidth=0.01),
            yaxis=dict(nticks=1, range=[d_lower, d_upper], ticks='outside',
                       tick0=d_lower, dtick=1, tickwidth=0.01),
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
