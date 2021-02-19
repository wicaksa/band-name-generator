# This program asks user for city name and pet name and generates a random band name from the two inputs.
# Ths is day 1 of 100 days of coding from Udemy Dr. Angela Yu.

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")

#2. Ask the user for the city that they grew up in.
user_city = input("What city did you grow up in?\n")

#3. Ask the user for the name of a pet.
user_pet = input("What is the name of your first pet?\n")

#4. Combine the name of their city and pet and show them their band name.
user_band_name = user_city + " " + user_pet
print("Your band name is " + user_band_name + "!")

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/


#def generate_band_name () :
    #user_city = input("What city did you grow up in?\n")
    #user_pet = input("What is the name of your first pet?\n")
    #print("Your band name is " + user_band_name + "!")
