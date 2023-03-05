# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:00:26 2023

@author: admin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read CSV file
Olympic_Data = pd.read_csv('summer.csv',  )
Country_Data = pd.read_csv('dictionary.csv',)
print(Olympic_Data.head());
print(Country_Data.head())

# Function
def bar_color(color):
     ''' This function can be used to give custom colour to the bar of Bar plot
         color parameters to be passed while calling this function'''
     for i in range(20):
          barlist[i].set_color(color)

#Create Data for Plotting
Olympics_Data_Final = Olympic_Data.merge(Country_Data, left_on='Country', right_on='Code', how='inner')
Olympics_Data_Final
Olympics_Data_Final = Olympics_Data_Final.drop(columns=['Country_x']);
Olympics_Data_Final = Olympics_Data_Final.rename(columns={'Country_y': 'Country'})
Olympics_Data_Final.fillna(0,inplace=True)
Olympics_Data_Final.head(10)
Total_Medals = Olympics_Data_Final.groupby(['Country'])['Medal'].count()
pd.DataFrame(Total_Medals)
Total_Medals = Total_Medals.reset_index(drop=False)
Total_Medals = Total_Medals.sort_values(by = ['Medal'], ascending = False)
Total_Medals = Total_Medals.head(20)

#Plot data
with plt.style.context('ggplot'):
    fig2=plt.figure(figsize=(10, 8), dpi= 80, facecolor='w', edgecolor='blue')
    barlist = plt.bar('Country','Medal',data = Total_Medals)
    # Callfunction to define color of BAR in Bar plot.
    bar_color('green')
    barlist[0].set_color('Yellow')
    barlist[19].set_color('red')
    plt.xlabel('Country', fontsize = 16)
    plt.ylabel('Medals Won', fontsize = 16)
    plt.title('Total Medals won by Top 20 Countries since 1896', fontsize = 16)
    plt.xticks(Total_Medals['Country'], rotation=90, fontsize = 14)
    plt.show()