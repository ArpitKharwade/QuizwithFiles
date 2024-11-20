import json
import random
import hashlib
import os

# File path for user data storage
USER_DB_FILE = 'user.json'

# Load user data from user.json file
def load_users():
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, 'r') as f:
        return json.load(f)

# Save user data to user.json file
def save_users(users):
    with open(USER_DB_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Load quiz questions from questions.json file
def load_questions():
    with open('questions.json') as f:
        data = json.load(f)
        return data['questions']

# Register a new user
def register_user(users):
    username = input("Enter username: ")
    if username in users:
        print("Username already exists!")
        return users
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
    users[username] = hashed_password
    save_users(users)
    print("User registered successfully!")
    return users

# Login an existing user
def login_user(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the entered password
    if username in users and users[username] == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

# Start the quiz and calculate the score
def start_quiz():
    questions = load_questions()
    random_questions = random.sample(questions, 5) 
    
    score = 0
    for question in random_questions:
        print(f"\nQuestion: {question['question']}")
        for idx, option in enumerate(question['options']):
            print(f"{idx + 1}. {option}")
        
        answer = input("Your answer: ")
        if answer.strip().lower() == question['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {question['answer']}")
    
    print(f"\nYour final score: {score}/5")

# Main Application Logic
def main():
    users = load_users()  # Load users from user.json

    while True:
        print("\nWelcome to the Python Quiz App!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            users = register_user(users)
        elif choice == "2":
            if login_user(users):
                start_quiz()
                break
        elif choice == "3":
            print("Exiting the app...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
