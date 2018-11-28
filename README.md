# HeaderFileBuilder
Script for creating value array header files FlxMain, FlxPedalUi, and FlxEditor.

The processes required a variety of data types.  While the Volume and Mixer processes simply needed floating point type data, the digital filter processes needed an array of filter coefficients.  When it came to being able to control the parameter settings of any given process, the simplest solution was to use an array of 100 of the data type, with 0 to 99 being the parameter value range. In addition to the process data types, user-interface data arrays were also written (i.e filter frequency, delay time, etc.)  Python scripts were written to create these various data arrays, with a parent script running each of these scripts and writing the data from each script to the header files
