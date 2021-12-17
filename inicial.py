<<<<<<< HEAD
import sqlite3
from login2 import pro_login    ###!!!O PROGRAMA DEVE SER INICIADO AQUI!!!###
from adm import pro_admin
from operator import itemgetter

def inicio(): #Define se o usuario vai entrar como administrador(entrada == 2) ou como usuario normal(entrada == 1)
    entrada = int(input("'1' Iniciar\n'2' Entrar como administrador\nR: "))
    n_eh_a_senha = ('4321')

    if entrada == 1:
        pro_login() #Encaminha para a area de login
    elif entrada == 2:
        while True:
            print("\n-------------------ENTRAR COMO ADMINISTRADOR---------------------\n")
            print("'9' Voltar")
            senha = input("Digite a senha: ")
            if senha == n_eh_a_senha:
                pro_admin() #Configurações do Administrador
            elif senha == '9':
                print("\n-----------------------------------")
                inicio()
            else:
                print("\nSenha invalida")
    else:
        print("INVÁLIDO")
        inicio()

def ranking(): #Apresenta um ranking com todos os usuarios ordenados pela pontuação
    print("\n---------RANKING---------\n")
    
    lista = []
    con = sqlite3.connect("Usuarios.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM novo;")
    colocados = cursor.fetchall()
    con.close()

    for linha in colocados:
        lista.append(linha)
    print("Posição | Pontos | Usuário\n---------------------------")
    for n, i in enumerate(sorted(lista, key=itemgetter(2), reverse=True), 1):
        print("   {}º   |   {}   -  {}\n---------------------------".format(n,i[2],i[1]))
    print()
    inicio()
ranking()
=======
from principal import pro_intro
>>>>>>> fe227c4 (versão 0.1)
