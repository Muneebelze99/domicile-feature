students=["muneeb","Doe","Jane","Smith"]
employees=["Alice","ali","Charlie","David"]
user_name=input("Enter your name: ")
if user_name in students:
    print("You are a student.")
elif user_name in employees:
    print("You are an employee.")
else:
    print("user is not found in list")