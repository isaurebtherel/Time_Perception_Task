import matplotlib.pyplot as plt
import numpy as np

def average_difference(lst):
    differences = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
    sum_of_differences = sum(differences)
    average_diff = sum_of_differences / len(differences)
    return average_diff

def average_difference_list_of_lists(lst_of_lst):
    avg_diffs = []
    for lst in lst_of_lst:
        differences = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
        sum_of_differences = sum(differences)
        average_diff = sum_of_differences / len(differences)
        avg_diffs.append(average_diff)
    return avg_diffs

# Given lists of lists
rsp = [[46867, 61730, 85236, 104187, 127509],
       [25347, 50911, 79208, 102504, 130302, 152488, 174652],
       [104174, 127751, 149878, 170467, 192487, 210391],
       [32993, 57012, 191247, 191247, 196335, 247894],
       [82014, 110881, 110882, 135666, 164719, 208462, 232048, 255216, 283246, 313773],
       [83177, 110859, 151654, 177832, 208911, 222702, 260999], [71020, 73518, 95579, 118340, 138927, 158665, 182600, 199845, 226538]
,[115400, 148806, 186372, 210503, 237280, 277543, 302118]
]

reading = [[189898, 206883, 231964, 243252, 265638, 277996, 292349, 306087, 369595, 381135, 394251, 418388, 437303, 447604, 474199, 489495, 504508, 518459],
           [206923, 239280, 276300, 309818, 359313, 395087, 412911, 464600],
           [230150, 261374, 280139, 302341, 326438, 361475, 421099, 456400, 501422],
           [307936, 326682, 349991, 379927, 397241, 412869, 435652, 456855, 484650, 516099],
           [332233, 343901, 376169, 406643, 426114, 455430, 481488, 516989, 539803, 554483, 578821, 603130, 616431, 639967],
           [301636, 337464, 373111, 405003, 427180, 458383, 494465, 522415, 539811, 569141, 624167, 648277],[253927, 275710, 323833, 341640, 381515, 416319, 438794, 467201, 506441, 541289],[401665, 443968, 486607, 516819, 542410, 579671, 617762, 659865, 699795, 737026]]

# Calculate average differences for each list of lists
rsp_avg_diffs = average_difference_list_of_lists(rsp)
reading_avg_diffs = average_difference_list_of_lists(reading)

def plotting(results1,results2):
    light_blue = (216 / 255, 233 / 255, 248 / 255)
    light_pink = (246 / 255, 230 / 255, 230 / 255)
    bubbles = (155/255, 218/255, 210/255)
    # Data
    x = rsp_avg_diffs + results1 + reading_avg_diffs + results2
    y = numbers = list(range(1, len(x)+1))
    colors = [light_blue, light_blue, light_blue, light_blue, light_blue, light_blue, light_blue, light_blue,bubbles, light_pink, light_pink, light_pink, light_pink, light_pink, light_pink, light_pink, light_pink, bubbles]

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

