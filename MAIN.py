import matplotlib.pyplot as plt
y_values = [12, 49, 48, 52, 99, 98, 117, 155, 317, 499, 418, 310, 127, 55, 22, 14, 15, 2]
x_values = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
plt.bar(x_values,y_values)
plt.title("U.S K.I.A", fontsize=18)
plt.xlabel("YEARS", fontsize=14)
plt.ylabel("K.I.A", fontsize=14)
plt.axis([2001, 2018, 0, 500])
plt.show()

