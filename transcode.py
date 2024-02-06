###########
# Created by Joseph Hale
#
# Simple script to transcode MKV files from blu-ray to M4V in batch
# Creates screen sessions for each movie to check progress
#
##########


import os
#base directory for all dvd/blu-ray rips
directory = "/home/joseph/plexdata/makemkvout"
#loop through all sub directories which are each disc rip
for root, dirs, files in os.walk(directory):
    for direct in dirs:
        for subroot, subdir, subfiles in os.walk("/home/joseph/plexdata/makemkvout/"+direct):
#vars to find largest file for each directory (this is most likely the main feature film but not 100% make sure to check files after transcode)
            largestFile = None
            largestSize = 0
#loop through each file in the sub-directory
            for file in subfiles:
#get the file name and size
                file_path = os.path.join(subroot, file)
                file_size = os.path.getsize(file_path)
#check if the current file is the largest
                if(file_size > largestSize):
                    largestFile = file_path
                    largestSize = file_size
#get movie name for file creation
            if largestFile is not None:
                fileName = largestFile.rsplit('/', 1)[-1]
                fileName = fileName.rsplit('.', 1)[0]
                print(f"screen -dm HandBrakeCLI -Z 'HQ 1080p30 Surround' -i '{largestFile}' -o '/home/joseph/plexdata/movies/{fileName}.m4v'")
