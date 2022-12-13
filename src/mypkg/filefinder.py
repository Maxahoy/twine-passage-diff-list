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

    if filetype:
        os.chdir(original_input_folder)
        newlist = glob.glob(original_input_folder + '/**/*.'+filetype, recursive=True)
        print(type(newlist))
        print(newlist)
        original_file_list.append(newlist)
        os.chdir(modded_input_folder)
        newlist = glob.glob(modded_input_folder + '/**/*.'+filetype, recursive=True)
        print(type(newlist))
        print(newlist)
        modded_file_list.append(newlist)

    else:
        for filetype in common_twine_plaintext:
            os.chdir(original_input_folder)
            print(type(original_file_list))
            print(type(modded_file_list))
            newlist = glob.glob(original_input_folder + '/**/*.'+filetype, recursive=True)
            print(type(newlist))
            print(newlist)
            original_file_list.append(newlist)
            os.chdir(modded_input_folder)
            newlist = glob.glob(modded_input_folder + '/**/*.'+filetype, recursive=True)
            print(type(newlist))
            print(newlist)
            modded_file_list.append(newlist)

    return original_file_list, modded_file_list



