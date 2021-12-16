print("\tMaior ou Menor com estrutura de repetição")
print("\t\t     By Satur")
print()

try: 
    num1 = int(input("Digite um número:"))
    num1 == int and num1 >= 0
    if num1 < 0:
        while num1<0:
            print("Erro! insira um número maior que 0")
            num1 = int(input("Digite um número:"))
            if num1<0:
                continue

except ValueError:
    print("Error")

try:
    num2 = int(input("Digite outro número:"))
    num2 == int and num2 >= 0
    if num2 < 0:
        while num2<0:
            print("Erro! insira um número maior que 0")
            num2 = int(input("Digite um número:"))
            if num2<0:
                continue
    
except ValueError:
    print("Error")

if num1>=num2:
    print("O maior número é", num1)

elif num2>=num1:
    print("O maior número é", num2)

elif num1==True:
    print("Esse número é verdadeiro")

elif num2==True:
    print("Esse número é verdadeiro")
else:
    print("Erro")
