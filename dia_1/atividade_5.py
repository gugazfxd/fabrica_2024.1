usuario=input("Digite um número: ")
if usuario.isdigit():
    usuario=int(usuario)
else:
    print("O dado informando não e um número. Por favor Tente novamente!")
    quit()
if usuario%2==0:
    print("O número digitado e par")
else:
    print("O número digitado e Impar")
