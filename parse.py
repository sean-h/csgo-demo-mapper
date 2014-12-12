import matplotlib.pyplot as plt
import pylab as pl

def get_positions(data):
    x_positions = []
    y_positions = []
    for line in data:
        x, y, z, team, weapon = line.split(' ')
        x_positions.append(x)
        y_positions.append(y)
    return x_positions, y_positions

with open('shots.txt', 'r') as f:
    file_data = f.read()

lines = file_data.split('\n')
del lines[-1]

x, y = get_positions(lines)
fig = pl.figure(figsize=(50, 50))
axes = fig.add_axes([0, 0, 1, 1])
axes.axis('off')
axes.hexbin(x, y, gridsize = (200,200), cmap=plt.cm.RdPu_r, mincnt=1)
plt.savefig('output.png')
