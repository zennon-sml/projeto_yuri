def pro_admin(): #Apresenta as opções para a escolha do administrador
    from adm_quiz import conf_quiz
    from adm_usuarios import conf_usu
    from adm_pesquisa import conf_pesq
    from material import pro_material

    print("\n-------------------OPÇÕES DE ADMINISTRADOR---------------------\n")
    print("Selecione a opção desejada:\n")    
    print("'1' Opções para Usuários")
    print("'2' Opções para Quiz")
    print("'3' Opções para Pesquisa")
    print("'4' Opções para Material")
    print("'9' Sair")
    r = int(input("R: "))
    
    if r == 1:
        conf_usu() #Encaminha para administração de usuarios
    elif r == 2:
        conf_quiz() #Encaminha para administração de quiz
    elif r == 3:
        conf_pesq() #Encaminha para administração de pesquisa
    elif r == 4:
        pro_material() #Encaminha para administração de material
    elif r == 9:
        print("\n----------------------------\n| Até a Proxima Meu Patrão |\n----------------------------")
        quit()
               
    else:
        print("\nInválido!")
        pro_admin()


