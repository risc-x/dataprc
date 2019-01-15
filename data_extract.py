# Extract data from txt and create new file

import pandas as pd
import numpy as np
from filter50 import *

name = ['f', 'r', 'i']

def read_and_write(read_name, names, fw, lft, rgt):
    for i in range(1, 21):
        table = pd.read_table(read_name.format(i), sep='\s+', names=names)
        amp = np.sqrt(np.square(table.r) + np.square(table.i))
        filter50(amp)
        amp_mean = amp[lft*4:rgt*4].mean()
        fw.write(str(amp_mean))
        fw.write('\n')


with open('vvd.txt', 'w') as vvd,\
     open('vhd.txt', 'w') as vhd,\
     open('hvd.txt', 'w') as hvd,\
     open('hhd.txt', 'w') as hhd:
    read_and_write('vv{}.txt', name, vvd, 60, 350)
    read_and_write('vh{}.txt', name, vhd, 60, 200)
    read_and_write('hv{}.txt', name, hvd, 60, 250)
    read_and_write('hh{}.txt', name, hhd, 60, 250)
