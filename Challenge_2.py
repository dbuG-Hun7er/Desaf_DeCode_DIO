import sys

modelos_disponiveis = [
    {"nome": "Claude 3 Opus", "pontuacao_desempenho": 9, "preco_mensal": 600},
    {"nome": "Claude 3 Sonnet", "pontuacao_desempenho": 8, "preco_mensal": 450},
    {"nome": "Claude 3 Haiku", "pontuacao_desempenho": 7, "preco_mensal": 350},
]

def recomendar_modelo(modelos, orcamento):
    
    if orcamento < 250:
        return None, "Seu orçamento é muito baixo para recomendar um modelo adequado."

    modelos_dentro_orcamento = [modelo for modelo in modelos if modelo['preco_mensal'] <= orcamento]

    if not modelos_dentro_orcamento:
        modelo_mais_proximo = min(modelos, key=lambda x: abs(x['preco_mensal'] - orcamento))
        return modelo_mais_proximo['nome'], "Este modelo está mais próximo do seu orçamento."

    # Encontrar o modelo com o melhor desempenho dentro do orçamento
    melhor_modelo = max(modelos_dentro_orcamento, key=lambda x: x['pontuacao_desempenho'])
    return melhor_modelo['nome'], "Melhor desempenho dentro do seu orçamento."

orcamento_usuario = float(sys.stdin.read().strip())

modelo_recomendado, motivo = recomendar_modelo(modelos_disponiveis, orcamento_usuario)

if modelo_recomendado:
    sys.stdout.write(modelo_recomendado + ". " + motivo + "\n")
else:
    sys.stdout.write(motivo + "\n")
