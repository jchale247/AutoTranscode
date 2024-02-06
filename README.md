# AutoTranscode
This is a simple python script to find all the MKV files from my blu-ray library rip files and automatically transcode them with HandBrake on a batch schedule

When I rip my blu-ray disc's they are ripped as large MKV files, I made this program to run once a day at an early hour to batch prosses my MKV files if there are any to rip. (or the program can be triggered when needed if not nightly) 

The python script loops through all sub directories (each movie) and finds the largest file (this is usualy the picture length film but not always, make sure to check the output file before deleting the MKV files)

It creates a screen session so I can check the progress of the transcoding. Make sure to change the base directory and the output directory of the screen command!
