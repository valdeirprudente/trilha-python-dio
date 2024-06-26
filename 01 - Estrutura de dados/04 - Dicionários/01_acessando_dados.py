dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234","extra":{"a":1}}
extra = dados["nome"]
print(extra)
print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Valdeir"
dados["idade"] = 41
dados["telefone"] = "99371-1170"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

