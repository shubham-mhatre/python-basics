
f=open("D:\\projects\\poc\\github\\shubham-mhatre\\python\\"
       "python-demo\\7_file_read_write\\test.txt","w")

#2nd param "w" here is to pass mode, so passing w for write
#write mode will override old content of file as well

f.write("leo messi is greatest of all time")
f.close()

#mode : append will make sure, previous content will be there as well as new one will
#get append

a=open("D:\\projects\\poc\\github\\shubham-mhatre\\python\\"
       "python-demo\\7_file_read_write\\append.txt","a")
a.write("ronaldo is greatest of all time")
a.close()
