lista = [1, "Python", [40, 30, 20]]

copia_lista = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(id(copia_lista), id(lista))

copia_lista = ["pera","laranja","uva"]
print(copia_lista)
print(lista)
