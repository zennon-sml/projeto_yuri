import sqlite3
from adm import pro_admin

def exibir_u(u): #Exibe uma lista com todos os usuarios cadastrados: Id, Nome e Pontuação (o parametro 'u' serve para definir se o exibir_u foi chamado do conf_usu ou não) 
    print("\n---------------------EXIBINDO USUÁRIOS---------------------\n")
    con = sqlite3.connect("Usuarios.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM novo")
    pessoas = cursor.fetchall()
    con.commit()
    con.close()

    for linha in pessoas:
        print("\n#-------------#-------------#-------------#-------------|\n")
        print("Id: {} // Usuário: {} // Pontuação: {}".format(linha[0],linha[1],linha[2]))
    print("\n^-------------^-------------^-------------^-------------|")
    if u == "s":
        return
    else:
        conf_usu()

def editar_u(): #Modifica os dados de algum usuario pelo ID
    id = input("\nInforme o Id do usuário a ser modificado: ")
    q = int(input("\nO que você deseja modificar?\n'1'Nome\n'2'Pontuação\nR: "))
    con = sqlite3.connect("Usuarios.db")
    cursor = con.cursor()

    if q == 1:
        nome = input("Informe um nome: ")
        cursor.execute("UPDATE novo SET nome=? WHERE id=?",[nome,id])
    elif q == 2:
        pontos = input("Informe a pontuação: ")
        cursor.execute("UPDATE novo SET pontos=? WHERE id=?",[pontos,id])
        
    print("\n----------------------------------\n| Usuário Atualizado Com Sucesso |\n----------------------------------")
    con.commit()
    con.close()
    conf_usu()

def menu_editar_u(): #Antes de modificar os dados do usuario o adiministrador vai escolher se deseja ver a lista com os usuarios ou não
    print("\n-------------------EDITAR USUÁRIO---------------------\n")
    ver = int(input("'1' Não Exibir Lista De Usuários\n'2' Exibir Lista De Usuários\nR: "))

    if ver == 1:
        editar_u()
    elif ver == 2:
        exibir_u("s")
        editar_u()
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        menu_editar_u()

def remove_u(): #Remove algum usuario pelo ID
    id = input("\nInforme o Id do usuário para remoção: ")
    con = sqlite3.connect("Usuarios.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM novo WHERE id='"+id+"'")
    print("\n--------------------------------\n| Usuário Removido Com Sucesso |\n--------------------------------")
    con.commit()
    con.close()
    conf_usu()

def menu_remove_u(): #Antes de remover o usuario o adiministrador vai escolher se deseja ver a lista com os usuarios ou não
    print("\n-------------------REMOVER USUÁRIO---------------------\n")
    ver = int(input("'1' Não Exibir Lista De Usuários\n'2' Exibir Lista De Usuários\nR: "))

    if ver == 1:
        remove_u()
    elif ver == 2:
        exibir_u("s")
        remove_u()
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        menu_remove_u()

def conf_usu(): #Apresenta as opções que o administrador pode utilizar na administração de usuarios
    print("\n-------------------CONFIGURAÇÕES DE USUÁRIOS---------------------\n")
    print("'1' Exibir Usuários")
    print("'2' Modificar Usuário")
    print("'3' Remover Usuário")
    print("'9' Voltar")
    escolha = int(input("R: "))
    if escolha == 1:
        exibir_u("n")
    elif escolha == 2:
        menu_editar_u()
    elif escolha == 3:
        menu_remove_u()
    elif escolha == 9:
        print("------------\n| Voltando |\n------------")
        pro_admin()
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        conf_usu()

#Usuarios.db  
#  
#TABLE novo(
#id VARCHAR(4) PRIMARY KEY,
#nome VARCHAR(100),
#pontos INTEGER);

