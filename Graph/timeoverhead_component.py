import matplotlib
import numpy as np
import pandas as pd
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 38})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.2     # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
dummy = [12,15, 18]
dummy_0 = [3, 0, 0]
dummy_1 = [5, 0, 0]
dummy_2 = [2, 0, 0]
# dummy2 = [95,96]

ax.bar(ind, dummy, width, color='white', edgecolor='black')
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

ax.set_ylabel('Time overhead (ms)')
# ax.set_xlabel('Number of other datasets in combination')
ax.set_xticks(ind)

xvalues = ["AdaInf/d", "AdaInf/ST", "AdaInf/TM"]
ax.set_xticklabels(xvalues, fontsize=38)

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0, box.y0 + box.height*0.01, box.width, box.height*0.75])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.45), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='38', ncol=1, handleheight=1.2, labelspacing=0.0, frameon=False)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()