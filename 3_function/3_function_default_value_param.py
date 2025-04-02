
#here b param default value set to 5, if we don't pass anything it will
#consider b's default value will function computation
def cal_sum(a,b=5):
    print("a : ",a)
    print("b : ", b)
    total=0
    total=a+b
    return total

# here we are only passing a param
total=cal_sum(10)
print("total : ",total)

#here passing both values
total=cal_sum(10,20)
print("total : ",total)