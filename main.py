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

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountgenerate(cls):
        alph = random.choices(string.ascii_letters , k=3)
        num = random.choices(string.digits , k=3)
        spchar = random.choices("!@#$%^&*()_+=-",k=1)
        id = alph + num + spchar
        random.shuffle(id)
        return "".join(id)
        
    def Createaccount(self):
        info = {
            "name": input("Tell Your Name :- "),
            "age": int(input("Tell Your Age :- ")),
            "email": input("Tell Your Email :- "),
            "pin": int(input("Tell 4 number Your Pin :- ")),
            "accountNo": Bank.__accountgenerate(),
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
            Bank.__update()
            

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
