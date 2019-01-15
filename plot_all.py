#!/usr/bin/env python
# -*- coding:utf-8 -*-
# plot all figures. It is available after files separated.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from filter50 import *

plt.rcParams['figure.figsize'] = (12.8, 7.2)

def read_and_plot(name):
    for i in range(1, 21):
        names = ['f', 'r', 'i']
        table = pd.read_table((name+'{}.txt').format(i), sep='\s+', names=names)
        amp = np.sqrt(np.square(table.r) + np.square(table.i))
        filter50(amp)
        plt.plot(table.f, amp)
        plt.xlabel('frequency')
        plt.ylabel(name+' amplitude')


plt.subplot(221)
read_and_plot('vv')

plt.subplot(222)
read_and_plot('vh')

plt.subplot(223)
read_and_plot('hv')

plt.subplot(224)
read_and_plot('hh')

plt.show()
