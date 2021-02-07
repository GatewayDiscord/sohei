import os
import sys

sys.path.insert(0, os.path.abspath("..")) # this is for me to fix a local bug. not a part of the project itself.


from sohei import Models
from sohei.main import register, sanitise
import json
import getpass

Models.db.create_all()
username=sanitise(input("Enter admin username: "))[1]
password=getpass.getpass()

while True:
    if " " in password:
        print("Password can't contain space.")
    else:
        break
    password=input("Enter admin password: ")

teamname=input("Enter team-name [Leave blank for it to just say Gateway]: ").replace('}','').replace('{','').replace('\"',"").replace('\'','')

if teamname==" " or teamname=="":
    teamname="Gateway"

slogan=input('Enter custom slogan [Leave it blank for it to just say the default slogan.]: ').replace('{','').replace('\"',"").replace('\'','')

if slogan==" " or slogan=="":
    slogan="A framework for CTF Teams to play CTFs in order to win them."


res=register(username, password, "admin")


with open(__file__[:-8]+'config.json', 'w+') as file:
    json_to_save={"team_name":teamname,
            "head_text":slogan}
    data=json.dumps(json_to_save)
    file.write(data)

print(res)


if res!="Success":
    print("Try deleting test.db and try again.")
