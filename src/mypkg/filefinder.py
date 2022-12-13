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

def return_common_files(original_file_list, modded_file_list, original_repo_name, modded_repo_name):
    #returns all files that share a directory + filename with something in the other structure
    #IE, if both contain a /home/user/original/twine/tests/file.twee and a /home/user/original/modded/twine/tests/file.twee then that directory (truncated to be inside of the respective repos) will be returned
    # but if one repo contains a twine/tests/file.twee and the other twine/src/file.twee, then that won't be returned

    #go through all the files in the original list truncate until after the appearance of "original repo name"
    # do the same operation except using the modded_repo_name on the other list
    original_file_list_reduced = original_file_list.split(original_repo_name, 1)[1]
    modded_file_list_reduced = modded_file_list.split(modded_repo_name, 1)[1]

    common = original_file_list_reduced.intersection(modded-file_list_reduced)
    return common

def modded_extra_files(original_file_list, modded_file_list, original_repo_name, modded_repo_name):
    original_file_list_reduced = original_file_list.split(original_repo_name, 1)[1]
    modded_file_list_reduced = modded_file_list.split(modded_repo_name, 1)[1]

    common = original_file_list_reduced.intersection(modded-file_list_reduced)
    #extras = modded_file_list_reduced - common
    extras = [filename for filename in modded_file_list_reduced if filename not in original_file_list_reduced]
    return extras




