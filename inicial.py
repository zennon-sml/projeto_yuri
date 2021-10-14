def inicio():
    entrada = int(input("'1' para entrar como visitante / '2' para entrar com login ou criar login\nR: "))
    if entrada == 2:
        from login import pro_login
        pro_login()

    elif entrada == 1:
        from principal import pro_intro 
        pro_intro()

    else:
        print("INVALIDO")
        inicio()
inicio()