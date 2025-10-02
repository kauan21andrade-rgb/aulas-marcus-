print("Nome:Kauan Henry de Andrade")
print("RA 0220482523036")
glicose=float(input("qual o seu nível de glicose mg/dL em jejum ? "))
print("seu nível de glicose em jejum é " ,glicose)
if glicose<100:
    print("Glicemia Normal.")
elif glicose>=100 and glicose<=125:
    print("Pré-diabetes: Risco Moderado.")
elif glicose>125:
    print("Diabetes: Nível Alto.")
else:
    print("Não é aceito número negativo!")