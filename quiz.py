<<<<<<< HEAD
import sqlite3
from principal import pro_intro

def pro_quiz(dad):#Apresenta o quiz(o parametro 'dad' é a lista com os dados do usuario: ID, nome e pontos)
    print("\n---------------------QUIZ-----------------------\n\nVamos testar seus conhecimentos",dad[1])
    print("Serão 10 perguntas\n")
    dados = dad
    
    while True:
        dificu_quiz = int(input("Selecione a dificuldade, ou volte:\n\n'1' Fácil\n'2' Médio\n'3' Difícil\n'9' Voltar\nR: "))
        con = sqlite3.connect("quiz_db.db")
        cursor = con.cursor()
        
        if dificu_quiz == 1:
            cursor.execute("SELECT * FROM facil")
            soma_pont = 1
        elif dificu_quiz == 2:
            cursor.execute("SELECT * FROM medio") #Conforme a escolha da dificuldade o sistema vai acessar o banco de dados
            soma_pont = 2
        elif dificu_quiz == 3:
            cursor.execute("SELECT * FROM dificil")
            soma_pont = 3
        elif dificu_quiz == 9:
            con.close()
            pro_intro(dados)

        questoes = cursor.fetchall()
        con.commit()
        con.close()
        pontuacao = 0
        acertos = 0

        for linha in questoes: #Exibindo as questões para o usuario
            print()
            print("{}- {}".format(linha[0],linha[1]))
            print("A)",linha[2])
            print("B)",linha[3]) 
            print("C)",linha[4])
            print("D)",linha[5])
            resposta = input("R: ")
            print("\n#-------------#-------------#-------------#-------------|")
            
            if resposta.lower() == linha[6]: #Se a resposta for correta
                print("Resposta Correta")
                pontuacao += soma_pont
                acertos += 1
            else: #Se a resposta estiver incorreta
                print("Resposta Errada")
                print("Correta:", linha[6])

        print("\n\n*******************************************************************\n")

        lista_respostas = ["Camuflar um erro seu é anular a busca pelo conhecimento. Aprenda com eles e faça novamente de forma correta.",
        "Vish, só 1, estude mais da próxima vez!","2 é melhor que 1, mas ainda é ruim, estude mais!",
        "3 para mais sorte e mais estudo da próxima vez!","4 é um belo número, mas não vai te dar muitos pontos aqui, estude mais!",
        "Meio certo e meio errado, estude mais um pouco!","Foi bom, mas pode ser melhor","Parabéns, você foi muito bem!",
        "Wooow, você foi incrivel, só errou 2","NOSSAAA!!! Você foi quase perfeito, parabéns!!!",
        "PERFEITO!!! Você conseguiu a pontuação máxima, sem palavras!!!"] #Respostas que seram imprimidas dependendo da pontuação
        
        print(dad[1],"você acertou", acertos, "perguntas e sua pontuação foi", pontuacao) #Mensagens finais com pontuação, acertos e pontuação atualizada
        print(lista_respostas[acertos])
        pontos_velhos = int(dad[2])
        nova_pontuacao = pontuacao + pontos_velhos
        print("Agora você está com", nova_pontuacao, "pontos")
        
        con = sqlite3.connect("Usuarios.db")
        cursor = con.cursor()
        cursor.execute("UPDATE novo SET pontos=? WHERE id=?", [nova_pontuacao, dad[0]]) #Atualiza a pontuação no banco de dados
        cursor.execute("SELECT * FROM novo WHERE id='"+dad[0]+"';")
        con.commit()
        novo_p = cursor.fetchall()
        con.close()
        dados = []

        for linha in novo_p:
            dados.append(linha[0])
            dados.append(linha[1]) #Adciona os dados atualizados a uma lista para ser o novo parametro do pro_intro
            dados.append(linha[2])
        print("\nVamos novamente?")

        
