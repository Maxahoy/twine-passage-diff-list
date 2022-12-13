#run test suite inside test folder
import pytest
import os
import sys

cwd = os.getcwd()
#sys.path.insert(0, )

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finished")

if __name__ == "__main__":
    returncode = pytest.main(["-x"])
    sys.exit()