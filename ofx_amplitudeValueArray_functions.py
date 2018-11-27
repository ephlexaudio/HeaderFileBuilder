import os
import sys
import math
from scipy import signal

value = [[""]*256]*3


lin_amp_length = 101
log_amp_length = 101


def create_linAmplitude_pedalUi_array():
    amp_data = "//linAmp\n"
    amp_data += "{"
    print "linear amplitude"
    for i in range(0,lin_amp_length):
        lin_amp = (i + 1.0)/10.0
        if i == lin_amp_length-1:
            amp_data += "\" \"},\n"
        else:
            amp_data += "\"" + str(lin_amp)+"\", "
    print "dB amplitude"
    amp_data += "//dBAmp\n"
    amp_data += "{"
    for i in range(0,lin_amp_length):
        lin_amp = (i + 1.0)/10.0
        if i == lin_amp_length-1:
            amp_data += "\"dB\"},\n"
        else:
            amp_data += "\"" + str(lin_amp)+"\", "

    amp_data += "//logAmp\n"
    amp_data += "{"
    print "logarithmic amplitude"
    for i in range(0,log_amp_length):
        if i == 0:
            log_amp = 0.01
        elif 1 <= i <= 50:
            log_amp = 0.016*i+0.2
        elif 50 < i <= 70:
            log_amp = 0.11*i-4.5
        else:
            log_amp = 0.227*i-12.7+0.23
        if i == log_amp_length-1:
            amp_data += "\" \"},\n"
        else:
            amp_data += "\"" + str(round(log_amp,2))+"\", "
    return amp_data

def create_amplitude_hostUi_array():
    amp_data = "lutArray[0] = new String[]{"
    print "linear amplitude"
    for i in range(0,lin_amp_length):
        lin_amp = (i + 1.0)/10.0
        if i == lin_amp_length-1:
            amp_data += "\" \"};\n"
        else:
            amp_data += "\"" + str(lin_amp)+"\", "

    amp_data += "lutArray[1] = new String[]{"
    print "dB amplitude"
    for i in range(0,lin_amp_length):
        lin_amp = (i + 1.0)/10.0
        if i == lin_amp_length-1:
            amp_data += "\"dB\"};\n"
        else:
            amp_data += "\"" + str(lin_amp)+"\", "

    amp_data += "lutArray[2] = new String[]{"
    print "logarithmic amplitude"
    for i in range(0,log_amp_length):
        if i == 0:
            log_amp = 0.01
        elif 1 <= i <= 50:
            log_amp = 0.016*i+0.2
        elif 50 < i <= 70:
            log_amp = 0.11*i-4.5
        else:
            log_amp = 0.227*i-12.7+0.23
        if i == log_amp_length-1:
            amp_data += "\" \"};\n"
        else:
            amp_data += "\"" + str(round(log_amp,2))+"\", "
    return amp_data

main_lin_amp_length = 100
main_log_amp_length = 100

def create_amplitude_main_array():
    amp_data = "const float linAmp["+str(main_lin_amp_length)+"] = {"
    print "linear amplitude"
    for i in range(0,main_lin_amp_length):
        lin_amp = (i + 1.0)/10.0
        if i == main_lin_amp_length-1:
            amp_data += str(lin_amp)+"};\n"
        else:
            amp_data += str(lin_amp)+","

    amp_data += "const float dBAmp["+str(main_lin_amp_length)+"] = {"
    print "dB amplitude"
    for i in range(0,main_lin_amp_length):
        lin_amp = (i + 1.0)/10.0
        if i == main_lin_amp_length-1:
            amp_data += str(lin_amp)+"};\n"
        else:
            amp_data += str(lin_amp)+","

    amp_data += "const float logAmp["+str(main_log_amp_length)+"] = {"
    print "logarithmic amplitude"
    for i in range(0,main_log_amp_length):
        if i == 0:
            log_amp = 0.01
        elif 1 <= i <= 50:
            log_amp = 0.02*i
        elif 50 < i <= 70:
            log_amp = 0.11*i-4.5
        else:
            log_amp = 0.227*i-12.7+0.23
        if i == 0:
            amp_data += str(0.01)+","
        elif i == main_log_amp_length-1:
            amp_data += str(log_amp)+"};\n"
        else:
            amp_data += str(log_amp)+","
    return amp_data
