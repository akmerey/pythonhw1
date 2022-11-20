a=int(input())
b=int(input())
c=int(input())
if( a==b and b==c and a==c):
    print(3)
elif((a==b and a==c) or (b==c and a==c)or(a==b and b==a)):
    print(2)
else:
    print(1)