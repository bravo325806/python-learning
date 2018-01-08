import matplotlib.pyplot as plt
labels = 'python','C++','Ruby','Java','PHP','Perl'
size = [33,52,12,17,62,48]
separated = (.1,0,0,0,0,0) # separate
plt.pie(size , labels = labels,autopct='%1.1f%%',explode=separated) # pie
plt.axis('equal') # 比例
plt.show()