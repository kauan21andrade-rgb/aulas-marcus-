numero=int(input("qual é o número ? "))
print("número é ") ,numero
conta=numero%2
if conta==0:
    print(f"valor é par, resto é {conta}")
else:
    print(f"valor é impar, resto é {conta}")
