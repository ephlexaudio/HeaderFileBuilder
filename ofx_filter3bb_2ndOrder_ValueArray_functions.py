import os
import sys
import math
from scipy import signal

## VALUE ARRAYS FOR 2ND ORDER FILTERS


value = [[""]*256]*3

base_freq = 75
exponent = 14.0
filter_type = 0
order = 2
atten = 0.01
log_atten =-20*math.log(atten,10)

filter_length = 101

def create_freq_pedalUi_array():
    freq_data = " //filter freq\n"
    freq_data += "{"
    for i in range(0,filter_length):
        freq = int(base_freq*(2**(i/exponent)))

        if i == filter_length-1:
            freq_data += "\"Hz\"},\n"
        else:
            freq_data += "\"" + str(freq)+ "\", "
    return freq_data

filter_length = 101
def create_freq_hostUi_array():
    freq_data = "lutArray[3] = new String[] {"
    for i in range(0,filter_length):
        freq = int(base_freq*(2**(i/exponent)))

        if i == filter_length-1:
            freq_data += "\"Hz\"};\n"
        else:
            freq_data += "\"" + str(freq)+"\", "
    return freq_data

main_filter_length = 100

def create_filter3bb_2ndOrder_main_array():
    filter_data = "const double lp["+str(main_filter_length)+"][6] = {"
    print "low pass"
    for i in range(0,main_filter_length):
        lo_freq = int(base_freq*(2**(i/exponent)))
        sample_freq = 48000
        nyq = 0.5 * sample_freq
        if filter_type == 0:
            lo_normal_freq = lo_freq / nyq
            filter_b, filter_a = signal.butter(order, lo_normal_freq, 'low', analog=False)
        else:
            lo_normal_freq = lo_freq / nyq
            filter_b, filter_a = signal.cheby2(order, log_atten, lo_normal_freq, 'low', analog=False)
        filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f}".format(filter_b[0],filter_b[1],filter_b[2],filter_a[0],filter_a[1],filter_a[2])
        if i == main_filter_length-1:
            filter_data += "{" + str(filter_string)+"}};\n"
        else:
            filter_data += "{" + str(filter_string)+"}, "

    filter_data += "const double hp["+str(main_filter_length)+"][6] = {"
    print "high pass"
    for i in range(0,main_filter_length):
        hi_freq = int(base_freq*(2**(i/exponent)))
        sample_freq = 48000
        nyq = 0.5 * sample_freq
        if filter_type == 0:
            hi_normal_freq = hi_freq / nyq
            filter_b, filter_a = signal.butter(order, hi_normal_freq, 'high', analog=False)
        else:
            hi_normal_freq = 0.15 * (hi_freq / nyq)
            filter_b, filter_a = signal.cheby2(order, log_atten, hi_normal_freq, 'high', analog=False)
        filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f}".format(filter_b[0],filter_b[1],filter_b[2],filter_a[0],filter_a[1],filter_a[2])
        if i == main_filter_length-1:
            filter_data += "{" + str(filter_string)+"}};\n"
        else:
            filter_data += "{" + str(filter_string)+"}, "
    return filter_data
