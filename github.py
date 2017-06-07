import os
import shutil
import subprocess
import sys
from array import *
import multiprocessing as mp
import time
import glob

home = '/home/cxg5395/grobid_result'
tempFolder = '/home/cxg5395/temp'
documentDirectory = '/home/cxg5395/citeseerx-crawl-labeled-sample-b/pdf/'
if not os.path.exists(tempFolder):
        os.makedirs(tempFolder)
if not os.path.exists(home):
        os.makedirs(home)
start_time = time.time()
def execute_Command(apply_files):
        callResult = 'curl -s --form input=@' + apply_files + ' localhost:8080/processHeaderDocument'
        output = subprocess.check_output(callResult, shell = True, universal_newlines=True)
        fileLocation = tempFolder + '/' + apply_files.replace('.pdf', '.tei.xml').replace(documentDirectory, '')
        #print(fileLocation)
        with open(fileLocation, "w") as f:
                f.write(output)
                #print('successfully wrote file at: ' + fileLocation)
                f.close()
        if os.path.exists(fileLocation):
                return
        dstdir = home + '/' + apply_files.replace('.pdf','').replace('.','/').replace(documentDirectory, '')
        if not os.path.exists(dstdir): os.makedirs(dstdir)
        cmd_mv = 'mv' + ' ' + fileLocation + ' ' + dstdir + '/ '
        #print('successfully moved file from: ' + cmd_mv)
        subprocess.call(cmd_mv, shell = True)
        #creates the directory



def apply_async_with_callback():
        pool = mp.Pool(processes=16)
        files = glob.glob(os.path.join(documentDirectory,"*.pdf"))
        for i in range(len(files)):
                pool.apply_async(execute_Command, args = (files[i], ))
        pool.close()
        pool.join()
        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
        apply_async_with_callback()