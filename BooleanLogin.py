is_logged_in = False
password = input("Enter a password: ")

if password == "admin123":
    is_logged_in = True
    print("Access granted!")
else:
    print("Access denied!")