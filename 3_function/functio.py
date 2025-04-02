
shubham_expense=[2940,3841,4352,2345,2187]
shubhangi_expense=[2301,2204,2712,2811,2488]


def calculateTotalExpense(expense):
    total = 0
    for item in expense:
        total = total + item

    return total

total_shubham_expense=calculateTotalExpense(shubham_expense)
print("shubham's total expense : ",total_shubham_expense)

total_shubhangi_expense=calculateTotalExpense(shubhangi_expense)
print("shubhangi's total expense : ",total_shubhangi_expense)


