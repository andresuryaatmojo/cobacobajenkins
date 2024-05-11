# main.py
from auth import login
from input_form import get_user_input
from process_data import process_data

def main():
    print("Welcome to the Simple App")
    username, password = get_user_input()
    if login(username, password):
        print("Login successful!")
        data = input("Please enter some data to process: ")
        result = process_data(data)
        print(f"Processed data: {result}")
    else:
        print("Login failed!")

if __name__ == "__main__":
    main()
