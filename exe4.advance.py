# Dictionary of 10 European countries and their capitals

european_countries = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Switzerland": "Bern"
}

# Example usage
for country, capital in european_countries.items(): 
    answer = input(f"What is the capital of {country}? ")
    if answer.lower() == capital.lower():
        print(f"Correct! The capital of {country} is {capital}.")
    else:
        print(f"Incorrect! The capital of {country} is {capital}.")
