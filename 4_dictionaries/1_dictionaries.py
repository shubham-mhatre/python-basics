
#dictionary is map, it store data in key value format

# intialize dictionary
print("intialize dictionary")
d={"shubham":9886364728,"shubhangi":9735468232}
print(d)

#get value from dictionary: get using key
print("get value from dictionary: get using key :  d['shubham']")
print("result", d["shubham"])

#add entry to dictionary
print("add entry to dictionary :  d['manju']=9852637238 ")
d['manju']=9852637238
print("result after adding value ",d)

#iterate over all entries in dictionary
print("iterate over all entries in dictionary : for key in d")
for key in d:
    print("key : ",key)
    print("value : ", d[key])

#another way to iterate over all entries in dictionary
print("another way to iterate over all entries in dictionary : for key,value in d.items() ")
for key,value in d.items():
    print("key : ",key)
    print("value : ", value)

#check if specific key is present in dictionary using in operator : "shubham" in d
print("check for shubham if present in dictionary : ", "shubham" in d)

#delete entry to dictionary : use key to delete specific entry
print("delete entry to dictionary : use key to delete specific entry : del d['shubham']")
del d['shubham']
print("result after deleting entry ",d)

#clear all entries from dictionary
print("clear all entries from dictionary : d.clear()")
d.clear()
print("result after clearing all entries : d.clear() : ",d)


