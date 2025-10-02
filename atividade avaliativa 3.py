print("Nome:Kauan Henry de Andrade")
print("RA 0220482523036")
pesoe=int(input("qual quilos tem a encomenda ? "))
print(" o peso da encomenda em quilos é " ,pesoe)
distanciae=int(input("qual a distância da entrega em quilômetros ? "))
print(" a distância de entrega em quilômetros é " ,distanciae)
custob=(pesoe*1.5)+(distanciae*0.25)
if custob>200:
    desconto=(custob/100)*10
    custof=custob-desconto
    print(f"o valor era de {custob} reais,já com desconto de 10%, o preço foi para {custof} reais")
elif custob>=50 and custob<=200:
    print(f"não há desconto nem taxa!, preço é equivalente a {custob} reais")
elif custob<50:
    taxa=5
    custov=custob+5
    print(f"preço era de {custob} reais,mas com o acréscimo da taxa de manuseio o preço foi para {custov} reais")
else:
    print("não é aceito número negativo de preço base!")
