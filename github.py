import os
import shutil
import subprocess
import sys
from array import *
import multiprocessing as mp
import time
import glob

home = '/data/cxg5395'
tempFolder = '/home/cxg5395/temp'

if not os.path.exists(tempFolder):
        os.makedirs(tempFolder)
if not os.path.exists(home):
        os.makedirs(home)
        
def execute_Command(apply_files):
        callResult = 'curl -s --form input=@' + apply_files + ' localhost:8080/processHeaderDocument'

        output = subprocess.check_output(callResult, shell = True, universal_newlines=True)
        fileLocation = tempFolder + '/' + (os.path.basename(apply_files)).replace('.pdf','.tei.xml')

        if os.path.exists(fileLocation):
                return
        with open(fileLocation, "w") as f:
                f.write(output)
                #print('successfully wrote file at: ' + fileLocation)
                f.close()
        dstdir = home + '/' + (os.path.basename(apply_files)).replace('.pdf','').replace('.','/')
        if not os.path.exists(dstdir): os.makedirs(dstdir)
        cmd_mv = 'mv' + ' ' + fileLocation + ' ' + dstdir + '/ '
        #print('successfully moved file from: ' + cmd_mv)
        subprocess.call(cmd_mv, shell = True)
        #reates the directory
def apply_async_with_callback():
        pool = mp.Pool(processes=10)
        with open('/data/cxg5395/citeseerx-repo-snapshot-path-pdf.txt') as g:
                for line in g:
                        #print(fileList)
                        pool.apply_async(execute_Command, args = (line.strip(), ))
        pool.close()
        pool.join()

if __name__ == '__main__':
        apply_async_with_callback()
