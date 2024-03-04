usuario=input("Digite um número: ")
if usuario.isdigit():
    usuario=int(usuario)
else:
    print("O dado informando não e um número. Por favor Tente novamente!")
    quit()
if usuario%2==0:
    print("O número digitado não e primo")
elif usuario==2:
    print("O número digitado e primo")
else:
    print("O número digitado e primo")
