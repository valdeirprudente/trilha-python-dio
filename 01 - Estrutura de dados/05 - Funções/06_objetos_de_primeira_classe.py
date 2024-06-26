salario = 2000

def salario_bonus(bonus,lista):
    global salario
    lista_auxiliar = lista.copy()   
    lista_auxiliar.append(2)
    print(f"Lista auxiliar : {lista_auxiliar}  ")   
    salario += bonus
    return salario

    

lista = [1]
salario_com_bonus = salario_bonus(500,[2,3,4])
print(salario_bonus)
print(lista)

