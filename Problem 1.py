
a=list(map(int,input().split(",")))
arr=[]
for i in a:
    if i>=35:
        arr.append("Pass")
    else:
        arr.append("Fail")
print(arr)
print("finish")


mark=input("Enter the mark")
if(mark>35):
    print("pass")
else:
    print("fail")
