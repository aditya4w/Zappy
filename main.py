import os
import json
from datetime import date

class StorageManager:
    def __init__(self):

        self.config_file = os.path.join(os.path.expanduser("~"), ".zpconfig.json")
        self.filename = ".zpdata.json"
        self.filepath = ""

    def setup(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    data = json.load(f)
                    self.filepath = data["path"]
                    if os.path.exists(self.filepath):
                        return 
            except:
                pass

        print("=== ZAPPY Needs Storage Permission For Work >w< ===")
        print("~ Where Should Zappy Store Your Data? ~")
        print("1. System (In Home Folder) - Recommended")
        print("2. Local (This folder)")
        
        choice = input("Select (1/2): ")

        if choice == "1":
            home_dir = os.path.expanduser("~") 
            folder_path = os.path.join(home_dir, ".zpstorage")
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Success! at {folder_path}")
            else:
                print("Unexpected Error!")
            
            self.filepath = os.path.join(folder_path, self.filename)
            
        else:
            self.filepath = self.filename

        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                f.write("[]")
            print("New Database Created!")
        else:
            print("Found Existing Database!")
        with open(self.config_file, "w") as f:
            json.dump({"path": self.filepath}, f)
        print("~ Setup Complete! ~")


    def get_path(self):
        return self.filepath

print ("~ HELLO THERE! I\'M ZAPPY >w< ~")

storage = StorageManager()
storage.setup()

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount 
        self.date = date

class ExpenseManager:
    def __init__(self):
       self.storage = StorageManager()
       self.storage.setup()
       self.filepath = self.storage.get_path()
       self.expenses = []
       self.load_expenses()

    def add_expenses(self):
        category = input("Enter Category [ex Food, Travel.,etc]: ")
        amount = input("Enter Amount: ")

        d_input= input("Date [Enter for Today]: ")
        if d_input == "":
           d_input = date.today().strftime("%d-%m-%Y")

        new_obj = Expense(category, amount, d_input)
        self.expenses.append(new_obj)
        self.save_expenses()
        print("~ Saved! ~")

    def save_expenses(self):
        temp_list = []
        for e in self.expenses:
            temp_list.append(e.__dict__)

        with open(self.filepath, "w") as f:
            json.dump(temp_list, f, indent=4)

    def load_expenses(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    raw_data = json.load(f)
                    
                self.expenses = []
                for item in raw_data:
                        obj = Expense(item['category'], item['amount'], item['date'])
                        self.expenses.append(obj)
            except:
                self.expenses = []
        else:
            self.expenses = []


    def smry_expenses(self):
        print("\n=== SUMMARY ===")
        
        if len(self.expenses) ==0:
            print("Nothing is here!")
            return
        for i, item in enumerate(self.expenses, 1):
            print(f"{i}. {item.date} | {item.category}: {item.amount}")
            
        print("----------------------------")

app = ExpenseManager()

while True:
  print("~ WHAT WOULD YOU LIKE TO DO? ~")
  print("1. Add Expense")
  print("2. Summary")
  print("3. Exit")

  choice = int(input(": "))
  if choice == 1:
    app.add_expenses()
  elif choice == 2:
    app.smry_expenses()
  elif choice == 3:
    print("BYE BYE! ^_^")
    break
  else:
      print("Invalid choice, try again!")
