
nome = input("Digite teu nome: ")
nome = nome.upper()

print("\n")

print("-----------> CALCULADORA DO LUCAS, BEM VINDO(A) %s! <-----------------" %(nome))

print("\n")

print("1 - SOMAR")
print("2 - SUBTRAIR")
print("3 - DIVIDIR")
print("4 - MULTIPLICAR")

print("\n")


calculo = str(input("SELECIONE O CALCULO QUU DESEJAS (1/2/3/4): "))

print("\n")
#SOMAR
if calculo == '1':

    nro1 = int(input("DIGITE O NUMERO QUE QUER SOMAR: "))
    print("\n")
    nro2 = int(input("AGORA DIGITE OUTRO NUMERO: "))
    soma = nro1 + nro2
    print("\n")
    print("A soma total é: %s" %(soma))

    print("\n")

    print("MUITO OBRIGADO!")
    print("\n")
    print("SIGA-ME NO LINKEDIN -> linkedin.com/in/lucas-z-86a319160 OU NO PROPRIO GITHUB -> @LUCALOCO")    

#SUBTRAIR
elif calculo == '2':

    nro1 = int(input("DIGITE O NUMERO QUE QUER SUBTRAIR: "))
    print("\n")
    nro2 = int(input("AGORA DIGITE OUTRO NUMERO: "))
    sub = nro1 - nro2
    print("\n")
    print("A subtracao total é: %s" %(sub))

    print("\n")
#DIVISAO
elif calculo == '3':

    nro1 = int(input("DIGITE O NUMERO QUE QUER DIVIDIR: "))
    print("\n")
    nro2 = int(input("AGORA DIGITE OUTRO NUMERO: "))
    div = nro1 / nro2
    print("\n")
    print("A divisao total é: %s" %(div))

    print("\n")

        
    print("MUITO OBRIGADO!")
    print("\n")
    print("SIGA-ME NO LINKEDIN -> linkedin.com/in/lucas-z-86a319160 OU NO PROPRIO GITHUB -> @LUCALOCO")

##MULTIPLICAR
elif calculo == '4':

    nro1 = int(input("DIGITE O NUMERO QUE QUER MULTIPLICAR: "))
    print("\n")
    nro2 = int(input("AGORA DIGITE OUTRO NUMERO: "))
    multi = nro1 * nro2
    print("\n")
    print("A MULTIPLICACAO TOTAL É: %s" %(multi))

    print("\n")

    print("MUITO OBRIGADO!")
    print("\n")
    print("SIGA-ME NO LINKEDIN -> LINKEDIN.COM/IN/LUCAS-Z-86A319160 OU NO PROPRIO GITHUB -> @LUCALOCO")    

# SE NAO SELECIONOU NENHUM PRE PROGRAMADO
else:

    print("POR FAVOR, SELECIONE ALGUM NUMERO DE 1 A 4")
    
