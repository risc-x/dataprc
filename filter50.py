# filter50
import numpy as np
def filter50(amp):
    lg = 5
    sf = 1024
    t = 4
    spcl = sf * t
    for i in range(t*50+1, spcl-1,t*50):
        ampl = amp[i-lg]
        ampr = amp[i+lg]
        for j in range(i-lg, i+lg):
            amp[j] = (ampr-ampl)*(j-i+lg)/(2*lg)+ampl
    amp[0:10] = np.arange(10)*0


