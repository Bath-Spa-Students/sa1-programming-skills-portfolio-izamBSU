# Basic implementation
user_info = {
     "name": "izam",
     "hometown": "dubai",
     "age": 19
 }
print(f"Name: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}")

# Advanced implementation
try:
    name = input("Enter your name: ")
    hometown = input("Enter your hometown: ")
    age = int(input("Enter your age: "))  # Convert age to an integer to prevent invalid input

    user_info = {
        "name": name,
        "hometown": hometown,
        "age": age
    }

    print(f"Name: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}")

except ValueError:
    print("Invalid input for age. Please enter a numeric value.")
