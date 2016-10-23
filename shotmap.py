# -*- coding: utf-8 -*-
import numpy as np 
from scipy import signal, interpolate
from matplotlib import pylab as plt
import matplotlib.ticker as tick
from matplotlib.colors import LogNorm
from matplotlib.colors import LinearSegmentedColormap 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd (a, b)


def generate_cmap(colors):
    """自分で定義したカラーマップを返す"""
    values = range(len(colors))

    vmax = np.ceil(np.max(values))
    color_list = []
    for v, c in zip(values, colors):
        color_list.append( ( v/ vmax, c) )

    print("color_list : ", color_list)
    return LinearSegmentedColormap.from_list('custom_cmap', color_list)

def plot_shotmap(data, vmin, vmax):
    """ """
    y,x = data.shape
    print("data shape : ", data.shape)
    #Z = np.zeros((x+2, y+2))
    Z = np.zeros((y+2, x+2))
    #Z[1:y+1, 1:x+1] = data
    #Z[1:y+1, 1:x+1] = data
    Z[1:y+1, 1:x+1] = data
    #x = np.arange(x+3)
    #y = np.arange(y+3)
    x = np.arange(x+2)
    y = np.arange(y+2)

    X, Y = np.meshgrid(x, y)
    print(Z.shape)
    print(X.shape)
    print(Y.shape)

    val_gcd = gcd(len(x), len(y))
    print("gcd => ", gcd, " aspect ", len(x)//val_gcd, " : ", len(y)//val_gcd)
    #================================================================================
    # plt
    #================================================================================

    fig, ax = plt.subplots(figsize=(len(x), len(y)))

    #cm = generate_cmap(['#87CEEB', '#2E8B57', '#F4A460'])
    plt.pcolor(X, Y, Z, norm=LogNorm(), vmin= vmin, vmax= vmax)

    plt.gca().xaxis.set_minor_locator(tick.MultipleLocator(1))
    plt.gca().yaxis.set_minor_locator(tick.MultipleLocator(1))
    ax.set_xticks(x + 0.5, minor=False)
    ax.set_yticks(y + 0.5, minor=False)

    xtick = [" "] + list(x[1:-1]) + [" "]
    ytick = [" "] + list(y[1:-1]) + [" "]

    ax.set_xticklabels(xtick, minor=False)
    ax.set_yticklabels(ytick, minor=False)
    plt.grid(which = 'minor', color='black', linestyle='-')
    #plt.xlim([0, len(x)-1])
    #plt.ylim([0, len(y)-1])
    plt.colorbar()

    #testx = [0,1,1,0]
    #testy = [0,0,1,1]
    #plt.fill(testx,testy,color="y",alpha=1.0)
    #ax.set_aspect('equal')


    plt.show()


if __name__ == '__main__':
    wafer_x = 23 
    wafer_y = 18 
    x = np.arange(wafer_x+1)
    y = np.arange(wafer_y+1)
    #Z = np.zeros((wafer_x, wafer_y)) + 10 * 10**(5)
    Z = np.zeros((wafer_y, wafer_x)) + 10 * 10**(5)
    print("org Z : ", Z)
    #Z = np.zeros((wafer_y, wafer_x)) + 10 * 10**(5)
    plot_shotmap(Z, 10**(-14), 10**(-6))
