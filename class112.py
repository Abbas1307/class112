import os
import shutil

source= "C:/Users/ME/Downloads/mydownloads"
dist="C:/Users/ME/Downloads/moveingfolder"

list_of_files = os.listdir(source)
print(list_of_files)

for i in list_of_files:
    name,extention=os.path.splitext(i)
   # print(name)
    #print(extention)

    if extention=="":
        continue
    if extention in [ '.txt', '.doc', '.docx', '.pdf',".jpg",".gif","png"]:
        path1=source+"/"+i
        path2=dist+"/"+"images_files"
        path3= dist+"/"+"images_files"+"/"+i

        if os.path.exists(path2):
            print("Moving "+i+".......")

            shutil.move(path1,path2)
        else:
            os.makedirs(path2)
            print("Moving "+i+".......")

            shutil.move(path1,path2)
