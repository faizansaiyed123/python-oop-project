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
        data = {
            "name": input("Tell Your Name :- "),
            "age": int(input("Tell Your Age :- ")),
            "email": input("Tell Your Email :- "),
            "pin": int(input("Tell 4 number Your Pin :- ")),
            "accountNo": random.randint(10000000, 99999999),  # random account no
            "balance": 0
        }

        # ✅ fixed condition (age check, pin length, email check)
        if data["age"] < 18 or len(str(data["pin"])) != 4 or "@" not in data["email"]:
            print("❌ Sorry, you cannot create an account")
        else:
            print("✅ Account has been created successfully")
            for k, v in data.items():
                print(f"{k}: {v}")
            print("⚠️ Please note down your account number")

            Bank.update(data)   # <-- this will fail unless you define update()
            

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
