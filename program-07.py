#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on March 5 2020
Creator: Ankit Ghanghas

program_07.py

This script reads csv file as pandas dataframe and produces basic plots for visual analysis using Matplotlib.

The output of this script is 8 png files in the root directory namely histogram.png, kde.png, latlong.png, cdf.png, variationwithdepth.pnd, normal.png and gumbelqq.png

"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

#so far these import important modueles required for this script
df_quakes=pd.read_csv("all_month.csv") # imports all_month.csv present in the present directory as df_quakes
#Plot the histogram
binwidth=1
plt.figure() # generates a new blank figure
plt.hist(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,bins=range(0,10+binwidth,binwidth)) #first finds points where the magnitude is finite then only for those indices makes a histogram of magnitude of bin width 1.
plt.title('Histogram of Earthquake magnitude (binwidth ='+ str(binwidth)+')')# adds title to the plot.
plt.xlabel('Earthquake Magnitude')# adds label to the x axis
plt.ylabel('Number of events')# adds label to the y-axis
plt.savefig('histogram.png') #saves the figure as specified name
plt.close() # closes the figure

#plot kde
df_quakes[np.isfinite(df_quakes['mag'])].mag.plot.kde(title="KDE of Magnitude")#uses inbulit kde method of pandas module to cerate and plot it.
plt.savefig('kde.png')

#plot the scatter of longitude and lattitude
plt.figure()
plt.scatter(df_quakes[np.isfinite(df_quakes['mag'])].longitude, df_quakes[np.isfinite(df_quakes['mag'])].latitude) # scatter plot with longitude as xaxis and latitude as yaxis.
plt.title("Earthquakes across the Lat and Long")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig('latlong.png')
plt.close()

# plotting normalized cdf of earthquake depth
plt.figure()
plt.hist(df_quakes[np.isfinite(df_quakes['mag'])].depth.values,bins=500,cumulative =True,histtype="step", density=True)
plt.title("Normalized Cumulative Distribution Plot of Earthquake depths")
plt.xlabel("Depth(km)")
plt.ylabel("Cumulative Frequency")
plt.savefig('cdf.png')
plt.close()

# plotting a scatter plot of magnitude against depth for all cases where we have definite magnitude
plt.figure()
plt.scatter(df_quakes[np.isfinite(df_quakes['mag'])].mag,df_quakes[np.isfinite(df_quakes['mag'])].depth)
plt.title("Earthquake magnitude variation with depth")
plt.xlabel("Magnitude")
plt.ylabel("Depth(km)")
plt.savefig('variationwithdepth.png')
plt.close()

# plots qq plot of magnitude assuming gumbel distribution. We use probplt method in stats for plotting qq-plot
plt.figure()
stats.probplot(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,dist=stats.gumbel_r,plot=plt)
plt.title("Gumbel QQ-Plot")
plt.savefig('gumbelqq.png')
plt.close()

# qq-plot assuming normal distribution.
plt.figure()
stats.probplot(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,dist=stats.norm,plot=plt)
plt.title("Normal QQ-Plot")
plt.savefig('normal.png')
plt.close()

#qq-plot assuming pareto distribution.
#plt.figure()
#stats.probplot(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,dist=stats.genpareto(-0.75),plot=plt)
#plt.title("Pareto Distribution QQ-Plot")
#plt.savefig('pareto.png')
#plt.close()

