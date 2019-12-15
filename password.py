from hashlib import sha256
from getpass import getpass
import os
from pathlib import Path


try:
    PassFileDir = str(Path(__file__).parent) + "/passwd.sha256"
    print("\nYou need this password when using critical command (reboot , shutdown , kill) \n")
    while True:
        final_passwd = ""
        first_passwd = getpass("\nEnter new password: ",stream=None)
        second_passwd = getpass("Enter new password again: ",stream=None)

        if str(first_passwd) == str(second_passwd):
            final_passwd = str(first_passwd)
            if len(final_passwd) < 4:
                print("Password must be at least 4 characters!")
            else:
                break
        else:
            print("Password not matches!!")


    with open(PassFileDir,"w") as passFile:
        passFile.write(sha256(final_passwd.encode("utf-8")).hexdigest())

    print("Password update succesfull")

except Exception as err:
    print(err)
