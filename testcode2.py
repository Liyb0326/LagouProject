import os
import selenium

file_path ='/test/testdata1.txt'
try:

    with open(file_path) as filetest:
        #print(filetest.read().rstrip())
        lines = filetest.readlines()

    with open(file_path,'a') as filetest1:
        filetest1.write("I love python3 \n")
        filetest1.write("I love python4 \n")
except FileNotFoundError:
    print("文件路径不存在")