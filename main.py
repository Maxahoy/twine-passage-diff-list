#main file for diff detector; 
"""
Purpose 

Main guy here; this file grabs two repositories from github, displays their two structures so the user can confirm they're broadly similar
Recursively searches through files and generates a list of twine passages that exist in common structure between the two repos -- first by name only
Presents that list to the user for confirmation along with their contained files
Goes through each file, identifies passages with identical contents and passages with differing contents
Also identifies passages existing in one version and not the other

Should take in some command line arguments
original repo directory for original twine project
modded repo for modded twine projectg

Todo now, write function to go through files found and 

"""

