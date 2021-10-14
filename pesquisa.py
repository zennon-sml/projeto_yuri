def pro_pesquisa():
    lista_termos = ['STRING','INTEIRO','FLOAT','BOOLEAN'] #Lembrar de por os termos aqui em maiusculo

    while True:
        print("*****************************************\nVamos lá\n")
        v1 = input("'P' para prosseguir\n'V' para voltar\nR: ")

        if v1 == 'P' or v1 == 'p':
            while True:
                print("\n*****************************************")
                print("Qual termo você tem duvida?\n    ('V'para voltar)\n")
                termo = input("Digite aqui: ")
                termo = termo.upper() #transforma qualquer texto digitado em maiusculo

                if lista_termos.count(termo) >= 1:
                    elemento = lista_termos.index(termo) #vai indicar onde está localizado o termo na lista
                    sist_pesquisa(elemento)

                elif termo == 'V' or termo == 'v':
                    from principal import pro_intro
                    pro_intro()

                else:
                    print("\n*****************************************\nO termo ainda não foi adicionado ao sistema, tente outro termo, por favor!")
                    v = input("tecle ENTER para continuar")

        elif v1 == 'V' or 'v':
            from principal import pro_intro
            pro_intro()

        else:
            print("\n*****************************************")
            print("Opção invalida")

def sist_pesquisa(element):
    arquivo = open('arquivo.txt', 'r', encoding='utf-8') #abre o arquivo.txt para leitura
    texto = arquivo.readlines() #lê todas as linhas do arquivo.txt uma por uma
    cont = 0 #contador para auxiliar na apresentação da linha que tem a resposta

    for linha in texto:
        if cont == element: # o elemento é a posição que o termo pesquisado está presente na lista, vai ser printado a linha quando cont for igual a o elemento         
            print("\n*****************************************")
            print(linha)
            v = input("tecle ENTER para continuar")
            pro_pesquisa()

        cont += 1
    arquivo.close()

pro_pesquisa()