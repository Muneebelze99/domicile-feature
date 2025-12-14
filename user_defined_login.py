def user_defined_login():
    print("===Registration===")
    saved_username = input("Create a username: ")
    saved_password = input("Create a password: ")
    print("\n===Login===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == saved_username and password == saved_password:
        print("Login successful!")
    else:
        print("Login failed. Incorrect username or password.")
user_defined_login()