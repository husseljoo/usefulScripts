import os
import sys


def lowerAll(path):
    for filename in os.listdir(path):
        a=customEdit(filename)
        src=path+'/'+filename
        dst=path+'/'+a
        print(dst) #optional to comment it out 
        os.rename(src,dst)  
        if os.path.isdir(src):
            lowerAll(src)
    
def customEdit(str):
    a=""
    for char in str:
        if char.isupper():
            a+=char.lower()
        elif char==' ':
            a+='_'
        else:
            a+=char
    return a
    

if __name__=='__main__':
    if len(sys.argv)!=2:
        print("Add only one file path to apply changes to!")
    else:
        lowerAll(sys.argv[1])
        print("Finished successfully!")
