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

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.2     # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
batchSize_time = (np.array([20,35,68,152]))
comm_time = np.array([5, 10, 14, 40])
# dummy = [10.9,10.8,10.8,10.9]
# dummy2 = [2.2,2.3,2.2,2.2]

ax.bar(ind, comm_time, width, color=[(1,0.7,0)], hatch = '//', edgecolor='black', label='Communication time between\nCPU memory and GPU memory')
ax.bar(ind, batchSize_time-comm_time, width, color='darkgrey', edgecolor='black', label='Computation time in\nGPU computation space', bottom = comm_time)

# ax.set_ylim(70, 101)
# ytickvalues = []
# for i in range(70, 101, 5):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=32)
ax.set_xlabel('Batch size')
ax.set_ylabel('Per-batch\nlatency (ms)')
# ax.set_xlabel('Number of other datasets in combination')
ax.set_xticks(ind)

xvalues = [4, 8, 16, 32]
ax.set_xticklabels(xvalues)

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.05, box.width, box.height*0.6])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.95), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='48', ncol=1, handleheight=1.2, labelspacing=0.7, frameon=False)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()