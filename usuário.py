usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
        print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
        print("Seja bem-vindo Nico")
else:
        print("Usuário não identificado!")

        


usuario = input("Informe o usuário do sistema!")

pessoa_1 = usuario == "maria"
pessoa_2 = usuario == "livia"

if(pessoa_1):
    print("seja bem vinda!")
else:
    if(pessoa_2):
        print("seja bem vinda livia!")
    else:
       print("usuário não identificado")