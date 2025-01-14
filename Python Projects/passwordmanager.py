from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Uncomment the following line to generate a new key
# write_key()

master_password = "passwordmanager"
key = load_key()
fer = Fernet(key)

def menu():
    while True:
        mode = input("Would you like to add a new password or view existing ones? (view, add, edit, quit) ").lower()
        if mode == "quit":
            break
        
        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "edit":
            edit()
        else:
            print("Invalid mode. Please try again.")

def edit():
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
    found = False
    for i, line in enumerate(lines):
        parts = line.strip().split(" | ")
        if len(parts) == 3:
            user, encrypted_passw, socialmedia = parts
            try:
                decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                if decrypted_passw == pwd:
                    found = True
                    print("What would you like to change? (user, pass, socialmedia)")
                    change = input().lower()
                    if change == "user":
                        user = input("New username: ")
                    elif change == "pass":
                        new_passw = input("New password: ")
                        encrypted_passw = fer.encrypt(new_passw.encode()).decode()
                    elif change == "socialmedia":
                        socialmedia = input("New social media: ")
                    else:
                        print("Invalid input. Please try again.")
                        continue
                    lines[i] = f"{user} | {encrypted_passw} | {socialmedia}\n"
                    with open("passwords.txt", "w") as f:
                        f.writelines(lines)
                    print("Password updated successfully.")
                    break
            except Exception as e:
                print(f"Error decrypting password for {user}: {e}")
    if not found:
        print("Password not found.")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                user, encrypted_passw, socialmedia = parts
                try:
                    decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                    print(f"User: {user}, Password: {decrypted_passw}, Social Media: {socialmedia}")
                except Exception as e:
                    print(f"Error decrypting password for {user}: {e}")
            else:
                print("Error: Line does not contain exactly 3 values.")

def add():
    socialmedia = input("Social Media Platform: ")
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    
    with open("passwords.txt", "a") as f:
        f.write(name + " | " + encrypted_pwd + " | " + socialmedia + "\n")

while True:
    pwd = input("Enter password: ")
    if pwd == master_password:
        print("Password accepted.")
        menu()
        break
    else:
        print("Incorrect password. Please try again.")