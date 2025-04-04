#function to determine if a number is prime
def check_even_or_odd(number):
    if number % 2 == 0:
        return "the number is even"
    else:
        return "the number is odd"
    
    #main function
def main():
    #asking the user for a number
    user_input = int(input("Enter a number: "))

    #passing the number to the function and  getting the result
    result = check_even_or_odd(user_input)

    #printing the result
    print(result)

    #calling the main function to run the program
if __name__ == "__main__":
    main()