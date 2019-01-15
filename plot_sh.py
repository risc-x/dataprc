#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

loc = np.arange(1, 21)
plt.rcParams['figure.figsize'] = (12.8, 7.2)

def plot_dash(*height, num=20):
	for i in height:
		plt.plot(np.arange(1, num+1), i*np.ones(num))

plt.subplot(221)
names = ['amp']
table_hh = pd.read_table('hhd.txt', sep='\s+', names=names)
table_vh = pd.read_table('vhd.txt', sep='\s+', names=names)
plt.bar(loc, table_hh.amp, tick_label=loc)
plt.bar(loc, table_vh.amp)
hhamp = list(np.array(table_hh.amp))
hhamp.remove(max(hhamp))
hhamp.remove(max(hhamp))
hhamp.remove(min(hhamp))
hhamp.remove(min(hhamp))
mean_hh = np.array(hhamp).mean() * np.ones(20)
plt.plot(loc, mean_hh)
plt.xlabel('Location')
plt.ylabel('sensor_h_FRF')

plt.subplot(222)
percent_hh = (table_hh.amp - mean_hh)/mean_hh
plt.bar(loc, percent_hh)

plot_dash(0.1,-0.1,0.2,-0.2)
plt.ylim(-0.2, 0.5)
plt.xlabel('Location')
plt.ylabel('Error')

plt.subplot(223)
plt.bar(loc, table_vh.amp/table_hh.amp, tick_label=loc)
plt.xlabel('Location')
plt.ylabel('vh/hh')

plt.subplot(224)
ev3 = range(1, 19)
ev3_amp = []

for i in ev3:
    amp_ave3 = table_hh.amp[i-1]+table_hh.amp[i]+table_hh.amp[i+1]
    ev3_amp.append(amp_ave3)

s = 0

for i in range(len(ev3_amp)):
    s += ev3_amp[i]

s = s/len(ev3_amp)
ev3_percent = []

for i in range(len(ev3_amp)):
    ev3_percent.append((ev3_amp[i]-s)/s)

plt.bar(ev3, ev3_percent, tick_label=range(2, 20))
plot_dash(0.1,-0.1,0.05,-0.05,num=18)

plt.ylabel('ev3_FRF')
plt.xlabel('Location')

plt.show()
