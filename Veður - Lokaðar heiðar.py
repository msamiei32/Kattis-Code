x = int(input())
y = int(input())
b = {}
for i in range(y):
    s,n = map(str,input().split())
    b[s] = int(n)
for key,value in b.items():
    if value < x:
        print(key,'','lokud')
    else:
        print(key,'','opin')