#run test suite inside test folder
import pytest
import os
import sys
from tests import filefinder_tests
from lib import filefinder

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finished")

if __name__ == "__main__":
    filefinder_tests.basic_test()
    sys.exit()