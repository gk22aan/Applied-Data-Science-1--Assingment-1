# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:08:59 2023

@author: admin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot Pie Chart
def plot_bar_graph(X):
     ''' This function takes Parameter as data to be ploted a Pie Chart and plot a Pie Chart'''
     plt.figure(figsize=(10, 10), dpi= 80, facecolor='w', edgecolor='blue')
     plt.pie(X, autopct='%1.1f%%', radius = 1,startangle=140, shadow=True, labels=Carbon_Emission_Data_final['Country'],explode=(0.06, 0.06, 0.06, 0.06,0.06))
     plt.title("Top 5 CO2 Emitting Countries For Year 2017",bbox={'facecolor':'8', 'pad':5}, y = -0.03)
     plt.show()
#Read Data from CSV
Carbon_Emission_Data = pd.read_csv('List of countries by carbon dioxide emissions.csv',  )
Carbon_Emission_Data.fillna(0,inplace=True)
Carbon_Emission_Data

#Manipulate data for Plotting
Carbon_Emission_Data =  Carbon_Emission_Data.loc[:,['Country','Fossil CO2 emissions']]
Carbon_Emission_Data_Country = pd.DataFrame(Carbon_Emission_Data)
Carbon_Emission_Data_Country.reset_index(drop=False)
Carbon_Emission_Data_final = Carbon_Emission_Data_Country.sort_values(by = ['Fossil CO2 emissions'], ascending = False).head(5)
Carbon_Emission_Data_final['Fossil CO2 emissions'] = pd.to_numeric(Carbon_Emission_Data_final['Fossil CO2 emissions'].str[:-1].astype('float64'))
Carbon_Emission_Data_final

#Plot Data as Bar Plot
X = Carbon_Emission_Data_final['Fossil CO2 emissions']
#Call function for plotting Pie Chart
plot_bar_graph(X)