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

    def depositmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))

        userdata = None
        for i in Bank.data:
            if i['accountNo'] == accnumber and i['pin'] == pin:
                userdata = i
                break

        if userdata is None:
            print("❌ Sorry, no data found")
        else:
            amount = int(input("How much you want to deposit :- "))
            if amount > 10000 or amount <= 0:
                print("❌ Sorry, this amount is invalid. You can deposit up to 10,000 and above 0.")
            else:
                userdata['balance'] += amount
                Bank.__update()
                print("✅ Amount deposited successfully")
            

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

if check == 2:
    user.depositmoney()
