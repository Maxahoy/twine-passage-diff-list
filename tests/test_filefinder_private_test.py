#filefinder tests
import pytest
import sys
import os

cwd = os.getcwd()
print(cwd)
sys.path.insert(0, cwd)

from src.mypkg.filefinder import *

#@base_test
#returns original file list then modded file list
def test_basic_print_test_twee():
    original_input_folder = "/home/maxahoy/xchange-life"
    modded_input_folder = "/home/maxahoy/xchange-life-oral-mod"
    filetype = "twee"
    new_extensions = []
    original, modded = return_file_lists(original_input_folder, modded_input_folder, filetype, new_extensions)

    print("Original\n",original)
    print("Modded\n", modded)

def test_basic_print_test_allfiles():
    original_input_folder = "/home/maxahoy/xchange-life"
    modded_input_folder = "/home/maxahoy/xchange-life-oral-mod"
    new_extensions = []
    original, modded = return_file_lists(original_input_folder, modded_input_folder)

    print("Original\n",original)
    print("Modded\n", modded)