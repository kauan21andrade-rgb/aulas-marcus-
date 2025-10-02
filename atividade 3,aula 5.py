import math
nome=input("qual seu nome ?")
print("seu nome é" ,nome)
a=float(input("qual valor do a ?"))
print("valor de a é", a)
b=float(input("qual valor de b ?"))
print("valor de b é" ,b)
c=float(input("qual valor de c ?"))
print("valor de c é" ,c)
delta=b**2-4*a*c
x1=-b-math.sqrt(delta)/2*a
x2=-b+math.sqrt(delta)/2*a
print(f"ola,{nome}, valor de a é {a}, valor de b é {b} e valor de c é {c}, portanto x1 é {x1} e x2 é {x2}")