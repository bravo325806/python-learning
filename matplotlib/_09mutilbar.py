import matplotlib.pyplot as plt
import numpy as np


col_count = 3
bar_width = 0.1
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
c = plt.bar(index+0.1,
            c_scores,
            bar_width,
            alpha=.4,
            label="C") 
n = plt.bar(index+0.2,
            n_scores,
            bar_width,
            alpha=.4,
            label="N") # x,y ,width
f = plt.bar(index+0.3,
            f_scores,
            bar_width,
            alpha=.4,
            label="F") # x,y ,width
plt.ylabel("Mean score")
plt.xlabel("Subject")
plt.title("Test Scores by Contry")

plt.xticks(index+.3 / 2 ,("Math","Reading","Science"))
plt.legend() 
plt.grid(True)
plt.show()