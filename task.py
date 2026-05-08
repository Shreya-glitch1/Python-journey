"""street_name = "Abbey Road"
print(street_name[4] + street_name[7])

print(type("Bayou"))
print(type(6))
print(type(3.14))
print(type(True))

#Type conversion 

print(int("666")+ int("123"))

print(3*3+3/3-3)

#F-string 

score = 0
height = 1.8
is_winning = True 

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}") 

print(6 + 4 / 2 - (1 * 2))

#if-else statement 

num = int(input("Enter a number:"))
if num%2 == 0:
    print("The number is even.")
else:
    print ("The number is odd.")"""
    
print("welcome to Python pizza delivery!")

size = input("What is the size of pizza you want? S,M,L:")
add_pepperoni = input("Do you want pepperoni? Y/N:")
add_cheese = input("Do you want extra cheese? Y/N:")
bill = 0
if size == "S":
    bill +=15
elif size == "M":
    bill +=20   
else:
    bill +=25
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
if add_cheese == "Y":
    bill +=1
print(f"Your final bill is: ${bill}.")


