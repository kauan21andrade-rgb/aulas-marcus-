idade=int(input("qual sua idade ? "))
print("sua idade é " ,idade)
generof=input("filme de terror ou ação ? ")
print("você assitirá a " ,generof)
if idade<18 and generof=='terror':
    print(f"Este filme não é recomendado para sua idade devido ao gênero.")
elif idade<16 and generof=='ação':
    print(f"Este filme de ação não é adequado para sua faixa etária.")
elif idade>=18 or generof=='ação':
    print(f"Recomendado para você: assistir o filme.")
else:
    print(f"Não há recomendações para este filme ou idade.")