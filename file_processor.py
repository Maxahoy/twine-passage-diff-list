#!python
import os
import sys
import path
from srx.mypkg.filefinder import *
#file processor
"""
TODO:
    - Take in lists of common files and generate list of common twine passages in each common file
    - Generate lists of twine packages in each additional modded file
    - Use those lists to find all passages which exist in an additional modded file but also exist somewhere in the original

"""

#return all passage names in file
def get_passages_in_file(twee_file):
    twee_file_line_list = []
    with open(twee_file) as file:
        lines = [line.rstrip() for line in file]
    passage_lines = [line.rstrip().split()[1] for line in twee_file_line_list if "::" in line]
    return passage_lines
        

# TODO
# INPUT: original file list, modded file list, original repo directory path, modded repo filepath
#
#
def find_common_passages_in_common_files(original_file_list, modded_file_list, original_repo="", modded_repo=""):
    # get a list of all passages in file a and file b
    # get list of common files first
    # create list of files by appending repo names to file names
    common_files = return_common_files(original_file_list, modded_file_list, original_repo, modded_repo)
    # get list of passages in these files
    passage_list = 

    #
    #



#TODO
#search through common files and find passages that only exist in the modded version
#also find passages that only exist in the common version
def find_extra_passages_in_common_files(original_file_list, modded_file_list, original_repo, modded_repo):


#TODO
# in case the modded files overwrite passages in the original
# modded file list should be those files which don't exist in the original
#return passages which exist in modded files (files NOT in original list) and 
# have a passage with the same name in the original file list
def find_overwritten_passages_in_modded_files(original_file_list, modded_file_list, original_repo, modded_repo):


#TODO
#in case the original is more up to date than the modded version
def find_passages_only_in_original(original_file_list, modded_file_list, original_repo, modded_repo):



