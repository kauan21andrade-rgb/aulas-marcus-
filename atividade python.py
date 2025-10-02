idade=int(input("sua idade : "))
nacionalidade=input("qual sua nacionalidade: ")

if idade>=60:
    if nacionalidade=='brasileiro':
        desconto=100
        print(f"você tem um desconto especial, equivalente a {desconto}")

    else:
        desconto2=20
        print(f"você tem um desconto padrão, no valor de {desconto2}") 

else:
    print(f"você não tem direito a desconto")