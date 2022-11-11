import os
import shutil

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Downloads/document"

list_of_files = os.listdir(from_dir)
#print(list_of_files)


for file_name in list_of_files: 
    name, ext = os.path.splitext(file_name)
    print(name,ext)

    if ext == '':
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "document_files"
        path3 = to_dir + "/" + "document_files" + "/" + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)
        else :
            os.mkdir(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)