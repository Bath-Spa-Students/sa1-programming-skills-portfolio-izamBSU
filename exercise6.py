password=56789
while True:
    guess=int(input("Enter the password: "))
    if guess==password:
        print("Password is correct!")
        break
    else:
        print("Incorrect password, try again.")