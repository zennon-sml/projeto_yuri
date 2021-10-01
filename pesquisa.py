def pro_pesquisa():
    lista_termos = ['STRING','INTEIRO','FLOAT','BOOLEAN']
    while True:
        print("*****************************************\nVamos lá\n")
        v1 = input("'P' para prosseguir\n'V' para voltar\nR: ")
        if v1 == 'P' or v1 == 'p':
            print("*****************************************")
            print("Tem duvida com algum termo?\n")
            print("Termos mais comuns: ")
            for i in range(0,len(lista_termos)):
                print(lista_termos[i])
            termo = input("Pesquise aqui: ")
            termo = termo.upper() #transforma qualquer texto digitado em maiusculo
            elemento = lista_termos.index(termo) #vai indicar onde está localizado o termo na lista
            sist_pesquisa(elemento)
        elif v1 == 'V' or 'v':
            from principal import pro_intro
        else:
            print("*****************************************")
            print("Opção invalida")

def sist_pesquisa(element):
    arquivo = open('arquivo.txt', 'r') #abre o arquivo.txt para leitura
    texto = arquivo.readlines() #lê todas as linhas do arquivo.txt uma por uma
    cont = 0 #contador para auxiliar na apresentação da linha que tem a resposta

    for linha in texto:
        if cont == element: # o elemento é a posição que o termo pesquisado está presente na lista, vai ser printado a linha quando cont for igual a o elemento
            
            print(linha)
            v = input("tecle ENTER para continuar")
            pro_pesquisa()

        cont += 1
    arquivo.close()

pro_pesquisa()