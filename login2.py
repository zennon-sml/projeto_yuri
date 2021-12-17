import sqlite3
from principal import pro_intro

def pro_login(): #Criar um novo login(entrada == 2) ou entrar com login existente (entrada == 1)
    print("\n---------------------INICIAR---------------------\n")
    entrada = int(input("'1' Entrar com login\n'2' Criar novo login\nR: "))
    if entrada == 2:
        pro_novo_usuario()
    elif entrada == 1:
        usuario()

def pro_novo_usuario(): #Adciona um novo usuario ao banco de dados
    print("\n-------------------NOVO USUÁRIO---------------------\n")
    id = input("Digite um login com 4 dígitos: ")
    con = sqlite3.connect("Usuarios.db")
    cursor = con.cursor()
    cursor.execute("SELECT id FROM novo;")
    ids = cursor.fetchall()
    con.close()
    cont = 0
    dados = []

    for linha in ids:
        if id in linha:
            cont += 1
        elif len(id) > 4 or len(id) < 4:
            print("\n--------------------\n| APENAS 4 DÍGITOS! |\n--------------------")
            pro_novo_usuario()
   
    if cont == 1:
        print("\n---------------------\n| Usuário Existente! |\n---------------------")
        pro_novo_usuario()
    else:
        nome = input("Digite seu nome: ")
        pontos = '0'
        con = sqlite3.connect("Usuarios.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO novo(id, nome, pontos) VALUES ('"+id+"','"+nome+"','"+pontos+"');")
        con.commit()
        con.close()
        dados.append(id)    
        dados.append(nome)   #Os dados do novo usuario vão ser adcionados a uma lista que posteriormente vão ser passados para outras partes
        dados.append(pontos)
        pro_intro(dados)
        
def usuario(): #Recupera os dados do usuario se ele estiver no banco de dados
    id = input("Seu login: ")
    con = sqlite3.connect("Usuarios.db")
    cursor = con.cursor()
    cursor.execute("SELECT id FROM novo;")
    ids = cursor.fetchall()
    con.close()

    cont = 0
    for linha in ids:
        if id in linha:
            cont += 1
        elif len(id) > 4 or len(id) < 4:
            print("APENAS 4 DIGITOS!")
            usuario()

    if cont == 1:
        con = sqlite3.connect("Usuarios.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM novo WHERE id='"+id+"';")
        nome = cursor.fetchall()
        con.close()
        dados =[]

        for linha in nome:
            dados.append(linha[0])
            dados.append(linha[1]) #Adciona os dados do usuario a uma lista
            dados.append(linha[2])
            print("\n----------------------------------\nSeja bem-vindo novamente",linha[1])
                     
        pro_intro(dados) #Passa lista com os dados do usuario para o pro_intro
   
    else:
        print("Usuário Inexistente!")
        usuario()

