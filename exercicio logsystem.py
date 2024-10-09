#cadastre 10 usuarios com nome e senha
#mostrar o usuario, mostrar se a senha é compativel
#repetir o processo 3 vezes
#e colocar uma saida pro loguin
cadastro = [0]*10
senha = [0]*10
tamcadas=len(cadastro)
tentativa=0

operacao=0
while operacao !=4:
    print("escolha uma opção: \n"
          "1- Cadastro: \n"
          "2- mostrar: \n"
          "3- login: \n"
          "4- logout: \n")
    operacao = int(input("escolha uma opcao: "))
    if operacao == 1:
        for z in range (tamcadas):
            cadastro[z]=input("nome do login: ")
            senha[z]=input("senha de login: ")
            if z < tamcadas -1:
                continuar = input("cadastrar novo usuario? (sim/não): ")
                if continuar != 'sim':
                    break
                else:
                    print("lime de cadastro atingido.")
            if operacao == 2:
                for x in range (tamcadas):
                    print(f"usuario {x} - {cadastro[x]} \n"
                          f"senha: {senha[x]}")
            if operacao == 3:
                for y in range(tamcadas):
                    cadastro[y]=input("digite o login: ")
                    senha[y]=input("digite a senha: ")
                    if cadastro[y]==cadastro:
                        cadastro[y]==tentativa
            if operacao == 4:
                print("tchal, ate a proxima")
            else:
                print("não deu, tente novamente.")








