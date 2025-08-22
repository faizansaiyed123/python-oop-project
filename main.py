import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():  
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No Such File Exists")
    except Exception as err:
        print(f"An exception occurred: {err}")
        
    def Createaccount(self):
        pass


user = Bank() 
print("====== Bank Management System ======")
print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Account Details")
print("6. Delete Account")
print("====================================")

check = int(input("Tell your response: "))

if check == 1:
    user.Createaccount()
