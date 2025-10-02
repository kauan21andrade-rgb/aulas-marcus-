totaldacompra=float(input("qual o valor total da compra: "))

if totaldacompra>100:
        desconto5=(totaldacompra/100)*5
        valoratualizado=totaldacompra-desconto5
        print(f" valor com desconto é {valoratualizado}")
        if valoratualizado>150:
            descontoad2=(valoratualizado/100)*2
            valorfinal=valoratualizado-descontoad2
            print(f"valor com desconto adicional é {valorfinal}")

else:
    print(f"nenhum desconto aplicado, valor total {totaldacompra} ")