<<<<<<< HEAD
import sqlite3
from principal import pro_intro

def enter(): #Dá uma pausa e continua quando preciona enter
    r = input("Pressione ENTER para continuar")

def sist_pesquisa(dad): #Apresenta a definição do termo pesquisado se estiver presente no banco de dados(o parametro 'dad' é a lista com os dados do usuario: ID, nome e pontos)
    termo = input("\nInforme o termo desejado {}\nR: ".format(dad[1]))
    con = sqlite3.connect("pesquisa_db.db")
    cursor = con.cursor()
    cursor.execute("SELECT argumento FROM arquivo;")
    definicao = cursor.fetchall()
    cont = 0

    for linha in definicao:
        if termo.lower() in linha: #Vendo se o termo está presente no banco de dados
            cont += 1
    if cont == 1: 
        cursor.execute("SELECT * FROM arquivo WHERE argumento='"+termo.lower()+"';")
        conteudo = cursor.fetchall()
        con.close()

        for linha2 in conteudo:
            print("\n---------------------DEFINIÇÃO DE",termo.upper(),"---------------------\n")
            print("{}: {}".format(termo.title(),linha2[1])) #Apresentando a definição do termo
            print()
    else:
        con.close()
        print("---------------------\n| Termo Inexistente |\n---------------------")
        enter()
        pro_pesquisa(dad)

def pro_pesquisa(dad): #Se o usuario deseja pesquisar ou deseja voltar 
    print("\n---------------------PESQUISA---------------------\n")
    while True:
        r = int(input("'1' Pesquisar termo\n'9' Voltar\nR: "))
        if r == 1:
            sist_pesquisa(dad)
        elif r == 9:
            pro_intro(dad)


=======
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
>>>>>>> fe227c4 (versão 0.1)
