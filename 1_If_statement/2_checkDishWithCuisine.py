dish=input("Enter Dish Name :")

indian=["samosa","daal rice","tandori chicken"]
italian=["pizza","pasta"]
chinese=["egg roll","fried rice"]

if dish in indian :
    print("dish is indian")
elif dish in italian:
    print("dish is italian")
elif dish in chinese:
    print("dish is chinese")
else:
    print("selected dish is not available in our cuisine")

