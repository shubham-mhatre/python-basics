def cal_square(num):
    print("inside cal_square function :  __name__ :: ", __name__)
    return num * num


if __name__ == "__main__":
    print("inside square file")
    a = cal_square(5)
    print("area : ", a)
