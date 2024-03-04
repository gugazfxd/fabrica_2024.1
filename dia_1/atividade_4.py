usuario=input("Digite sua idade : ").strip()
if usuario.isdigit():
    usuario=int(usuario)
else:
    print("O dado digitado não foi número por favor tente novamente ")
    quit()
if usuario>=18:
    print("Você e maior de idade!")
else:
    print("Você ainda não fez 18 anos por tanto ainda e de menor.")