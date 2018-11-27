import os
import sys

from ofx_filter3bb_2ndOrder_ValueArray_functions import * # lp and hp arrays
from ofx_filter3bb_3rdOrder_ValueArray_functions import * # lp and hp arrays
from ofx_filter3bb2_2ndOrder_ValueArray_functions import * # lp and hp arrays
from ofx_filter3bb2_3rdOrder_ValueArray_functions import * # lp and hp arrays
from ofx_lohifilterValueArray_functions import * # lp and hp arrays
from ofx_delayValueArray_functions import * # delay array
from ofx_amplitudeValueArray_functions import * # linear and logarithmic array
from ofx_envGenValueArray_functions import * # envelope generator times
from ofx_lfoValueArray_functions import *   # low frequency oscillator freq, amplitude, offset, and waveforms
from ofx_waveshaperBpArray_functions import * # breakpoint array
from ofx_couplingFilterCoefs_functions import *
from ofx_noiseFilterCoefs_functions import *
from ofx_antiAliasingFilterCoefs_functions import *




def create_ofx_main_file(ofx_main_fd):
    ofx_main_fd.write("#ifndef LOOKUPTABLE_H_\n")
    ofx_main_fd.write("#define LOOKUPTABLE_H_\n")
    ofx_main_fd.write("\n")
    ofx_main_fd.write("#include <string>\n")
    ofx_main_fd.write("#include <cstring>\n")
    ofx_main_fd.write("\n")
    ofx_main_fd.write("\n")
    ofx_main_fd.write("namespace std{\n")

    #   0:amplitude
    ofx_main_fd.write(create_amplitude_main_array())

    #   3:filter frequency
    ofx_main_fd.write("#if(FILTER_ORDER == 2)\n")
    ofx_main_fd.write(create_filter3bb_2ndOrder_main_array())
    ofx_main_fd.write("#elif(FILTER_ORDER == 3)\n")
    ofx_main_fd.write(create_filter3bb_3rdOrder_main_array())
    ofx_main_fd.write("#endif\n")

    #   3:filter2 frequency
    ofx_main_fd.write("#if(FILTER_ORDER == 2)\n")
    ofx_main_fd.write(create_filter3bb2_2ndOrder_main_array())
    ofx_main_fd.write("#elif(FILTER_ORDER == 3)\n")
    ofx_main_fd.write(create_filter3bb2_3rdOrder_main_array())
    ofx_main_fd.write("#endif\n")

    #   3:lohifilter frequency
    ofx_main_fd.write(create_lohifilter_main_array())

    #   4,5:delay time (Coarse & Fine)
    ofx_main_fd.write(create_delay_main_array())

    #   6:envlope generator time
    ofx_main_fd.write(create_envGen_main_array())

    #   7:LFO frequency, 8:LFO amplitude, 9:LFO offset
    ofx_main_fd.write(create_lfo_main_array())

    #   10:waveshaper edge breakpoint
    ofx_main_fd.write(create_breakpoint_main_array())

    ofx_main_fd.write(create_coupler_main_coefs())
    ofx_main_fd.write(create_noiseFilter_main_coefs())
    ofx_main_fd.write(create_antiAliasingFilter_main_coefs())
    ofx_main_fd.write("}\n")
    ofx_main_fd.write("#endif")



def create_ofx_pedalUi_file(ofx_pedalUi_fd):
    ofx_pedalUi_fd.write("#ifndef LOOKUPTABLE_H_\n")
    ofx_pedalUi_fd.write("#define LOOKUPTABLE_H_\n")
    ofx_pedalUi_fd.write("\n")
    ofx_pedalUi_fd.write("#include <string>\n")
    ofx_pedalUi_fd.write("#include <cstring>\n")
    ofx_pedalUi_fd.write("\n")
    ofx_pedalUi_fd.write("\n")
    ofx_pedalUi_fd.write("namespace std{\n")

    ofx_pedalUi_fd.write("string lutArray[11][101] = {\n")
    #   0:lin amplitude, 1: dB amplitude 2:log amplitude
    ofx_pedalUi_fd.write(create_linAmplitude_pedalUi_array())
    #   3:filter frequency
    ofx_pedalUi_fd.write(create_freq_pedalUi_array())
    #   4:coarse delay time,  5:fine delay time
    ofx_pedalUi_fd.write(create_delay_pedalUi_array())
    #   6:envlope generator time
    ofx_pedalUi_fd.write(create_envGen_pedalUi_array())
    #   7:LFO frequency, 8:LFO amplitude,9: LFO offset
    ofx_pedalUi_fd.write(create_lfo_pedalUi_array())
    #   10:waveshaper edge breakpoints
    ofx_pedalUi_fd.write(create_breakpoint_pedalUi_array())
    ofx_pedalUi_fd.write("};\n")
    ofx_pedalUi_fd.write("}\n")
    ofx_pedalUi_fd.write("#endif")

