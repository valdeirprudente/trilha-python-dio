contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()

print(copia)
copia["guilherme@gmail.com"] = {"nome":"valdeir"}
print(contatos)
print(copia)