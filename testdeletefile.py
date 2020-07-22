import os

def find_file(path):
    _filename = []
    filelist = os.listdir(path)
    if len(filelist) > 0:
        for i in range(0, len(filelist)):
             _path1 = os.path.join(path, filelist[i])
             if os.path.isdir(_path1):
                 find_file(_path1)
             elif os.path.isfile(_path1):
                 _filename.append(filelist[i])


f = find_file(r"C:\Users\liyb16997\Desktop\Test")

