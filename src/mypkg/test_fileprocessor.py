#fileprocessor tests
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

 - Testing out if the common files function can separate file directories properly
     (it can, and tests on my local drive showed that, but I'm not putting my filesystem's info on github)
 - Testing out if repos can be used on different drives (since Windows especially doesn't have location independence in its file system)
 
"""

#TODO: test get passages in file

#TODO: create passages case
#input a twee file in this case
#the same as above but with directory structures
testcase = "basic_twee_file_test.twee"
def test_get_passages_in_file():
    result = return_common_files(original_base_case, modded_base_case)
    expected = ["a.txt", "b.txt", "c.txt"]
    assert expected == result