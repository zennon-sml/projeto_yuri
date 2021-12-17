import sqlite3
from adm import pro_admin

def enter(): #Dá uma pausa e continua quando preciona enter
    e = input("Pressione ENTER para continuar")

def novo_p(): #Adciona um novo termo ao banco de dados 
    print("\n-------------------NOVO OBJETO---------------------\n")
    argumento = input("Informe a palavra chave: ")
    definicao = input("Informe a definição: ")
    
    con = sqlite3.connect("pesquisa_db.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO arquivo (argumento, definicao) VALUES (?,?)",[argumento.lower(),definicao])
    print("\n---------------------------------\n| Objeto Adicionado Com Sucesso |\n---------------------------------")               
    con.commit()
    con.close()
   
    while True:
        e = int(input("'1' Novo Objeto\n'2' Continuar\nR: "))
        if e == 1:
            novo_p()
        elif e == 2:
            conf_pesq()
        else:
            print("\nInválido!\n")
            continue

def exibir_p(a): #Exibe os termos presentes no banco de dados e apresenta a definição se assim o administrador desejar (o parametro 'a' serve para definir se o exibir_p foi chamado do conf_pesq ou não)
    print("\n---------------------EXIBINDO OBJETOS---------------------\n")
    con = sqlite3.connect("pesquisa_db.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM arquivo")
    objetos = cursor.fetchall()
    con.commit()
   
    for n, linha in enumerate(objetos,1):
        print(n,"-",linha[0])
        print("-------------#|")
    defn = int(input("\n'1' Ver a definição de um objeto\n'2' Continuar\nR:"))

    if defn == 1:
        qual = input("\nEscolha o objeto desejado para ver a definição: ")
        cursor.execute("SELECT argumento FROM arquivo;")
        definicao = cursor.fetchall()
        cont = 0

        for linha in definicao:
            if qual in linha:
                cont += 1
        
        if cont == 1: #Se o termo estiver no banco de dados a definição dele será apresentanda 
            cursor.execute("SELECT * FROM arquivo WHERE argumento='"+qual+"';")
            conteudo = cursor.fetchall()
            con.close()
            for linha2 in conteudo:
                print("\nDefinição de",qual)
                print("\n",qual,":",linha2[1],"\n") 

                enter()
                if a == "voltar":
                    conf_pesq()    
                elif a == "atua":
                    pass
            
        else:
            con.close()
            print("---------------------\n| Objeto Inexistente |\n---------------------")
            enter()
            exibir_p()

    elif defn == 2:
        if a == "voltar":
            conf_pesq()    
        elif a == "atua":
            pass

def atualizar_p(): #Modifica os dados do termo escolhido
    print("\n-------------------MODIFICANDO OBJETO---------------------")
    chave = input("\nInforme a palavra-passe para alteração: ")
    argumento = input("Informe a nova palavra chave: ")
    definicao = input("Informe a nova definição: ")
    con = sqlite3.connect("pesquisa_db.db")
    cursor = con.cursor()
    cursor.execute("UPDATE arquivo SET argumento=?, definicao=? WHERE argumento=?",[argumento,definicao,chave])
    print("\n----------------------------------\n| Questão Atualizada Com Sucesso |\n----------------------------------")
    con.commit()
    con.close()
    enter()
    conf_pesq()

def menu_atualizar_p(): #Antes de modificar os dados dos termos o adiministrador vai escolher se deseja ver a lista com os termos ou não
    print("\n-------------------MODIFICAR OBJETO---------------------\n")
    ver = int(input("'1' Não Exibir Lista\n'2' Exibir Lista\nR: "))
    if ver == 1:
        atualizar_p()
    elif ver == 2:
        exibir_p("atua")
        atualizar_p()
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        menu_atualizar_p()

def remover_p(): #Remove um termo
    print("\n-------------------REMOVENDO OBJETO---------------------")
    chave = input("\nInforme a palavra-passe desejada para remoção: ")
    con = sqlite3.connect("pesquisa_db.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM arquivo WHERE argumento=?", [chave])
    print("\n-------------------------------\n| Objeto Removido Com Sucesso |\n-------------------------------")
    con.commit()
    con.close()
    enter()
    conf_pesq()

def menu_remover_p(): #Antes de remover um termo o adiministrador vai escolher se deseja ver a lista com os termos ou não
    print("\n-------------------REMOVER OBJETO---------------------\n")
    ver = int(input("'1' Não Exibir Lista\n'2' Exibir Lista\nR: "))
    if ver == 1:
        remover_p()
    elif ver == 2:
        exibir_p("atua")
        remover_p()
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        menu_remover_p()

def conf_pesq(): #Apresenta as opções que o administrador pode utilizar na administração da pesquisa
    print("\n-------------------CONFIGURAÇÕES DE PESQUISA---------------------\n")
    
    print("'1' Adicionar Objeto")
    print("'2' Exibir Objetos")
    print("'3' Modificar Objeto")
    print("'4' Remover Objeto")
    print("'9' Voltar")
    
    escolha = int(input("R: "))

    if escolha == 1:
        novo_p()
    elif escolha == 2:
        exibir_p("voltar")
    elif escolha == 3:
        menu_atualizar_p()
    elif escolha == 4:
        menu_remover_p()
    elif escolha == 9:
        print("------------\n| Voltando |\n------------")
        pro_admin()
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        conf_pesq()

#pesquisa_db.db
#
#TABLE arquivo(
#argumento VARCHAR(20) PRIMARY KEY,
#definição VARCHAR(300));