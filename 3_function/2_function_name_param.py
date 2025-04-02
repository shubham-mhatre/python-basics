
def cal_sum(a,b):
    print("a : ",a)
    print("b : ", b)
    total=0
    total=a+b
    return total

#when we pass like this, param sequence not required
total=cal_sum(b=5,a=3)
print("total : ",total)
