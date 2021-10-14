def pro_login():
    entrada = int(input("'1' para entrar com login / '2' criar login\nR: "))
    if entrada == 2:
        pro_novo_usuario()
    elif entrada == 1:
        usuario()

def usuario():
    cod = input("Seu login: ")
    global lista_u
    lista_u = []
    
    with open('Clientes.txt','r') as pessoa:
        for n_linha, l in enumerate(pessoa, 1):
            if cod in l:
                lista_u.append(l[:10].replace("\n","").replace(" ",""))   #codigo
                lista_u.append(l[10:30].replace("\n","").replace(" ","")) #nome
                lista_u.append(l[30:].replace("\n","").replace(" ",""))   #pontuação
                from principal import pro_intro
                pro_intro()

def dados():
    return lista_u 
    
def info_usuario(lista, tipo):
    with open('Clientes.txt','r') as pessoa:
        for n_linha, l in enumerate(pessoa, 1):
            if tipo == 'cod':
                if lista[0] in l:
                    return l[:10].replace("\n","").replace(" ","")
            elif tipo == 'nome':
                if lista[1] in l:
                    return l[10:30].replace("\n","").replace(" ","")
            elif tipo == 'pont':
                if lista[3] in l:
                    return l[30:].replace("\n","").replace(" ","")
                
def pro_novo_usuario():                            # Vai adicionar um novo usuario ao arquivo Clientes.py 
    lista = []
    cod = input("Digite um login com 4 digitos: ")

    pessoa = open('Clientes.txt','r')
    texto = pessoa.read()
    ocorrencia = texto.count(cod)
    pessoa.close()

    if len(cod) > 4 or len(cod) < 4:

        print("QUATRO DIGITOS")
        pro_novo_usuario()

    elif ocorrencia > 0:

        print("LOGIN EXISTENTE, TENTE OUTRO")
        pro_novo_usuario()

    else:
        lista.append(cod)
        nome = input("Digite seu nick (Até 10 caracteres): ")
        lista.append(nome)
        lista.append(0)
        atualizacao_dados(lista)
        print("Usuario", info_usuario(lista, 'nome'), "Cadastrado com sucesso" )

def atualizacao_dados(dados):                       
    with open('Clientes.txt','a') as new_pessoa:
        for lis in dados:
            new_pessoa.write("{:10} ".format(lis))
        new_pessoa.write("\n")

pro_login()
##########################################################################

#ref_arquivo = open("qbdata.txt","r")
#linha = ref_arquivo.readline()
#while linha:
#    valores = linha.split()
#    print('QB ', valores[0], valores[1], 'obteve a avaliacao ', valores[10] )
#    linha = ref_arquivo.readline()

#ref_arquivo.close()

#def get_line(word):
#    with open('Arquivo.txt') as f:
#        for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
#            if word in l: # ver se palavra esta na linha
#                return l_num
#        return False # não foi encontrada


        
        

     
