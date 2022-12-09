#filefinder.py
import glob, os
from os import walk
from os import path
#input folder a

original_input_folder = "/home/maxahoy/xchange-life"
modded_input_folder = "/home/maxahoy/xchange-life-oral-mod"
filetype = "twee"
filetype = ""

#common files to include in twine formats include
common_plaintext = ["txt","json","twee", "js", "css", "md"]

original_file_list = []
modded_file_list = []

#if input args exist, replace the three above vars maybe?

#if we are given a specific filetype to look for, then only get that list
if filetype:
    os.chdir(original_input_folder)
    print(str("'**/*."+filetype))
    print("Printing files in: ", os.getcwd())
    original_file_list = glob.glob(original_input_folder + '/**/*.'+filetype, recursive=True)
    modded_file_list = glob.glob(modded_input_folder + '/**/*.'+filetype, recursive=True)
    #print(original_file_list)
    #os.chdir(modded_input_folder)
    #for file in glob.glob("*."+filetype):
        #create file list for modded version
        #print(file)
else:
    #just get all using common plaintext formats in twine projects
    #included are 
    for filetype in common_plaintext:
        os.chdir(original_input_folder)
        print(str("'**/*."+filetype))
        print("Printing files in: ", os.getcwd())
        #for each filetype append to the list
        original_file_list.append(glob.glob(original_input_folder + '/**/*.'+filetype, recursive=True))
        modded_file_list.append(glob.glob(modded_input_folder + '/**/*.'+filetype, recursive=True))

return original_file_list, modded_file_list



