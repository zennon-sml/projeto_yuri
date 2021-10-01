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
    
