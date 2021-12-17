<<<<<<< HEAD
def pro_intro(dad): #Apresenta as opções para o usuario (o parametro 'dad' é a lista com os dados do usuario: ID, nome e pontos)
    from quiz import pro_quiz
    from pesquisa import pro_pesquisa
    from material import listar_material

    intro = ''
    while True:
        print("--------------------------------------------------")
        print("Olá {} sua pontuação é {}\n".format(dad[1],dad[2])) #Mensagem informativa sobre a pontuação do usuario
        print("O que você deseja?\n")
        intro = int(input("'1' para o Quiz\n'2' para pesquisa\n'3' para acessar o material\n'9' para sair\nR: "))

        if intro == 1:
            pro_quiz(dad)
        elif intro == 2:
            pro_pesquisa(dad)
        elif intro == 3:
            listar_material(dad,continuar = 0,topico = 0)
        elif intro == 9:
            exit()
        else:
            print("-------------------------------------------------------------------------------------------------------\n\nOpção Inválida")

=======
def pro_intro():

    intro = ''
    while True:
        print()
        print("-------------------------------------------------------------------------------------------------------\nO que você deseja?\n")
        intro = input("'P' para pesquisa\n'Q' para o Quiz\n'M' para acessar o material\n'S' para sair\nR= ")

        if intro == 'q' or intro == 'Q':
            from quiz import pro_quiz
            pro_quiz()

        elif (intro == 'p') or (intro == 'P'):
            from pesquisa import pro_pesquisa

        elif (intro == 'm') or (intro == 'M'):
            from material import pro_material
        
        elif (intro == "s") or (intro == "S"):
            exit()
        
        else:
            print("-------------------------------------------------------------------------------------------------------\n\nOpção Invalida")
pro_intro()
>>>>>>> fe227c4 (versão 0.1)
    
