import os
print("######4%&*+=-   Calculadora em Python!  -=+*&%4#####")
sair=""

while(sair != "s"):
    print("Qual operação deseja realizar?")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    op = input("Digite por favor uma das opções: ")
    if(op == "1"):
        print("Soma -> Digite dois números: ")
        num1 = int(input())
        num2 = int(input())
        print("A soma dos números é: ", num1 + num2)
        
    elif(op == "2"):
        print("Subtração -> Digite dois números: ")
        num1 = int(input())
        num2 = int(input())
        print("A subtração dos números é: ", num1 - num2)
        
    elif(op == "3"):
        print("Divisão -> Digite dois números: ")
        num1 = int(input())
        num2 = int(input())
        print("A divisão dos números é: ", int(num1 / num2))
        
    elif(op == "4"):
        print("Multiplicação -> Digite dois números: ")
        num1 = int(input())
        num2 = int(input())
        print("A multiplicação dos números é: ", num1 * num2)
    else:
        print("Opção inválida!")    
    sair = input("Digite s caso deseje sair:")
    os.system("cls")

print("Obrigado por usar nossa calculadora!")