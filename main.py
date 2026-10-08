from datetime import datetime
dt = datetime.now()

class Journal:

    def __init__(self):

        with open("journal.txt", "a") as file:
            print()

    def add(self):
        try:
            entry = input("Enter your journal entry:-")
            with open("journal.txt", "a") as file:
                file.write( entry + "\n " +str(dt)+ "\n")
                print("Entry added successfully !")
        except:
            print("Error: Failed to add entry.")

    def view(self):
        print("Your Journal Entries:")
        print("")
        try:
            with open("journal.txt", "r") as file:
                data = file.read()
                print(f"{data}```")
        except:
            print("Error: Failed to read journal entries.")

    def search(self):
        try:
            with open("journal.txt", "r") as file:
                find = input("Enter a Keyword or data to search:- ")
                print("Matching Entries :")
                print("")

                for i in file:
                    if find in i:
                        print(f"{i}[{dt}]")
                        break
                else :
                    print("Not Found")
        except:
            print("Error: Failed to search journal entries.")

    def delete(self):
        try:
            entries = input("Are you sure you want to delet all entries? (yes/no):- ").strip().lower()
            if entries == "yes":
                with open("journal.txt", "w") as file:
                    file.write("")
                    print("All journal entries have been deleted.")
            elif entries == "no":
                print("No journal entries to delete.")

            else:
                print("please Select (yes-no)")
        except:
            print("Error: Failed to delete journal entries.")

journal = Journal()

while True:
    print("Welcome to Personal Journal Manager!")
    print()
    print("Please select an option:")
    print("1. Add a new Entry ")
    print("2. View All Entries ")
    print("3. Search for an Entry ")
    print("4. Delete All Entries ")
    print("5. Exit")

    try:
        choice = int(input("User Input :-"))
    except :
        print("Enter Only (1to5).")

    if choice == 1:
        journal.add()

    elif choice == 2:
        journal.view()

    elif choice == 3:
        journal.search()

    elif choice == 4:
        journal.delete() 

    elif choice == 5:
        print("Thank you for using personal Journal Manager. GoodBye!")
        break      

    else:
        print("Invalid option. please select a valid option from the menu.")