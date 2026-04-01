list = []
n=int(input("enter number of elements="))
for i in range(n):
    x=int (input("enter  element:"))
    list.append (x)
result=[]
for i in list :
    if i not in result:
        result.append (i)
print("list after removing=",result)          
