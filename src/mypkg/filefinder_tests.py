#filefinder tests
import pytest
import sys
import os

cwd = os.getcwd()
print(cwd)
sys.path.insert(0, cwd)

from src.mypkg.filefinder import *

#TODO documentation & explanantion
"""
Since this is a personal project I'm not going to write a super extensive testing regimen,
 but hopefully this shows I know how to use basic pytest functions! Thanks for snooping :)

 Other test cases that I would consider using in this case but don't feel like spending time, 
 since this repo has one purpose on a personal project:

 - Testing out if the common files function can separate file directories properly (it can, but tests should show that)
 - Testing out if repos can be used on different drives (since Windows especially doesn't have location independence in its file system)
 - O
"""

#these versions don't have directory structures
original_base_case = ["a.txt", "b.txt", "c.txt"]
modded_base_case = ["a.txt", "b.txt", "c.txt", "d.txt"]

original_empty = []
modded_empty = []

original_expanded = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt"]
modded_expanded = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]

original_missing_middle = ["a.txt", "c.txt"]
modded_missing_middle = ["a.txt", "d.txt", "e.txt"]

#the same as above but with directory structures
def test_get_common_files_base_case():
    result = return_common_files(original_base_case, modded_base_case)
    expected = ["a.txt", "b.txt", "c.txt"]
    assert expected == result

#TODO
def test_get_common_files_empty():
    result = return_common_files(original_empty, modded_empty)

#TODO
def test_get_common_files_original_larger():
    

