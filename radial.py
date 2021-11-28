"""Radial distribution functions for Hydrogen."""

import matplotlib.pyplot as plt
import numpy as np


def rad(n, l, x):
    """Radial part R(r).

    Args:
        n: Principal quantum number (1, 2, 3).
        l: Azimuthal quantum number (0, 1, 2).
        x: Distance from nucleus in terms of Bohr radius.
    """
    if (n == 1):
        if (l == 0):
            return 2 * np.exp(- x)
    
    elif (n == 2):
        if (l == 0):
            return (1 / np.sqrt(2)) * (1 - x / 2) * np.exp(- x / 2)
        elif (l == 1):
            return (1 / (2 * np.sqrt(6))) * x * np.exp(- x / 2)
    
    elif (n == 3):
        if (l == 0):
            return (2 / (3 * np.sqrt(3))) * (1 - 2 * x / 3 + 2 * (x ** 2) / 27) * np.exp(- x / 3)
        elif (l == 1):
            return (8 / (27 * np.sqrt(6))) * (1 - x / 6) * x * np.exp(- x / 3)
        elif (l == 2):
            return (4 / (81 * np.sqrt(30))) * (x ** 2) * np.exp(- x / 3)
    
    return 0


def r2rad2(n, l, x):
    """Radial probability density r²R²(r).

    Args:
        n: Principal quantum number (1, 2, 3).
        l: Azimuthal quantum number (0, 1, 2).
        x: Distance from nucleus in terms of Bohr radius.
    """
    return x * x * np.square(rad(n, l, x))


if __name__ == '__main__':
    for n in [1, 2, 3]:
        x_list = np.linspace(0, 5 * (n ** 2 - n + 4) / 2, 250 * (n ** 2 - n + 4))
        
        for l in range(n):
            plt.suptitle('Radial Distribution Functions for Hydrogen', fontsize = 14)

            rad_list = []
            r2rad2_list = []

            for x in x_list:
                rad_list.append(rad(n, l, x))
                r2rad2_list.append(r2rad2(n, l, x))
        
            plt.plot(x_list, rad_list, label = 'Radial Part')
            plt.plot(x_list, r2rad2_list, label = 'Radial Probability Density')
            plt.legend(loc = 'upper right')
        
            plt.xlabel('r/a', fontsize = 10)
            plt.xticks(np.arange(0, 5 * (n ** 2 - n + 4) / 2, step = 5))
            plt.title(f'n = {n}, l = {l}', fontsize = 10)
            plt.grid()
            plt.axhline(y = 0, color = 'k')
            plt.axvline(x = 0, color = 'k')

            plt.savefig(f'Radial Distributions\\n{n}-l{l}.png')
            plt.close()
