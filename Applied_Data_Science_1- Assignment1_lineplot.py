# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 03:43:27 2023

@author: admin
"""
# Import Python Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot multiple line graph
def Create_plot_line(Year,Type,Label,Color):
    '''function to plot line graph. The function accepts 4 parameters i.e X axis data, Y axis data, label and color'''
    plt.plot(Year,Type,label = Label, linestyle="-", marker='o', markersize=4, color= Color, linewidth=2.5)
    plt.xticks(BD_economic_indicators['Year'])
    plt.yticks(np.arange(0, 50, step=2))
    plt.title('Bangladesh Economic growth Indicator')
    plt.xlabel('Year $\longrightarrow$')
    plt.ylabel('Data in Percentage of Total GDP $\longrightarrow$')
    plt.legend(loc='upper right', prop={'size': 11})

# Read data from CSV file and select the data for ploting
print(Create_plot_line.__doc__)
BD_economic_indicators = pd.read_csv('BD_economic_indicators.csv', )
BD_economic_indicators
BD_economic_indicators = pd.DataFrame(BD_economic_indicators)
BD_economic_indicators.dtypes
BD_economic_indicators = BD_economic_indicators.iloc[29:40,:]
BD_economic_indicators

# Call function to plot line plots
fig1 = plt.figure(figsize=(10,8))
Create_plot_line(BD_economic_indicators['Year'],BD_economic_indicators['Inflation rate'],"Inflation rate","yellow")
Create_plot_line(BD_economic_indicators['Year'],BD_economic_indicators['GDP growth'],"GDP growth","red")
Create_plot_line(BD_economic_indicators['Year'],BD_economic_indicators['Unemployed rate'],"Unemployed rate","blue")
Create_plot_line(BD_economic_indicators['Year'],BD_economic_indicators['Government debt'],"Government debt","green")
Create_plot_line(BD_economic_indicators['Year'],BD_economic_indicators['Total Investment'],"Total Investment","black")
plt.show()

