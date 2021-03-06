#Hell noes!!
import math
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

N = 70
# make an empty data set
data = np.ones((N, N)) * np.nan
# fill in some fake data
for j in range(3)[::-1]:
    data[N//2 - j : N//2 + j +1, N//2 - j : N//2 + j +1] = j
data[6][7] = 0
print(data)
# make a figure + axes
fig, ax = plt.subplots(1, 1, tight_layout=True)
# make color map
my_cmap = matplotlib.colors.ListedColormap(['r', 'g', 'b'])
# set the 'bad' values (nan) to be white and transparent
my_cmap.set_bad(color='w', alpha=0)
# draw the grid
for x in range(N + 1):
    ax.axhline(x, lw=2, color='k', zorder=5)
    ax.axvline(x, lw=2, color='k', zorder=5)
# draw the boxes
ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
# turn off the axis labels
ax.axis('off')

plt.savefig('books_read.png')
