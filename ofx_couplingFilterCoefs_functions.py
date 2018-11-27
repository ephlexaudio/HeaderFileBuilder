import os
import sys
import math
from scipy import signal

## VALUE ARRAYS FOR 2ND ORDER FILTERS




value = [[""]*256]*3

freq_length = 100
filter_length = 100






base_freq = 50.000
filter_type = 0
order = 2
atten = 0.01
log_atten =-20*math.log(atten,10)


def create_coupler_main_coefs():
    hi_freq = int(base_freq)
    sample_freq = 48000
    nyq = 0.5 * sample_freq
    if filter_type == 0:
        hi_normal_freq = hi_freq / nyq
        filter_b, filter_a = signal.butter(order, hi_normal_freq, 'high', analog=False)
    else:
        hi_normal_freq = 0.15 * (hi_freq / nyq)
        filter_b, filter_a = signal.cheby2(order, log_atten, hi_normal_freq, 'high', analog=False)
    filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f}".format(filter_b[0],filter_b[1],filter_b[2],filter_a[0],filter_a[1],filter_a[2])

    filter_data = "const double couplingFilter[6] = {"+str(filter_string)+"};\n"
    return filter_data
