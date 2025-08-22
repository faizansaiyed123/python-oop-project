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

    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
        
    def Createaccount(self):
        info = {
            "name": input("Tell Your Name :- "),
            "age": int(input("Tell Your Age :- ")),
            "email": input("Tell Your Email :- "),
            "pin": int(input("Tell 4 number Your Pin :- ")),
            "accountNo": random.randint(10000000, 99999999),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4 or "@" not in info["email"]:
            print("❌ Sorry, you cannot create an account")
        else:
            print("✅ Account has been created successfully")
            for k, v in info.items():
                print(f"{k}: {v}")
            print("⚠️ Please note down your account number")
            
            Bank.data.append(info)
            Bank.update()
            

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
