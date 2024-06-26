def calcular_total(numeros):
    return sum(numeros)

def retorna_sucessor_e_antececssor(numero):
    antecessor  = numero - 1
    sucessor = numero + 1
    
    return antecessor,sucessor

print(calcular_total([10,1000,28,32]))
print(retorna_sucessor_e_antececssor(10))

def  func_3():
    print("Olá Mundo")
    return None
    
print(func_3())