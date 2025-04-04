
book={}
book["tom"]={
    "name":"tom",
    "address":"mumbai india",
    "contact":726637490
}
book["bob"]={
    "name":"bob",
    "address":"goa india",
    "contact":988234678
}

print('type of object before using json  ',type(book))

import json

#dumps serializes a Python object into a JSON formatted string
s=json.dumps(book)
print('type of object after using json.dumps()  ',type(s))
print('printing output of json.dumps ', s)


#write to file
with open("D:\\projects\\poc\\github\\shubham-mhatre\\python\\python-demo\\8_json\\book.txt","w") as f:
    f.write(s)

#read from same file
r=open("D:\\projects\\poc\\github\\shubham-mhatre\\python\\python-demo\\8_json\\book.txt","r")
s=r.read()
print('type of object after reading file ',type(s))
print("printing output of r.read() ",s)

#used to deserialize data from a file or stream, converting it back into Python objects
j=json.loads(s)
print('type of object after json.loads() ',type(j))
print("printing output of json.loads() ", j)

#print specific value like phone number of bob
print("print specific value like phone number of bob")
print(book["bob"]["contact"])


#print all person : iterate over json array and print all json object
print("print all person : iterate over json array and print all json object")
for person in book:
    print(book[person])