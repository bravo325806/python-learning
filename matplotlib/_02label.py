import matplotlib.pyplot as plt

years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]

pops = [2.5,2.7,3,3.3,3.6,4.0,
        4.4,4.8,5.3,6.1,6.5,6.9,7.3]
plt.plot(years,pops, color=(255/255,100/255,100/255))

plt.title("Population Growth") # title
plt.ylabel("Population in billions") # y label
plt.xlabel("Population growth by year") # x label

plt.show()