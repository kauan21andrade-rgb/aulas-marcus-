compra=float(input("qual o valor total da compra ? "))
print(" valor total da compra é ") ,compra 
status=input("você é um cliente novo ou fiel ? ")
print("você é um cliente" ,status)
produto=input("produto eletrônico ou livro ? ")
print("produto é " , produto)
if compra>=200 and status=='fiel':
    print(f"Parabéns! Você tem direito a frete grátis e um brinde especial.")
elif compra>=200 or produto=='livro':
    print(f"Você tem direito a frete grátis. Aproveite!")
elif status=='fiel' and produto=='eletrônico':
    print(f"Você tem direito a um desconto de 5% no frete.")
else:
    print(f"Não há promoções aplicáveis a este pedido.")
