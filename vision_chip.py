# -*- coding: utf-8 -*-
import numpy as np 
from scipy import signal, interpolate
from matplotlib import pylab as plt
import matplotlib.ticker as tick
from matplotlib.colors import LogNorm
from matplotlib.colors import LinearSegmentedColormap

def generate_cmap(colors):
    """自分で定義したカラーマップを返す"""
    values = range(len(colors))

    vmax = np.ceil(np.max(values))
    color_list = []
    for v, c in zip(values, colors):
        color_list.append( ( v/ vmax, c) )

    print("color_list : ", color_list)
    return LinearSegmentedColormap.from_list('custom_cmap', color_list)

if __name__ == '__main__':
    N = 10 
    x = np.arange(N+1)
    y = np.arange(N+1)
    Z = np.zeros((N, N))# + 10 * 10**(5)

    Z[2,3] = 1000 * 10 **(-7)
    Z[3,4] = 34234 * 10 ** (-4)

    #Z = np.log(Z)

    X, Y = np.meshgrid(x, y)
    print(Z)


    #================================================================================
    # plt
    #================================================================================
    fig, ax = plt.subplots()

    #cm = generate_cmap(['#87CEEB', '#2E8B57', '#F4A460'])
    #plt.pcolor(X, Y, Z)
    #plt.pcolor(X, Y, Z, norm=LogNorm(vmin= Z.min(), vmax=Z.max()), cmap='PuBu_r')
    #plt.pcolor(X, Y, Z, norm=LogNorm(vmin= Z.min(), vmax=Z.max()))
    #plt.pcolor(X, Y, Z, norm=LogNorm(), cmap = cm, vmin=-10, vmax=10**10)
    plt.pcolor(X, Y, Z, norm=LogNorm(), vmin= 10**(-14), vmax=10**(14))
    #plt.pcolor(X, Y, Z, cmap = cm, vmin=-10, vmax=10**10)
    #plt.pcolor(X, Y, Z, cmap = cm, vmin=0)
    #plt.pcolor(X, Y, Z, vmin=0)

    #plt.gca().xaxis.set_major_locator(tick.MultipleLocator(1)) #plt.gca().yaxis.set_major_locator(tick.MultipleLocator(1))

    plt.gca().xaxis.set_minor_locator(tick.MultipleLocator(1))
    plt.gca().yaxis.set_minor_locator(tick.MultipleLocator(1))

    ax.set_xticks(np.arange(N) + 0.5, minor=False)
    ax.set_yticks(np.arange(N) + 0.5, minor=False)
    #ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    #ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    xtick = [" "] + (list(range(N-1)))
    print(xtick)
    #ax.set_xticklabels([" "].append(list(range(N-1))), minor=False)
    ax.set_xticklabels(xtick, minor=False)
    ax.set_yticklabels(range(N), minor=False)

    #plt.grid(which='both')
    plt.grid(which = 'minor', color='black', linestyle='-')
    plt.xlim([0, N])
    plt.ylim([0, N])
    plt.plot([1, 1], [2, N-2], 'g-', lw=2)
    plt.plot([1, 2], [N-2, N-2], 'g-', lw=2)
    plt.plot([1, 2], [2, 2], 'g-', lw=2)
    plt.plot([2, 2], [2, 1], 'g-', lw=2)
    plt.plot([2, 2], [N-2, N-1], 'g-', lw=2)
    plt.plot([2, N-2], [1, 1], 'g-', lw=2)
    plt.plot([2, N-2], [N-1, N-1], 'g-', lw=2)
    plt.plot([N-2, N-2], [N-1, N-2], 'g-', lw=2)
    plt.plot([N-1, N-2], [N-2, N-2], 'g-', lw=2)
    plt.plot([N-2, N-2], [1, 2], 'g-', lw=2)
    plt.plot([N-1, N-2], [2, 2], 'g-', lw=2)
    plt.plot([N-1, N-1], [2, N-2], 'g-', lw=2)
    plt.colorbar()

    # fill
    testx = [0,1,1,0]
    testy = [0,0,N,N]
    plt.fill(testx,testy,color="y",alpha=1.0)

    plt.show()
