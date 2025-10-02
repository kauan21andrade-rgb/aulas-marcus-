numero1=int(input("qual é o número ? "))
print("número é " ,numero1)
numero2=int(input("qual é o número ? "))
print("número é " ,numero2)
if numero1 % numero2 == 0 and numero2 % numero1 == 0:
    print(f"Os números são divisíveis entre si")
else:
    print(f"Os números não são divisíveis entre si")