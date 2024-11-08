import matplotlib
import numpy as np
import pandas as pd
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 48})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 8
ind = np.arange(N)  # the x locations for the groups
width = 0.25     # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
dummy = [96.4,77.1,78.9,89,88.3,93.2,92.5,91.6]
dummy_0 = [3, 0, 0]
dummy_1 = [5, 0, 0]
dummy_2 = [2, 0, 0]
# dummy2 = [95,96]

ax.bar(ind, dummy, width, color='grey', edgecolor='black')
# ax.bar(ind, dummy_0, width, color='white', hatch = '-', edgecolor='black', label = 'DAG creation overhead')
# ax.bar(ind, dummy_1, width, color = 'white', hatch = '//', edgecolor = 'black', bottom= dummy_0, label='Time and space multiplexing overhead')
# ax.bar(ind, dummy_2, width, color = 'white', hatch = '||', edgecolor = 'black', bottom = dummy_1, label = 'Overhead to minize GPU memory-CPU memory transfer')
# ax.bar(ind+width, dummy2, width, color='magenta', edgecolor='black', label='With retraining')

# ax.set_ylim(70, 101)
# ytickvalues = []
# for i in range(70, 101, 5):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=32)

ax.set_ylabel('Accuracy')
# ax.set_xlabel('Number of other datasets in combination')
ytickvalues = []

ax.set_ylim(75, 101)
ytickvalues = []
for i in range(75, 101, 5):
	ytickvalues.append(i)
plt.yticks(ytickvalues)
ax.set_yticklabels(["%d%%" % x for x in ytickvalues])

ax.set_xticks(ind)

xvalues = ["AdaInf", "/I", "/U", "/S", "/E", "/A", "/M1", "/M2"]
ax.set_xticklabels(xvalues)

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.01, box.width, box.height*0.95])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.45), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='48', ncol=1, handleheight=1.2, labelspacing=0.0, frameon=False)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()