world=input("Please enter the world you dont wnt to be removed by profanity extension")
file=open("D:\pythonproject\\allowed.txt",'w+')
data=file.read()
data=data.split('|')
c=0
for i in data():
    if(world==data):
        c=1
if(c!=0):
    file.write(world+"|")
else:
    print("The word already exsist in the library")
