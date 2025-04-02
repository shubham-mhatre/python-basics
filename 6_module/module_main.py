
#to use custom module, add import statement and module name,
#check for package location, if file to be imported in

#import  custom_module

#if module is not in same directory and in some other directory.
#we can use sys module and use absolute path

import sys
sys.path.append("D:\\projects\\poc\\github\\shubham-mhatre\\python\\python-demo\\6_module")

import custom_module

print(custom_module.calculate_area_of_triangle(10,30))
