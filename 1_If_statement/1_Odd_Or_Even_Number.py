# Check Number is Odd or Even
# accept input from user

num = input("Enter a number :")

# convert string input to integer
num = int(num)

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
