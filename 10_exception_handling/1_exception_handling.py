x = input("enter 1st number : ")
y = input("enter 2nd number : ")

try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("ZeroDivisionError : ", e)
    print("type of exception ", type(e))
except ValueError as e:
    print("ValueError : ", e)
    print("type of exception ", type(e))
    z = None


print("division is : ", z)
