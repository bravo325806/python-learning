import matplotlib.pyplot as plt
import pandas as pd

raw_data = {'names':['a','b','c','d','e'],
            'jan_ir':[133,122,101,104,320],
            'feb_ir':[122,132,144,98,62],
            'march_ir':[64,99,32,12,65] }
df = pd.DataFrame(raw_data,columns=['names','jan_ir','feb_ir','march_ir'])
df['total_ir'] = df['jan_ir']+ df['feb_ir']+df['march_ir']
colors = [(1,.4,.4),(1,.6,1),(.5,.3,1),(.7,.7,.2),(.6,.2,.6)]
print(df)

plt.pie( df['total_ir'] ,
    labels = df['names'],
    colors = colors,
    autopct='%1.1f%%',
    ) # 比例
plt.axis('equal') 

plt.show()