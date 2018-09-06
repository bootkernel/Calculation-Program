#Asking the user to input the required information in the main function
def main():
    global wall_space_sq_feet
    wall_space_sq_feet = float(input("Please enter Wall space in square feet: "))
    global price_per_gallon
    price_per_gallon = float(input("Enter the price per gallon: "))
main()

#Calculate How many gallons are there
def gallon_func():
    global result
    result = wall_space_sq_feet/112
gallon_func()

#Multiply Cost per gallon with number of gallon
def multiply():
    global result1
    result1 = price_per_gallon * result
multiply()

#Get the total price
def total_cost():
    global total_cost
    total_cost = (result1 * result) + 280 #280 is a constant value as it's a predefined value given by the company
total_cost()

#the round function converts the float value to integer value, it's useful when you have a situation like this (2.965433 and you want to round up the value to 3)
print ("Gallons of Paint:", round(result))
print ("Hours of Labor: 8 hours (required)") #Hours are already given by the company
print ("Paint charges: $", round(result1))
print ("Labor Charges (Our Company Charges $35.00 per hour for labor): $280")
print ("Total Cost: $", round(total_cost))
