import os
import sys
import math
from scipy import signal

## VALUE ARRAYS FOR 3RD ORDER LOHIFILTER

value = [[""]*256]*3

freq_length = 100
filter_length = 100


order = 3
exponent = 16.0
start_freq = 175
atten = 0.01
log_atten =-20*math.log(atten,10)


def create_lohifilter_main_array():
    filter_data = "const double lp3["+str(filter_length)+"][8] = {"

    print "low pass"
    for i in range(0,filter_length):
        lo_freq = int(110*(2**(i/exponent)))
        sample_freq = 48000
        nyq = 0.5 * sample_freq
        lo_normal_freq = lo_freq / nyq

        filter_b, filter_a = signal.cheby2(order, log_atten, lo_normal_freq, 'low', analog=False)
        filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f},{6:7.18f},{7:7.18f}".format(filter_b[0],filter_b[1],filter_b[2],filter_b[3],filter_a[0],filter_a[1],filter_a[2],filter_a[3])
        if i == filter_length-1:
            filter_data += "{" + str(filter_string)+"}};\n"
        else:
            filter_data += "{" + str(filter_string)+"}, "
    filter_data += "const double hp3["+str(filter_length)+"][8] = {"
    print "high pass"
    for i in range(0,filter_length):
        hi_freq = int(110*(2**(i/12.0))*0.15)
        sample_freq = 48000
        nyq = 0.5 * sample_freq
        hi_normal_freq = hi_freq / nyq

        filter_b, filter_a = signal.cheby2(order, log_atten, hi_normal_freq, 'high', analog=False)
        filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f},{6:7.18f},{7:7.18f}".format(filter_b[0],filter_b[1],filter_b[2],filter_b[3],filter_a[0],filter_a[1],filter_a[2],filter_a[3])
        if i == filter_length-1:
            filter_data += "{" + str(filter_string)+"}};\n"
        else:
            filter_data += "{" + str(filter_string)+"}, "
    return filter_data
