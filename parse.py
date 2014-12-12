import matplotlib.pyplot as plt
import pylab as pl
import subprocess

def get_positions(data, team_filter=None):
    x_positions = []
    y_positions = []
    for line in data:
        try:
            x, y, z, team, weapon = line.split(' ')
            if team_filter is None or team == team_filter:
                x_positions.append(float(x))
                y_positions.append(float(y))
        except ValueError as ex:
            print ex, "\non line:\n", line, "\n"
    return x_positions, y_positions

data = subprocess.Popen("./parse.sh", shell=True, stdout=subprocess.PIPE)
shot_data = []
for line in data.stdout.readlines():
    shot_data.append(line.rstrip())

x, y = get_positions(shot_data)
fig = pl.figure(figsize=(50, 50))
axes = fig.add_axes([0, 0, 1, 1])
axes.axis('off')
axes.hexbin(x, y, gridsize = (200,200), cmap=plt.cm.RdPu_r, mincnt=1)
plt.savefig('output.png')
