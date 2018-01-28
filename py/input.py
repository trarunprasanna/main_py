

#input from user
name = input("enter your name: ")


age = int(input("enter your age :"))

loc = input("enter your location :")

pin = input("enter your pin code :")

data ="your name is {} , your age is {} , your location is {} , your pincode is {}"
output=data.format(name,age,loc,pin)
print (output)

# below example firm udemy

# First, create a variable called start, and set it equal to "I am ".
# Remember the space after the word "am" !
start ="I am "

# Next, create a variable called age and set it equal to your age in years.
# This must be a number
age = 32

# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"
end =" years old"

# Next, create a variable called output, and use the format() function to add
# together the start, age and end variables.
output=start+str(age)+end
# An example output string would be "I am 15 years old"
print(output)

# Finally, print the output to the screen using the print() function.

