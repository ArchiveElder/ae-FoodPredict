import os

path=r'F:\건강관리를 위한 음식 이미지\Training\[원천]음식001_Tra'
f_list = os.listdir(path)

for f in f_list:
    print("%s" %(os.path.isdir(f)))
#list_of_files = []

#for root, dirs, files in os.walk(path):
#    for file in files:
#        list_of_files.append(os.path.join())