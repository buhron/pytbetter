# Handled by env
"""
Python with better actions
"""
import os
import sys
from os import dirlist
from pytbetter.__init__ import *
listOfFilesofDir = dirlist

def bashExec(command):
  """With the module os, we used os.system to run in bash instead of sh"""
 os.system(f"bash -c '{command}'")

class Engine:
   """
   Parts of the engine.
   """

   dir = os.environ['PWD']
   def part(ans):
     return sys.executable
   def send(command: object, class: bool):
      f"""
      Sends the executable that is being runned.
      It would be /usr/bin/python3.9 on Linux,
      or in virtualenv, it would be {os.environ['HOME']}/<root project dir>/venv/bin/python or python3.9
      or {sys.executable}.
      """
      insert = Engine.part
      return insert(command)
    class _self:
     homeitems = dirlist(os.environ['HOME'])