def create_ofx_hostUi_file(ofx_hostUi_fd):
    ofx_hostUi_fd.write("package diagramSubComponents;\n")
    ofx_hostUi_fd.write("import java.util.ArrayList;\n")
    ofx_hostUi_fd.write("import java.util.List;\n")
    ofx_hostUi_fd.write("public class LookUpTableTest {\n")
    ofx_hostUi_fd.write("	String[][] lutArray = new String[101][11];\n")
    ofx_hostUi_fd.write("	public LookUpTable()\n")
    ofx_hostUi_fd.write("	{\n")
	# #   0:lin amplitude, 1: dB amplitude 2:log amplitude
    ofx_hostUi_fd.write("	// amplitude: lin,dB,log\n")
    ofx_hostUi_fd.write(create_amplitude_hostUi_array())
    # #   3:filter frequency
    ofx_hostUi_fd.write("	// filterFreq\n")
    ofx_hostUi_fd.write(create_freq_hostUi_array())
    # #   4:coarse delay time,  5:fine delay time
    ofx_hostUi_fd.write("	// delayTime: Coarse,Fine\n")
    ofx_hostUi_fd.write(create_delay_hostUi_array())
    # #   6:envlope generator time
    ofx_hostUi_fd.write("	// envTime\n")
    ofx_hostUi_fd.write(create_envGen_hostUi_array())
    # #   7:LFO frequency, 8:LFO amplitude,9: LFO offset
    ofx_hostUi_fd.write("	// lfoFreq, lfoAmp, lfoOffset\n")
    ofx_hostUi_fd.write(create_lfo_hostUi_array())
    # #   10:waveshaper edge breakpoints
    ofx_hostUi_fd.write("	// edge\n")
    ofx_hostUi_fd.write(create_breakpoint_hostUi_array())
    ofx_hostUi_fd.write("}\n");
    ofx_hostUi_fd.write("public String getParameterValueString(int parameterType, int parameterValueIndex)\n");
    ofx_hostUi_fd.write("{\n");
    ofx_hostUi_fd.write("\tString output = \"\";\n");
    ofx_hostUi_fd.write("\tif(0<=parameterValueIndex && parameterValueIndex < 100)\n");
    ofx_hostUi_fd.write("\t{\n");
    ofx_hostUi_fd.write("\t\toutput = lutArray[parameterType][parameterValueIndex] + \" \" + lutArray[parameterType][100];\n")
    ofx_hostUi_fd.write("\t}\n");
    ofx_hostUi_fd.write("\treturn output;\n");
    ofx_hostUi_fd.write("}}\n");


def main(argv):

    target_directory = argv[0]
    ofx_main_file_string_CM1 = target_directory + "/FlxMainCM1DataArray.h"
    ofx_pedalUi_file_string_CM1 = target_directory + "/FlxPedalUiCM1ValueArray.h"
    ofx_hostUi_file_string = target_directory + "/LookUpTable.java"
    ofx_main_fd_CM1 = open(ofx_main_file_string_CM1,'w+')
    ofx_pedalUi_fd_CM1 = open(ofx_pedalUi_file_string_CM1,'w+')
    ofx_hostUi_fd = open(ofx_hostUi_file_string,'w+')

    create_ofx_main_file(ofx_main_fd_CM1)
    create_ofx_pedalUi_file(ofx_pedalUi_fd_CM1)
    create_ofx_hostUi_file(ofx_hostUi_fd)

    ofx_main_fd_CM1.close()
    ofx_pedalUi_fd_CM1.close()
    ofx_hostUi_fd.close()

if __name__ == "__main__":
   main(sys.argv[1:])
