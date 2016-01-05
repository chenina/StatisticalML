import pandas 
import matplotlib.pyplot as plt

df = pandas.read_csv("store_train.csv")
fig, ax = plt.subplots()
#ax.plot_date(df.Date, df.Sales, xdate=True)
import datetime
plt.plot(pandas.to_datetime(df.Date),df.Sales)  #pandas.to_datetime
plt.tight_layout()
plt.show()