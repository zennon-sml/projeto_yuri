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



    
