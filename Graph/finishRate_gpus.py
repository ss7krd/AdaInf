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

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.09      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

stepX=[1, 4, 8]
#DRAWING VERTICAL CHARTS
# vals = pd.read_csv('rmse_vs_serverNo.csv')
# vals_eachComp = pd.read_csv('training_time_data_each_comp.csv')

proposed = [97.4,99.7,99.9]
# sixtykValuesModified = []
# for i in sixtykValues:
#     j = (i/100.0)*6415
#     sixtykValuesModified.append(j) 

# rects1 = ax.bar(ind, our_system, width, color='r', edgecolor='black', hatch="+", label="Our System")
ax.plot(stepX,proposed,c='red',marker="x",mew=4,markersize=26,ls='-',label="AdaInf",fillstyle='full', linewidth = 6)

centralized = [40.4,49.8,59.7]
ax.plot(stepX,centralized,c='green',marker="*",markersize=26,ls='-',label="Ekya",fillstyle='full', linewidth = 6)

# fortykValuesModified = []
# for i in fortykValues:
#     j = (i/100.0)*7222
#     fortykValuesModified.append(j)

# rects2 = ax.bar(ind+width, federated_learning, width, color='b', edgecolor='black', hatch="*", label='Federated Learning')

static = [93.8,96.7,97.8]
ax.plot(stepX, static, c = 'blue', marker = 'o', markersize = 26, ls = '-', label = "Scrooge", fillstyle = 'full', linewidth = 6)
ax.plot(stepX, static, c = 'lime', marker = 's', markersize = 26, ls = '-', label = "Scrooge*", fillstyle = 'none', linewidth = 6)

ax.set_ylim(35, 105)
ytickvalues = []
for i in range(35, 105, 20):
	ytickvalues.append(i)
plt.yticks(ytickvalues)
ax.set_yticklabels(["%d%%" % x for x in ytickvalues])


ax.set_ylabel('Average finish rate')
ax.set_xlabel('Number of GPUs')
# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
xvalues = [1, 4, 8]
# plt.xticks(xvalues)
plt.xticks(xvalues)
# ax.set_xticklabels(["%d%%" % x for x in xvalues], fontsize=36)
ax.set_xticklabels(xvalues)

# ax.set_ylim(70, 100)
ytickvalues = []
# for i in range(70, 105, 10):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=36)
# ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('iWash', 'WristWash', 'H2DTR-NN', 'H2DTR-kNN'), loc=1, fontsize=28 )

# ax.legend( (rects1[0], rects2[0], rects3[0]), ('Our System', 'Federated Learning', 'Malicious Device Detection+Trust-aware Reassignment'), loc=1, fontsize=28)

# ax.legend(loc=1)
# plt.title("Categorization of Errors in Critical Cases")
# def autolabel(rects):
#     for rect in rects:
#         h = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
#                 ha='center', va='bottom')

# # autolabel(rects1)
# # autolabel(rects2)
# # autolabel(rects3)

# plt.show()

#DRAWING HORIZONTAL CHARTS
# our_lexicon_bangla = [9.8, 1.33]
# rects1 = ax.barh(ind, our_lexicon_bangla, width, color='r', edgecolor='black', hatch=patterns[0])
# our_lexicon_romanized = [9.9, 1.27]
# rects2 = ax.barh(ind+width, our_lexicon_romanized, width, color='g', edgecolor='black', hatch=patterns[1])
# google_lexicon = [14.8, 1.88]
# rects3 = ax.barh(ind+width*2, google_lexicon, width, color='b', edgecolor='black', hatch=patterns[9])

# ax.set_xlabel('Percentage')
# ax.set_yticks(ind+width)
# ax.set_yticklabels( ('WER %', 'PER %') )
# # ax.set_xlim(0,25)
# ax.legend( (rects1[0], rects2[0], rects3[0]), ('Our lexicon Bangla', 'Our lexicon romanized', 'Google lexicon') )

# # def autolabel(rects):
# #     for rect in rects:
# #         h = rect.get_height()
# #         ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
# #                 ha='center', va='bottom')

# # autolabel(rects1)
# # autolabel(rects2)
# # autolabel(rects3)

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.09, box.width, box.height*0.75])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.45), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
           fontsize='48', ncol=3, handleheight=1.5, labelspacing=0.0, frameon=False) 
# leg = plt.legend(loc='upper center', bbox_to_anchor=(0.3, 1.55), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            # fontsize='36', ncol=2, handleheight=1.5, labelspacing=0.0, frameon=False)
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          # fancybox=True, shadow=True, ncol=5)
# plt.legend(frameon=False)
# leg.get_frame().set_linewidth(0.0)
# fig.tight_layout()
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
# figure = plt.gcf()  # get current figure
# figure.set_size_inches(50, 30)
# plt.savefig("/home/sudipta/Desktop/image_filename_test.png")
plt.show()