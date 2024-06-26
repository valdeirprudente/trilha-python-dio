def soma(x,y): #função returna operações aritméticas entre x e y
    num = x * 2 + y * 3
    return num       
print(soma(50,60))

def antecessor_sucessor(x,y): #função retorna  antecessor e sucessor de um número 
    antecessor  =  x - 1
    sucessor = x + 1
    return antecessor,sucessor

print(antecessor_sucessor(1000,1001))

def area(largura, comprimento):
    area_terreno = largura * comprimento
    return area_terreno
print(f"A área total do terreno é: {area(15,30)} metros quadrados ")  

def calcular_media(notas): #função calcular média aritmética 
    soma_notas = sum(notas)
    media = soma_notas /len(notas)
    return media
notas = [7.5 , 8.2 , 6.9 , 8.1]
media = calcular_media(notas)
print(f" A média aritmética é: {media}")

def validar_idade(idade):    #função validar idade    
    if idade >= 18:
        return True
    else:
        return False
    
idade = int(input("Digite o valor da sua idade  : "))
if validar_idade(idade):
     print("Você já é maior de idade ")
else:
    print("Você ainda nao é maior de idade ")
    
def calcular_desconto(total, cupom):
    if cupom ==  "DESC10":
        desconto = total * 0.1
        return desconto
    else:
        return 0
    
#Chamada da função e impressão do desconto:
desconto_final = calcular_desconto(100,"DESC10")
print(f"Desconto aplicado :  {desconto_final}")

        




 