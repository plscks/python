# This is a test program, I am trying to see if I can adapt it to my
# Nexus Clash mapping project, anyways I lifted it from here:
# https://stackoverflow.com/questions/19586828/drawing-grid-pattern-in-matplotlib
#
# Onward to the show!
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np

N = 15
# make an empty data set
#data = np.ones((N, N)) * np.nan

data = np.chararray((N, N), itemsize=7)
data[:] = 'nan'
print(data)
data[0][1] = '#FF0033'
data[0][2] = '#BB22FF'
data[0][3] = '#00FF22'
data[1][4] = '#B4B4FF'

# fill in some fake data

# for j in range(3)[::-1]:
#     data[N//2 - j : N//2 + j +1, N//2 - j : N//2 + j +1] = j

# make a figure + axes

print('Whole data set:')
print(data)
print('This is how we select an individual position: data[0][2]')
print(data[0][2])
print('Here is another one: data[1][4]')
print(data[1][4])

# So what needs to happen is the data set needs to represent
# the coordinate system and the hex color code will be the data
# within. Then we need to figure out how it takes that map and
# applies color to the picture.

fig, ax = plt.subplots(1, 1, tight_layout=True)
# make color map
my_cmap = matplotlib.colors.ListedColormap(['r', 'g', 'b'])
# set the 'bad' values (nan) to be white and transparent
my_cmap.set_bad(color='k', alpha=1)
# draw the grid
for x in range(N + 1):
    ax.axhline(x, lw=2, color='w', zorder=5)
    ax.axvline(x, lw=2, color='w', zorder=5)
# draw the boxes
ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)

# turn off the axis labels
ax.axis('off')
plt.savefig('books_read.png')
