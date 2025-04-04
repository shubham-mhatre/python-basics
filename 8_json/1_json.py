
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

import json

#dumps serializes a Python object into a JSON formatted string
s=json.dumps(book)
print(s)

#write to file
with open("D:\\projects\\poc\\github\\shubham-mhatre\\python\\python-demo\\8_json\\book.txt","w") as f:
    f.write(s)

#read from same file
r=open("D:\\projects\\poc\\github\\shubham-mhatre\\python\\python-demo\\8_json\\book.txt","r")
s=r.read()
print(s)

#used to deserialize data from a file or stream, converting it back into Python objects
j=json.loads(s)
print(j)