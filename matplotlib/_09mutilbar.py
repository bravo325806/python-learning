import matplotlib.pyplot as plt
import numpy as np


col_count = 3
bar_width = 0.2
index = np.arange(col_count)

# create data
k_scores = (553,536,548)
c_scores = (518,523,523)
n_scores = (613,570,588)
f_scores = (475,505,499)

# put into data 
k = plt.bar(index,
           k_scores, 
           bar_width,
           alpha=.4,
           label="K") 
c = plt.bar(index+0.2,
            c_scores,
            bar_width,
            alpha=.4,
            label="C") 
n = plt.bar(index+0.4,
            n_scores,
            bar_width,
            alpha=.4,
            label="N") # x,y ,width
f = plt.bar(index+0.6,
            f_scores,
            bar_width,
            alpha=.4,
            label="F") # x,y ,width


def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x()+item.get_width()/2., 
            height*1.05, 
            '%d' % int(height),
            ha = "center",
            va = "bottom",
        )

createLabels(k)
createLabels(c)
createLabels(n)
createLabels(f)


plt.ylabel("Mean score")
plt.xlabel("Subject")
plt.title("Test Scores by Contry")

plt.xticks(index+.3 / 2 ,("Math","Reading","Science"))
plt.legend() 
plt.grid(True)

# for item in k:
#     print("height: ",item.get_height())
#     print("width: ",item.get_width())

plt.show()