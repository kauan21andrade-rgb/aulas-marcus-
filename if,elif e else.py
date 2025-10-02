s=float(input("informe o salário: "))
if s<5000:
    imposto=0.12*s
    print(f"valor do imposto é {imposto}")
elif s>=5000 and s<7500:
    imposto=0.17*s
    print(f"valor do imposto é {imposto}")
elif s>=7500 and s<8900:
    imposto=0.22*s
    print(f"valor do imposto é {imposto}")
else:
    imposto=0.27*s
    print(f"valor do imposto é {imposto}")