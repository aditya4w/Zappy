import os
import json

class StorageManager:
    def __init__(self):
        self.filename = ".zpdata.json"

        self.filepath = ""

    def setup(self):
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
            
            self.filepath = os.path.join(folder_path, self.filename)
            
        else:
            self.filepath = self.filename
            print("[Note] Creating file in current folder...")

        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                f.write("[]")
            print("~ New Database Created ~")
        else:
            print("~ Found Existing Database ~")

    def get_path(self):
        return self.filepath

print ("~ HELLO THERE! I\'M ZAPPY.,~")

storage = StorageManager()
storage.setup()
print(f"Saving Data In {storage.get_path()}")
print("~ Thank You for the Permissions >w< ~")

class Expense:
    def __init__(self, category, amount, date):
        pass

class ExpenseManager:
    pass


