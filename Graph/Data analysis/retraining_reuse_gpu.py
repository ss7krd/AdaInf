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

stepX_intOutputs=[0.01,0.01,0.01,0.51,0.51,0.51,0.51,0.91,0.91,0.91,0.91,1.4,1.4,1.4,1.9,1.9,1.9,2.4,2.4,2.4]
stepX_paramValues=[0.01,0.01,0.01,0.01,0.3,0.3,0.3,0.6,0.6,0.6,0.6,1,1,1,1.3,1.3,1.3,1.3,1.6,1.6]
#DRAWING VERTICAL CHARTS
# vals = pd.read_csv('rmse_vs_serverNo.csv')
# vals_eachComp = pd.read_csv('training_time_data_each_comp.csv')

stepY = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
# parameter_values = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
# sixtykValuesModified = []
# for i in sixtykValues:
#     j = (i/100.0)*6415
#     sixtykValuesModified.append(j) 

# rects1 = ax.bar(ind, our_system, width, color='r', edgecolor='black', hatch="+", label="Our System")
ax.plot(stepX_intOutputs,stepY,c='blue',ls='-', linewidth = 4, label="Intermediate outputs")
ax.plot(stepX_paramValues,stepY,c='red',ls='-', linewidth = 4, label="Parameter values")
# ax.plot()

# centralized = [95,95,95,95.3,95,95,95,95,95.4,95,95,95,95,95.5,95,95,95,95.8,95,95]
# ax.plot(stepX,centralized,c='black',marker="*",markersize=28,ls='-',label="Ekya",fillstyle='full', linewidth = 6)

# fortykValuesModified = []
# for i in fortykValues:
#     j = (i/100.0)*7222
#     fortykValuesModified.append(j)

# rects2 = ax.bar(ind+width, federated_learning, width, color='b', edgecolor='black', hatch="*", label='Federated Learning')

# static = [99,99,99.6,99,89,89.5,89.7,89,91.3,89,89,91.6,89.2,89,89.4,91,89,89.3,89.6,89.5]
# ax.plot(stepX, static, c = 'blue', marker = 'o', markersize = 26, ls = '-', label = "Without retraining", fillstyle = 'full', linewidth = 6)



ax.set_ylabel('Percentile')
ax.set_xlabel('Reuse time (ms)')
# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
# xvalues = [385,390,395,400,405,410,415,420,425,430]
# plt.xticks(xvalues)
# plt.xticks(xvalues)
# ax.set_xticklabels(["%d%%" % x for x in xvalues], fontsize=36)
# ax.set_xticklabels(xvalues)

# ax.set_ylim(70, 100)
ytickvalues = []

ax.set_ylim(5, 101)
ytickvalues = []
for i in range(5, 101, 20):
	ytickvalues.append(i)
plt.yticks(ytickvalues)
ax.set_yticklabels(["%d%%" % x for x in ytickvalues])
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
ax.set_position([box.x0 + box.width*0.01, box.y0 + box.height*0.09, box.width, box.height*0.85])
#bbox_to_anchor=(0.5, 1.6)

leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.35), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
           fontsize='48', ncol=1, handleheight=1.5, labelspacing=0.0, frameon=False) 

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