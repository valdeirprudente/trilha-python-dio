plano_essencial_fibra = "- RECOMENDADO - Plano Essencial Fibra - 50Mbps "
plano_prata_fibra = "- RECOMENDADO - Plano Prata Fibra - 100Mbps "
plano_premium_fibra = " - RECOMENDADO - Plano Premium Fibra - 300Mbps "
consumo = float(input("Informe seu consumo de mensal de internet em GB :  "))

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
def recomendar_plano(consumo):
 if consumo <= 10:
    return plano_essencial_fibra
 elif  consumo  <= 20  :
    return  plano_prata_fibra
 else:
     return plano_premium_fibra


# Solicita ao usuário que insira o consumo médio mensal de dados :

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print( recomendar_plano(consumo))