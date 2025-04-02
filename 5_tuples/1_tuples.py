
#tuple is similar to list with following difference
#tuple can have heterogenous values/mixed values
#tuple are immutable, once created cannot modify it's value

#here tuple with mixed values,
#street, city, pincode, statecode, state name
address_tuple_1=("1st floar sky city ","thane",400012,27,"maharashtra")

print("tuple : ",address_tuple_1)

#get value from tuple using index address_tuple_1[0]
print("get value from tuple using index address_tuple_1[0] : ")
print(address_tuple_1[0])

#try to modify value, it will give error : address_tuple_1[1]="mumbai"
print("try to modify value, it will give error : address_tuple_1[1]='mumbai' ")
address_tuple_1[1]="mumbai"