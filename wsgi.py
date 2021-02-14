import os
import sys

sys.path.insert(0, os.path.abspath("..")) # this is for me to fix a local bug. not a part of the project itself.
from sohei import app


if __name__=="__main__":
    app.run()
