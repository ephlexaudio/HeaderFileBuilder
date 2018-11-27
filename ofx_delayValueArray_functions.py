import os
import sys
import math
from scipy import signal

value = [[""]*256]*3


time_length = 101
delay_length = 100


def create_delay_pedalUi_array():
    time_data = "//delayCoarse\n"
    time_data += "{"
    for i in range(0,time_length):
        time = i*25

        if i == time_length-1:
            time_data += "\"mS\"},\n"
        else:
            time_data += "\"" + str(time)+"\", "
    time_data += "//delayFine\n"
    time_data += "{"
    for i in range(0,time_length):
        time = i*0.25

        if i == time_length-1:
            time_data += "\"mS\"},\n"
        else:
            time_data += "\"" + str(time)+"\", "
    return time_data

time_length = 101
def create_delay_hostUi_array():
    time_data = "lutArray[4] = new String[]{"
    for i in range(0,time_length):
        time = i*25

        if i == time_length-1:
            time_data += "\"mS\"};\n"
        else:
            time_data += "\"" + str(time)+"\", "
    time_data += "lutArray[5] = new String[]{"
    for i in range(0,time_length):
        time = i*0.25

        if i == time_length-1:
            time_data += "\"mS\"};\n"
        else:
            time_data += "\"" + str(time)+"\", "
    return time_data


def create_delay_main_array():
    delay_data = "const unsigned int delayTimeCoarse["+str(delay_length)+"] = {"

    print "delayCoarse"
    for i in range(0,delay_length):
        time = i*25*48 # no multiplication in code
        if i == delay_length-1:
            delay_data += str(time)+ "};\n"
        else:
            delay_data += str(time)+","
    delay_data += "const unsigned int delayTimeFine["+str(delay_length)+"] = {"

    print "delayFine"
    for i in range(0,delay_length):
        time = i*12 # no mulltiplication in code, creates increments of 0.5 seconds with a max of 50 ms
        if i == delay_length-1:
            delay_data += str(time) + "};\n"
        else:
            delay_data += str(time)+","
    return delay_data
