import matplotlib.pyplot as plt
import numpy as np

col_count = 3
k_scores = (553,536,548)
c_scores = (518,523,523)
n_scores = (613,570,588)
f_scores = (475,505,499)
index = np.arange(col_count)
k = plt.bar(index,k_scores, .5) # x,y ,width

plt.grid(True)
plt.show()