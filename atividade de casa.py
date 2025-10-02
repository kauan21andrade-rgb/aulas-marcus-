import math
a=int(input("qual o valor de a ? "))
print("a é " ,a)
b=int(input("qual o valor de b ? "))
print("b é " ,b)
c=int(input("qual o valor de c ? "))
print("c é " ,c)
d=int(input("qual o valor de d? "))
print("d é " ,d)
if a>b and b>c  and c>d:
    print(f"ordem correta")
else:
    print(f"ordem incorreta")