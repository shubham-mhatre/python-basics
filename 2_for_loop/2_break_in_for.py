
key_location="chair"
location=["kitchen","living room","garage","chair","closet"]

for key in location:
    if key == key_location:
        print("key found in : ",key)
        break
    else:
        print("key not found in : ",key)