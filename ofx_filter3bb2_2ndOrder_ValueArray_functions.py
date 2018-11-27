import os
import sys
import math
from scipy import signal

## VALUE ARRAYS FOR 2ND ORDER FILTERS

value = [[""]*256]*3

freq_length = 100
filter_length = 100

filter_type = 0
exponent = 16.0
order = 2
atten = 0.01
q = 0.57
start_freq = 175
log_atten =-20*math.log(atten,10)


lp_a = [[]*3]*100
lp_b = [[]*3]*100
bp_a = [[]*5]*100
bp_b = [[]*5]*100
hp_a = [[]*3]*100
hp_b = [[]*3]*100


def create_filter3bb2_2ndOrder_main_array():

    sample_freq = 48000
    nyq = 0.5 * sample_freq

    for i in range(0,filter_length):
        freq = int(start_freq*(2**(i/exponent)))
        bw = freq/q
        band_freq_low = freq - bw/2
        band_freq_high = freq + bw/2
        lo_freq = band_freq_low
        hi_freq = band_freq_high
        lo_normal_freq = lo_freq / nyq
        band_normal_freq = [band_freq_low/nyq, band_freq_high/nyq]
        hi_normal_freq = hi_freq / nyq
        if filter_type == 0:
            lp_b[i],lp_a[i] = signal.butter(order, lo_normal_freq, 'low', analog=False)
            bp_b[i],bp_a[i] = signal.butter(order, band_normal_freq, 'band', analog=False)
            hp_b[i],hp_a[i] = signal.butter(order, hi_normal_freq, 'high', analog=False)
        else:
            lp_b[i],lp_a[i] = signal.cheby2(order, log_atten, lo_normal_freq, 'low', analog=False)
            bp_b[i],bp_a[i] = signal.cheby2(order, log_atten, band_normal_freq, 'band', analog=False)
            hp_b[i],hp_a[i] = signal.cheby2(order, log_atten, hi_normal_freq, 'high', analog=False)



    filter_data = "const double lp2["+str(filter_length)+"][6] = {"
    print "low pass"
    for i in range(0,filter_length):

        filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f}".format(lp_b[i][0],lp_b[i][1],lp_b[i][2],lp_a[i][0],lp_a[i][1],lp_a[i][2])
        if i == filter_length-1:
            filter_data += "{" + str(filter_string)+"}};\n"
        else:
            filter_data += "{" + str(filter_string)+"}, "

    filter_data += "const double bp2["+str(filter_length)+"][10] = {"
    print "band pass"
    for i in range(0,filter_length):

        filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f},{6:7.18f},{7:7.18f},{8:7.18f},{9:7.18f}".format(bp_b[i][0],bp_b[i][1],bp_b[i][2],bp_b[i][3],bp_b[i][4],bp_a[i][0],bp_a[i][1],bp_a[i][2],bp_a[i][3],bp_a[i][4])

        if i == filter_length-1:
            filter_data += "{" + str(filter_string)+"}};\n"
        else:
            filter_data += "{" + str(filter_string)+"}, "



    filter_data += "const double hp2["+str(filter_length)+"][6] = {"
    print "high pass"
    for i in range(0,filter_length):
        filter_string = "{0:7.18f},{1:7.18f},{2:7.18f},{3:7.18f},{4:7.18f},{5:7.18f}".format(hp_b[i][0],hp_b[i][1],hp_b[i][2],hp_a[i][0],hp_a[i][1],hp_a[i][2])

        if i == filter_length-1:
            filter_data += "{" + str(filter_string)+"}};\n"
        else:
            filter_data += "{" + str(filter_string)+"}, "
    return filter_data
