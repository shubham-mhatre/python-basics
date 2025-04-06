
def process_file():
    try:
        f=open("D:\\projects\\poc\\github\\shubham-mhatre\\python\\python-demo\\7_file_read_write\\test.txt")
        x=1/0
    except Exception as e:
        print("exception : ",e,type(e))
    finally:
        print("cleaning file")
        f.close()

process_file()

