import clean as cl
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# case study
# Londed Air

# load dataset

air = pd.read_csv('LaqnData.csv')

cl.analysis(air)

# site and Provisional or Ratified has only one entry
# drop for analysis

air = air.drop(['Site', 'Provisional or Ratified'], axis=1)

# remove NaN from value
air.Value.dropna()

cl.analysis(air)

# plot hist of value
cl.plot(air, 'hist', column1='Value', xlimMin=-0.6, xlimMax=1023.400020)

# plot line of value
cl.plot(air, 'line', column1='Value', xlimMin=-0.6, xlimMax=1023.400020)

air = cl.removeOutliners(air, 'Value')

cl.analysis(air)

# pivoting ReadingDateTime

# first lets split ReadingDateTime

air['ReadingDateTime'] = air['ReadingDateTime'].str.split(" ")

# creating seperate columns for date and time
air['ReadingDate'] = air['ReadingDateTime'].str[0]
air['ReadingTime'] = air['ReadingDateTime'].str[1]

air = air.drop('ReadingDateTime', axis=1)

cl.analysis(air)

# pivot for date

airPivotDate = air.pivot_table(index=['Species', 'Units'], columns='ReadingDate', values='Value', aggfunc=np.mean)

airPivotDate = airPivotDate.reset_index()

cl.analysis(airPivotDate)

# plot lines of dates mean values
airPivotDate.plot()

plt.show()


# pivot for time

airPivotTime = air.pivot_table(index=['Species', 'Units'], columns='ReadingTime', values='Value', aggfunc=np.mean)

airPivotTime = airPivotTime.reset_index()

cl.analysis(airPivotTime)

# plot lines of dates mean values
airPivotTime.plot()

plt.show()