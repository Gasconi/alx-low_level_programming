#ask user to input their name
name = input("Please input your name: ")
print(f"\n{name.title()}, we are going to play a game")
print("\nEnter a number and I will tell you if it is a multiple of 10 or not")
#input number
number = input("Enter number: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of 10")
else:
    print(f"\n{number} is not a multiple of 10")

