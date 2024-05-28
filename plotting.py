import matplotlib.pyplot as plt
import numpy as np

def plotting(results1,results2):
    light_blue = (216 / 255, 233 / 255, 248 / 255)
    light_pink = (246 / 255, 230 / 255, 230 / 255)
    bubbles = (155/255, 218/255, 210/255)
    # Data
    rsp = [40.7482, 66.87266666666667, 49.72546666666667, 59.49826666666666]
    reading = [128.08694117647059, 109.91964285714286, 111.73444444444444, 121.4146666666666]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = rsp + results1 + reading + results2
    colors = [light_blue, light_blue, light_blue, light_blue, bubbles,light_pink, light_pink, light_pink, light_pink, bubbles]

    # Plotting
    plt.scatter(x, y, c=colors, alpha=0.5)
    plt.xlabel('Time')
    plt.ylabel('Trials')
    plt.title('Scatter Plot of rsp and reading values')
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=light_blue, markersize=10, label='rsp task'),
               plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=light_pink, markersize=10, label='reading task'),
               plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=bubbles, markersize=10, label='you')]
    plt.legend(handles=handles)
    # Saving the plot
    plt.savefig('trial.png')



