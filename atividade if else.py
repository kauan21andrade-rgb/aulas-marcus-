senhacerta="marcus"
usuariocerto="kauan@gmail"
u=input("informe usuário: ")
if u==usuariocerto:
    p=input("informe sua senha: ")
    if p==senhacerta:
        print("credenciais válidos")
    else:
        print("senha inválida")
else:
    print("usuário inválido")    