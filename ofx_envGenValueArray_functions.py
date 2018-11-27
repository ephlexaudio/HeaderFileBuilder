import os
import sys
import math
from scipy import signal



envTime_length = 101

def create_envGen_pedalUi_array():
    envTime_data = "//envTime\n"
    envTime_data += "{"
    for i in range(0,envTime_length):
        envTime = (i + 1)/10.0
        envTime_string = "{0:.2f}".format(envTime)
        if i == envTime_length-1:
            envTime_data += "\"S\"},\n"
        else:
            envTime_data += "\"" + str(envTime_string)+"\", "
    return envTime_data

envTime_length = 101
def create_envGen_hostUi_array():
    envTime_data = "lutArray[6] = new String[]{"
    for i in range(0,envTime_length):
        envTime = (i + 1)/10.0
        envTime_string = "{0:.2f}".format(envTime)
        if i == envTime_length-1:
            envTime_data += "\"S\"};\n"
        else:
            envTime_data += "\"" + str(envTime_string)+"\", "
    return envTime_data

main_envTime_length = 100
def create_envGen_main_array():
    envTime_data = "const float envTime["+str(main_envTime_length)+"] = {"
    print "LFO Frequency"
    for i in range(0,main_envTime_length):
        envTime = (i + 1)/10.0
        envTime_string = "{0:.2f}".format(envTime)

        if i == main_envTime_length-1:
            envTime_data += str(envTime_string)+"};\n"
        else:
            envTime_data += str(envTime_string)+", "
    return envTime_data
