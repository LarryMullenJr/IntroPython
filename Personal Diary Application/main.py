import os
import datetime

def write_diary_entry(entry, filename='diary.txt', add_timestamp=False):
    try:
        with open(filename, 'a') as file:
            if add_timestamp:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}\n")
            file.write(entry + "\n")
        print("Entry added successfully.")
    except Exception as e:
        print(f"Error occurred while writing the entry: {e}")

def read_diary_entries(filename='diary.txt'):
    try:
        with open(filename, 'r') as file:
            entries = file.readlines()
        if not entries:
            print("No entries found.")
        else:
            for entry in entries:
                print(entry.strip())
    except FileNotFoundError:
        print("Diary file not found.")
    except PermissionError:
        print("Permission denied to access the diary file.")
    except Exception as e:
        print(f"Error occurred while reading the entries: {e}")

def main():
    while True:
        print("\n*** Personal Diary Application ***")
        print("1. Write a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            entry = input("Enter your diary entry: ")
            add_timestamp = input("Do you want to add a timestamp to this entry? (yes/no): ").lower() == 'yes'
            write_diary_entry(entry, add_timestamp=add_timestamp)
        elif choice == '2':
            read_diary_entries()
        elif choice == '3':
            print("Exiting the diary application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()