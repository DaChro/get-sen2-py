# This script simply executes the sen2cor processor on all unzipped L1C files created
# by unzip_sentinel2.py
# sen2cor needs to be installed (standalone installer) and the direcetory containing
# "L2A_Process.bat" needs to be added to path system environment variable
# Takes one input argument, the directory where the unzipped L1C files are

from sys import argv
from os import system

import os


def run_correction(wd):
    # list level 1C files in folder
    L1Cfiles = [s for s in os.listdir(wd) if "L1C" in s]
    print(str(len(L1Cfiles)) + ' level 1C file(s) found. Performing atmospheric correction.')

    # run sen2cor on level 1C files
    for file in L1Cfiles:
        command = 'L2A_Process ' + os.path.join(wd, file) + ' --resolution=10'
        system(command)
        #print('Atmospheric correction finished for ' + file)

    print('Finished.')


if __name__ == "__main__":
    run_correction(argv[1])
