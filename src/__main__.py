# Handled by env
import os
from os import dirlist
from pytbetter.__init__ import *
listOfFilesofDir = dirlist
def bashExec(command):
 os.system(f"bash -c '{command}'")
