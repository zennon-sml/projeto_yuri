import sqlite3
from adm import pro_admin
       
def exibir_q(tip): #Exibe uma lista com as questões do quiz dependendo do nivel que o administrador deseja: id, enunciado, a, b, c, d e resposta correta (o parametro 'tip' serve para definir se o exibir_q foi chamado do conf_quiz ou não, se não retorna o nivel) 
    print("\n---------------------EXIBINDO QUESTÕES---------------------\n")
    nivel = int(input("Escolha a dificuldade desejada:\n'1' Fácil\n'2' Médio\n'3' Difícil\nR: "))
    
    if nivel < 1 or nivel > 3:
        print("\n------------------\n| Opção Inválida |\n------------------")
        exibir_q(tip)
    else: 
        con = sqlite3.connect("quiz_db.db")
        cursor = con.cursor()
        
        if nivel == 1:
            cursor.execute("SELECT * FROM facil")
        elif nivel == 2:
            cursor.execute("SELECT * FROM medio")
        elif nivel == 3:
            cursor.execute("SELECT * FROM dificil")

        questoes = cursor.fetchall()
        con.commit()
        con.close() 
        print("\nV-------------V-------------V-------------V-------------|")

        for linha in questoes:
            print("\n#-------------#-------------#-------------#-------------|\n") 
            print("Id: ({}) {}".format(linha[0],linha[1])) #Imprimindo as questões do quiz conforme o nivel escolhido
            print("A)",linha[2])
            print("B)",linha[3])
            print("C)",linha[4])
            print("D)",linha[5])
            print("Resposta Certa:", linha[6])
        print("\n#-------------#-------------#-------------#-------------|")
        print("\n^-------------^-------------^-------------^-------------|")
    
    if tip == 1:
        return nivel
    else:
        conf_quiz()
    
def atualizar(niv): #Modifica a questão desejada do quiz definida pelo ID e pelo nivel escolhido
    if niv < 1 or niv > 3:
        print("Inválido")
        menu_atualizar_q()
    else: 
        id = int(input("\nInforme o Id da Questão que Você Deseja Modificar:"))
        novo_eniciado = input("\nInforme um Novo Enunciado: ")
        novo_a = input("Informe uma nova letra 'A': ")
        novo_b = input("Informe uma nova letra 'B': ")
        novo_c = input("Informe uma nova letra 'C': ")
        novo_d = input("Informe uma nova letra 'D': ")
        novo_certo = input("Informe a letra que corresponde a resposta correta: ")
        con = sqlite3.connect("quiz_db.db")
        cursor = con.cursor()

        if niv == 1:
            cursor.execute("UPDATE facil SET enunciado=?,a=?,b=?,c=?,d=?,certo=? WHERE id=?",[novo_eniciado,novo_a,novo_b,novo_c,novo_d,novo_certo.lower(),id])
        if niv == 2:
            cursor.execute("UPDATE medio SET enunciado=?,a=?,b=?,c=?,d=?,certo=? WHERE id=?",[novo_eniciado,novo_a,novo_b,novo_c,novo_d,novo_certo.lower(),id])
        if niv == 3:
            cursor.execute("UPDATE dificil SET enunciado=?,a=?,b=?,c=?,d=?,certo=? WHERE id=?",[novo_eniciado,novo_a,novo_b,novo_c,novo_d,novo_certo.lower(),id])

        print("\n----------------------------------\n| Questão Atualizada Com Sucesso |\n----------------------------------")
        con.commit()
        con.close()
        conf_quiz()

def menu_atualizar_q(): #Antes de modificar os a questão do quiz o adiministrador vai escolher se deseja ver a lista com as questões ou não
    print("\n-------------------MODIFICAR QUESTÃO---------------------\n")
    ver = int(input("'1' Não Exibir Lista De Questões\n'2' Exibir Lista De Questões\nR: "))
    
    if ver == 2:
        nivel = exibir_q(1)
        atualizar(nivel)
    elif ver == 1:
        nivel = int(input("\nEscolha a dificuldade desejada:\n'1' Fácil\n'2' Médio\n'3' Difícil\nR: "))
        atualizar(nivel)    
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        menu_atualizar_q()

def conf_quiz(): #Apresenta as opções que o administrador pode utilizar na administração do quiz
    print("\n-------------------CONFIGURAÇÕES QUIZ---------------------\n")
    
    print("'1' Exibir questionário")
    print("'2' Modificar Questão")
    print("'9' Voltar")
    escolha = int(input("R: "))

    if escolha == 1:
        exibir_q(0)
    elif escolha == 2:
        menu_atualizar_q()
    
    elif escolha == 9:
        print("------------\n| Voltando |\n------------")
        pro_admin()
    else:
        print("\n------------------\n| Opção Inválida |\n------------------")
        conf_quiz()
 
#quiz_db.db
#
#TABLE facil(
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#enuciado VARCHAR(200),
#a VARCHAR(200),
#b VARCHAR(200),
#c VARCHAR(200),
#d VARCHAR(200),
#certo VARCHAR(1));
#
#TABLE medio(
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#enuciado VARCHAR(200),
#a VARCHAR(200),
#b VARCHAR(200),
#c VARCHAR(200),
#d VARCHAR(200),
#certo VARCHAR(1));
#
#TABLE dificil(
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#enuciado VARCHAR(200),
#a VARCHAR(200),
#b VARCHAR(200),
#c VARCHAR(200),
#d VARCHAR(200),
#certo VARCHAR(1));