#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

df_quakes=pd.read_csv("all_month.csv")
binwidth=1
plt.figure()
plt.hist(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,bins=range(0,10+binwidth,binwidth))
plt.title('Histogram of Earthquake magnitude (binwidth ='+ str(binwidth)+')')
plt.xlabel('Earthquake Magnitude')
plt.ylabel('Number of events')
plt.savefig('histogram.png')
plt.close()
#plot kde
df_quakes[np.isfinite(df_quakes['mag'])].mag.plot.kde(title="KDE of Magnitude")
plt.savefig('kde.png')
plt.figure()
plt.scatter(df_quakes[np.isfinite(df_quakes['mag'])].longitude, df_quakes[np.isfinite(df_quakes['mag'])].latitude)
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

plt.figure()
plt.scatter(df_quakes[np.isfinite(df_quakes['mag'])].mag,df_quakes[np.isfinite(df_quakes['mag'])].depth)
plt.title("Earthquake magnitude variation with depth")
plt.xlabel("Magnitude")
plt.ylabel("Depth(km)")
plt.savefig('variationwithdepth.png')
plt.close()

plt.figure()
stats.probplot(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,dist=stats.gumbel_r,plot=plt)
plt.title("Gumbel QQ-Plot")
plt.savefig('gumbelqq.png')
plt.close()
plt.figure()
stats.probplot(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,dist=stats.norm,plot=plt)
plt.title("Normal QQ-Plot")
plt.savefig('normal.png')
plt.close()
plt.figure()
stats.probplot(df_quakes[np.isfinite(df_quakes['mag'])].mag.values,dist=stats.genpareto(-0.75),plot=plt)
plt.title("Pareto Distribution QQ-Plot")
plt.savefig('pareto.png')
plt.close()

