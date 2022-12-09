#filefinder.py
import glob, os
from os import walk
from os import path
#input folder a

#takes an input original directory, and input modded directory, and returns all their applicable text files for twine development
# filetype to search for is paramaterized; if none given, then some common twine project files are searched for
# additional files can be appended to the new_extensions argument. By defulat, it'll search for txt, json, twee, js, css, and md files. 
# but others can be added if so desired.

#original_input_folder, modded_input_folder, filetype="", new_extensions=[]
#string,                string,              string,      list


def return_file_lists(original_input_folder, modded_input_folder, filetype="", new_extensions=[]):
    original_file_list = []
    modded_file_list = []

    common_twine_plaintext = ["txt","json","twee", "js", "css", "md"]
    common_twine_plaintext.append(new_extensions)

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
        for filetype in common_twine_plaintext:
            os.chdir(original_input_folder)
            print(str("'**/*."+filetype))
            print("Printing files in: ", os.getcwd())
            #for each filetype append to the list
            original_file_list.append(glob.glob(original_input_folder + '/**/*.'+filetype, recursive=True))
            modded_file_list.append(glob.glob(modded_input_folder + '/**/*.'+filetype, recursive=True))

    return original_file_list, modded_file_list



