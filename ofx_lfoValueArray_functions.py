import os
import sys
import math
from scipy import signal

value = [[""]*256]*3


lfo_length = 100
lfo_sine_length = 250
lfo_sine_freq = 1

lfo_freq_funct_m = [0.000,0.000]
lfo_freq_funct_b = [0.000,0.000]
lfo_freq_funct_x = [0,50,99]
lfo_freq_funct_y = [0.100,1.000,20.000]

lfo_freq_funct_m[0] = (lfo_freq_funct_y[1]-lfo_freq_funct_y[0])/(lfo_freq_funct_x[1]-lfo_freq_funct_x[0])
lfo_freq_funct_m[1] = (lfo_freq_funct_y[2]-lfo_freq_funct_y[1])/(lfo_freq_funct_x[2]-lfo_freq_funct_x[1])
lfo_freq_funct_b[0] = lfo_freq_funct_y[0] - lfo_freq_funct_m[0]*lfo_freq_funct_x[0]
lfo_freq_funct_b[1] = lfo_freq_funct_y[1] - lfo_freq_funct_m[1]*lfo_freq_funct_x[1]

lfo_length = 101
def create_lfo_pedalUi_array():
    lfo_data = "//lfo_freq\n"
    lfo_data += "{"
    for i in range(0,lfo_length):
        if(i < 50):
            lfo_freq=lfo_freq_funct_m[0]*i+lfo_freq_funct_b[0]
        else:
            lfo_freq=lfo_freq_funct_m[1]*i+lfo_freq_funct_b[1]

        lfo_freq_string = "{0:.2f}".format(lfo_freq)
        if i == lfo_length-1:
            lfo_data += "\"Hz\"},\n"
        else:
            lfo_data += "\"" + str(lfo_freq_string)+"\", "

    lfo_data += "//lfo_amp\n"
    lfo_data += "{"
    for i in range(0,lfo_length):
        lfo_amp = (i + 1)/10.0
        lfo_amp_string = "{0:.2f}".format(lfo_amp)
        if i == lfo_length-1:
            lfo_data += "\"  \"},\n"
        else:
            lfo_data += "\"" + str(lfo_amp_string)+"\", "

    lfo_data += "//lfo_offset\n"
    lfo_data += "{"
    for i in range(0,lfo_length):
        lfo_offset = (i + 1)/10.0
        lfo_offset_string = "{0:.2f}".format(lfo_offset)
        if i == lfo_length-1:
            lfo_data += "\"  \"},\n"
        else:
            lfo_data += "\"" + str(lfo_offset_string)+"\", "

    return lfo_data

lfo_length = 101
def create_lfo_hostUi_array():
    lfo_data = "lutArray[7] = new String[]{"
    for i in range(0,lfo_length):
        if(i < 50):
            lfo_freq=lfo_freq_funct_m[0]*i+lfo_freq_funct_b[0]
        else:
            lfo_freq=lfo_freq_funct_m[1]*i+lfo_freq_funct_b[1]

        lfo_freq_string = "{0:.2f}".format(lfo_freq)
        if i == lfo_length-1:
            lfo_data += "\"Hz\"};\n"
        else:
            lfo_data += "\"" + str(lfo_freq_string)+"\", "

    lfo_data += "lutArray[8] = new String[]{"
    for i in range(0,lfo_length):
        lfo_amp = (i + 1)/10.0
        lfo_amp_string = "{0:.2f}".format(lfo_amp)
        if i == lfo_length-1:
            lfo_data += "\"  \"};\n"
        else:
            lfo_data += "\"" + str(lfo_amp_string)+"\", "

    lfo_data += "lutArray[9] = new String[]{"
    for i in range(0,lfo_length):
        lfo_offset = (i + 1)/10.0
        lfo_offset_string = "{0:.2f}".format(lfo_offset)
        if i == lfo_length-1:
            lfo_data += "\"  \"};\n"
        else:
            lfo_data += "\"" + str(lfo_offset_string)+"\", "

    return lfo_data


main_lfo_length = 100
def create_lfo_main_array():
    global lfo_sine_freq
    lfo_data = "const float lfoFreq["+str(main_lfo_length)+"] = {"
    print "LFO Frequency"
    for i in range(0,main_lfo_length):
        if(i < 50):
            lfo_freq=lfo_freq_funct_m[0]*i+lfo_freq_funct_b[0]
        else:
            lfo_freq=lfo_freq_funct_m[1]*i+lfo_freq_funct_b[1]
        lfo_freq_string = "{0:.2f}".format(lfo_freq)

        if i == main_lfo_length-1:
            lfo_data += str(lfo_freq_string)+"};\n"
        else:
            lfo_data += str(lfo_freq_string)+", "

    lfo_data += "const float lfoAmp["+str(main_lfo_length)+"] = {"
    print "LFO Amplitude"
    for i in range(0,main_lfo_length):
        lfo_amp = (i + 1)/10.0
        lfo_amp_string = "{0:.2f}".format(lfo_amp)

        if i == main_lfo_length-1:
            lfo_data += str(lfo_amp_string)+"};\n"
        else:
            lfo_data += str(lfo_amp_string)+", "

    lfo_data += "const float lfoOffset["+str(main_lfo_length)+"] = {"
    print "LFO Offset"
    for i in range(0,main_lfo_length):
        lfo_offset = (i)
        lfo_offset_string = "{0:.2f}".format(lfo_offset)

        if i == main_lfo_length-1:
            lfo_data += str(lfo_offset_string)+"};\n"
        else:
            lfo_data += str(lfo_offset_string)+", "

    lfo_data += "const float lfoSine["+str(lfo_sine_length)+"] = {"
    print "LFO Sine wave"
    for i in range(0,lfo_sine_length):
        lfo_sine = 10*math.sin(lfo_sine_freq*2*math.pi*i/lfo_sine_length)
        lfo_sine_string = "{0:.2f}".format(lfo_sine)

        if i == lfo_sine_length-1:
            lfo_data += str(lfo_sine_string)+"};\n"
        else:
            lfo_data += str(lfo_sine_string)+", "

    return lfo_data
