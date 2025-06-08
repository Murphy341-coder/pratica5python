from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # sem considerar anos bissextos
    return idade_dias

# Exemplo de uso:
print(calcular_idade_em_dias(1992))  # Saída aproximada para alguém nascido em 1992
