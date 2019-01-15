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
table_vv = pd.read_table('vvd.txt', sep='\s+', names=names)
table_hv = pd.read_table('hvd.txt', sep='\s+', names=names)
plt.bar(loc, table_vv.amp, tick_label=loc)
plt.bar(loc, table_hv.amp)
vvamp = list(np.array(table_vv.amp))
vvamp.remove(max(vvamp))
vvamp.remove(max(vvamp))
vvamp.remove(min(vvamp))
vvamp.remove(min(vvamp))
mean_vv = np.array(vvamp).mean() * np.ones(20)
plt.plot(loc, mean_vv)
plt.ylim(0, 0.01)
plt.xlabel('Location')
plt.ylabel('sensor_v_FRF')

plt.subplot(222)
percent_vv = (table_vv.amp - mean_vv)/mean_vv
plt.bar(loc, percent_vv)
plot_dash(0.05,-0.05,0.1,-0.1)
plt.xlabel('Location')
plt.ylabel('Error')

plt.subplot(223)
plt.bar(loc, table_hv.amp/table_vv.amp, tick_label=loc)
plt.xlabel('Location')
plt.ylabel('hv/vv')

plt.subplot(224)
ev3 = range(1, 19)
ev3_amp = []

for i in ev3:
    amp_ave3 = table_vv.amp[i-1]+table_vv.amp[i]+table_vv.amp[i+1]
    ev3_amp.append(amp_ave3)

s = 0

for i in range(len(ev3_amp)):
    s += ev3_amp[i]

s = s/len(ev3_amp)
ev3_percent = []

for i in range(len(ev3_amp)):
    ev3_percent.append((ev3_amp[i]-s)/s)

plt.bar(ev3, ev3_percent, tick_label=range(2, 20))

plot_dash(-0.02,0.02,-0.05,0.05, num=18)
plt.ylim(-0.06, 0.06)
plt.ylabel('ev3_FRF_Error')
plt.xlabel('Location')

plt.show()
