<<<<<<< HEAD
from os import replace
import sqlite3
from adm import pro_admin
from principal import pro_intro

def pro_material():###chama a função desejada
    print("\n-------------------CONFIGURAÇÕES MATERIAL---------------------\n")
    print("Qual ação deseja realizar?\n'1' Listar todo material maxx = 50\n'2' Adicionar um novo material\n'3' Deletar algum material\n'4' Atualizar algum material\n'7' ###Deletar TODO o material###\n'9' Voltar ao início")
    acao = int(input("R: "))
    if acao == 1:
		###completo
        listar_tudo()
    elif acao == 2:
		###completo
        adc_material()
    elif acao == 3:
        #complete
        deletar_material()
    elif acao == 4:
		###completo
        atualizar_material()
    elif acao == 7:
        ###completo
        deletar_tudo()
    elif acao == 9:
        pro_admin()
    else:
        print("\nAção inválida tente novamente")
        pro_material()

def adc_material():###adiciona um novo material ao banco de dados
    conexao = sqlite3.connect("material.db")
    cursor = conexao.cursor()
    material = input("Cole aqui o material: ")
    sql = "INSERT INTO material (texto) VALUES ('" + material + "');"

    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    print("### MATERIAL INSERIDO ###")
    pro_material()

def listar_tudo():###lista todo o material por topicos
    print("Listando todo material:")
    conexao = sqlite3.connect("material.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM material;")
    material = cursor.fetchall()
    conexao.commit()
    conexao.close()
    
    for lista in material:
        print("--------------------------------------------------")
        print("ID:", lista[0])
        print(lista[1][:50])
    print("--------------------------------------------------")
    print()
    pro_material()
    
def listar_material(dad,topico,continuar):###apresente o material para o usuario
    print("\n-------------------CONFIGURAÇÕES MATERIAL---------------------\n")
    print("Qual tópico você deseja estudar hoje?")
    print("1º Lógica de programação\n\n    '1' Oque é um algoritmo\n    '2' Oque é lógica de programação\n    '3' Algoritimo de programação")
    print("2º Linguagem de programação Python\n\n    '4' Oque é uma linguagem de programção\n    '5' Interpretada ou compilada?\n    '6' Funções básicas do Python\n    '7' Referências e Cursos")
    if topico > 6:
        print("\n#### Parabéns você estudou todo o material, agora teste seus conhecimentos no quiz ou ou pesquisar\n algum termo desconhecido ou de uma olhada em outros materiais na internet \npara acessa-los é so usar CTRL + click do mouse, Até a proxima espero ter ajudado ####")
        pro_intro(dad)
    else:
        if continuar == 1:
            topico += 1
        else:
            topico = int(input("Digite o tópico escolhido: "))
    conexao = sqlite3.connect("material.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id,texto FROM material WHERE id=?;", [topico])
    material = cursor.fetchall()
    conexao.commit()
    conexao.close()
    for lista in material:
        print("-------------------------")
        print("    ", end="")
        j = 0
        for i in range(len(lista[1])):
            j += 1
            if lista[1][i] == '*':
               lista[1].replace(lista[1][i],"")
               print()
            else:
                print(lista[1][i],end="")
            #if j == 90 and topico != 6:
            #    print()
            #    j = 0
            
        print()
        print("-------------------------\n")
    continuar = int(input("1º Deseja ir para o próximo tópico?\n2º Voltar para a escolha dos tópicos?\n3º voltar para a tela inicial\nsua escolha:"))
    if continuar+6 == 8:
        listar_material(dad,topico=0,continuar=0)
    if continuar+6 == 9:
        pro_intro(dad)
    else:
        listar_material(dad,topico = topico,continuar=continuar)
    
def deletar_tudo():### deleta todo no banco
    conexao = sqlite3.connect("material.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM material;")
    conexao.commit()
    conexao.close()
    print("### TUDO EXCLUÍDO ####\n")
    pro_material()

def deletar_material():###deleta um material especifico pelo id
    conexao = sqlite3.connect("material.db")
    cursor = conexao.cursor()
    qual = int(input("Digite o id do material a ser excluído"))
    cursor.execute("DELETE FROM material WHERE id=?;", [qual])
    conexao.commit()
    conexao.close()
    print("### Material do ID "+ str(qual) +" EXCLUÍDO ####\n")
    pro_material()
    
def atualizar_material():###atualizada algum material especifico pelo id
    conexao = sqlite3.connect("material.db")
    cursor = conexao.cursor()
    qual_id = int(input("Digite o id:"))
    novo_texto = input("Novo material:")

    cursor.execute("UPDATE material SET texto = '"+novo_texto+"' WHERE id=?", [qual_id])
    conexao.commit()
    conexao.close()
    print("####ATUALIZADO COM SUCESSO####\n")
    pro_material()

#material.db
#table material
#id integer,
#texto text,
#PRIMARY KEY (id)
#TÓPICOS
#1º Lógica de programação
#    1º Oque é lógica de programação
#    2º Oque é algoritmo
#    3º Algoritimo de programação
#2º Linguagem de programação Python
#    4º Oque é uma linguagem de programção
#    5º Interpretada ou compilada?
#    6º Sintaxes básicas do Python
#    7°Referências e Cursos
=======
def pro_material():
    v = input("-------------------------------------------------------------------------------------------------------\n\nEm breve...\n\n'V' para voltar\nR:")
    if v == 'v' or v == 'V':
        from principal import pro_intro
        pro_intro()
pro_material()
>>>>>>> fe227c4 (versão 0.1)