=======
def pro_quiz():
    print("-------------------------------------------------------------------------------------------------------\nAgora vamos testar seus conhecimentos\n")
    print("Seram 10 perguntas\n")
    
    while True:
        dificu_quiz = input("Selecione a dificuldade:\n\n'F' Facil\n'M' Médio\n'D' Dificil\n'V' Voltar\nR= ")
        
        if dificu_quiz == 'F' or dificu_quiz == 'f':
            dific = 1
            sistem_quiz(dific)
       
        elif dificu_quiz == 'M' or dificu_quiz == 'm':
            dific = 2
            print("-------------------------------------------------------------------------------------------------------\nem breve...\n-------------------------------------------------------------------------------------------------------")
        
        elif dificu_quiz == 'D' or dificu_quiz == 'd':
            dific = 4
            print("-------------------------------------------------------------------------------------------------------\nem breve...\n-------------------------------------------------------------------------------------------------------")
        
        elif dificu_quiz == 'v' or dificu_quiz == 'V':
            from principal import pro_intro
            pro_intro()
            
def sistem_quiz(dificuldade):

    facil = [['1) O que significa ‘concatenar’?\n','A) Trata-se de um conjunto de caracteres\nB) Configurar o tipo de uma variável\nC) Dividir duas variáveis\nD) Unir dados de modos lógicos ou manter ligação ou conexão entre eles. ','D'],
        ['2) O que é um algoritmo?\n','A) São ações ditas ao computador para ele executar\nB) é a solução de um problema\nC) Trata-se de uma sequência de passos conhecida como um conjunto de instruções para se chegar a um determinado objetivo.\nD) Permite realizar operações lógicas e aritméticas utilizando apenas dois dígitos ou dois estados (sim ou não. verdadeiro ou falso, tudo ou nada, ligado ou desligado) ','C'],
        ['3) Marque a opção correta que define a estrutura de repetição ''PARA - ATÉ'' (Em inglês, "For"):\n','A) Caso o resultado seja falso encerra essa estrutura e volta para o fluxo do programa.\nB) Estrutura de repetição que realiza um teste lógico no final da estrutura, executando ao menos uma vez o conjunto de instruções antes de verificar a condição testada.\nC) Estrutura de repetição que realiza um teste lógico no início da estrutura e sempre que o teste lógico resultar em VERDADEIRO, os comandos associados a esta estrutura são executados. ','B'],
        ['4) Qual dos grupos apresentados abaixo apresenta apenas paradigmas de programação?\n','A) Imperativo, Funcional, Lógico e Orientado a Objetos.\nB) Algol, Basic, Lógico e Orientado a Objetos\nC) Imperativo, Programar, Lógico e Orientado a Objetos\nD) Orientado a Objetos, Java, Imperativo e Lógico ','A'],
        ['5) Analise o algoritmo abaixo e responda qual condicional está sendo utilizada:\n\nalgoritmo "Condicional"\n\nvar\nSALARIO: REAL\n\ninicio\nESCREVA ( “Digite o salário: ”\nLEIA ( SALARIO )\n\nSE ( SALARIO <= 2000 ) ENTAO\nESCREVA ( “Candidato selecionado para primeira fase da condicional” )\nSENAO\nESCREVA( “Candidato NÃO PREENCHEU OS REQUISITOS da condicional” )\n\nFIMSE\n\nfinalgoritmo\n','A) Condicional Encadeada\nB) Condicional Composta.\nC) Condicional Simples ','B']
        ]

    medio = []
    dificil = []

    if dificuldade == 1:
        dif = facil
    
    elif dificuldade == 2:
        dif = medio
    
    elif dificuldade == 3:
        dif = dificil

    pontuacao = 0
    for num in range(5):
        print("\n-------------------------------------------------------------------------------------------------------")
        print(dif[num][0])
        print(dif[num][1])
        rquiz = input("R: ")
        rquiz = rquiz.upper()
               
        if rquiz == dif[num][2]:
            print("-------------------------------------------------------------------------------------------------------\n\nCerto")
            pontuacao += 1       
        else:
            print("-------------------------------------------------------------------------------------------------------\n\nErrado")
    print("-------------------------------------------------------------------------------------------------------\nSUA PONTUAÇÃO FOI:", pontuacao)
    nada = input("\n\n'ENTER' para continuar\n-------------------------------------------------------------------------------------------------------")
pro_quiz()



    
>>>>>>> fe227c4 (versão 0.1)
