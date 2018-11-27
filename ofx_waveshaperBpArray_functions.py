import os
import sys
import matplotlib.pyplot as y1_plt
import matplotlib.pyplot as y2_plt
import matplotlib.pyplot as y3_plt
import matplotlib.pyplot as y4_plt

# VALUE ARRAYS FOR WAVESHAPER BREAKPOINTS

brkpt_length = 101
brkpt_count = 5
x = range(0,brkpt_length)
brkpt = [[0.0]*brkpt_count for i in range(brkpt_length)]
brkpt_max = 1.5


def create_breakpoint_pedalUi_array():

    brkpt_data = "//edge\n"
    brkpt_data +="{"
    for i in range(0,brkpt_length):
        brkpt = i/10.0

        if i == brkpt_length-1:
            brkpt_data += "\"  \"}"
        else:
            brkpt_data += "\"" + str(brkpt)+"\", "
    return brkpt_data

def create_breakpoint_hostUi_array():


    brkpt_data ="lutArray[10] = new String[]{"
    for i in range(0,brkpt_length):
        brkpt = i/10.0

        if i == brkpt_length-1:
            brkpt_data += "\"  \"};\n"
        else:
            brkpt_data += "\"" + str(brkpt)+"\", "
    return brkpt_data

brkpt = [[0.0]*brkpt_count for i in range(100)]

main_brkpt_length = 100
def create_breakpoint_main_array():
    brkpt_data = "const float brkpt["+str(main_brkpt_length)+"]["+str(brkpt_count)+"] = {"
    print "waveshaper breakpoints"
    for i in range(0,main_brkpt_length):
        brkpt[i][0] = brkpt_max - (5*brkpt_max/600)*(main_brkpt_length - i)
        brkpt[i][1] = brkpt_max - (4*brkpt_max/600)*(main_brkpt_length - i)
        brkpt[i][2] = brkpt_max - (3*brkpt_max/600)*(main_brkpt_length - i)
        brkpt[i][3] = brkpt_max - (2*brkpt_max/600)*(main_brkpt_length - i)
        brkpt[i][4] = brkpt_max - (brkpt_max/600)*(main_brkpt_length - i)
        string = "{%f,%f,%f,%f,%f}" % (brkpt[i][0],brkpt[i][1],brkpt[i][2],brkpt[i][3],brkpt[i][4])
        if i == main_brkpt_length-1:
            brkpt_data += string+"};\n"
        else:
            brkpt_data += string+","

    return brkpt_data
