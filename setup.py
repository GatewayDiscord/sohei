import os
import sys
sys.path.insert(0, os.path.abspath("..")) # this is for me to fix a local bug. not a part of the project itself.


from sohei import Models
from sohei.main import register, sanitise
import getpass


Models.db.create_all()
username=sanitise(input("Enter admin username: "))[1]
password=getpass.getpass()

res=register(username, password, "admin")
print(res)

if res!="Success":
    print("Try deleting test.db and try again.")
