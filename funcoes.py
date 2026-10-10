"""Funções de análise térmica da telemetria do satélite."""

# ---------- Limites ----------
# Faixa física do sensor: fora disso a leitura é considerada erro
SENSOR_MIN = -100
SENSOR_MAX = 120

# Limites da tabela de classificação térmica (°C)
LIMITE_CRITICO_FRIO = -40
LIMITE_ATENCAO_FRIO = -20
LIMITE_ATENCAO_QUENTE = 50
LIMITE_CRITICO_QUENTE = 70


# ---------- Funções ----------
def validar_temperatura(t):
    """Retorna True se a leitura está dentro da faixa física do sensor."""
    return SENSOR_MIN <= t <= SENSOR_MAX


def classificar_termica(t):
    """Classifica a temperatura de acordo com a tabela de limites."""
    if t < LIMITE_CRITICO_FRIO:
        return "Cold Case Crítico - Alerta de Falha Imediata"
    elif t < LIMITE_ATENCAO_FRIO:
        return "Frio (Atenção) - Ligar Aquecedores"
    elif t <= LIMITE_ATENCAO_QUENTE:
        return "Nominal (Ideal) - Operação Padrão"
    elif t <= LIMITE_CRITICO_QUENTE:
        return "Quente (Atenção) - Desligar Cargas Úteis"
    else:
        return "Hot Case Crítico - Alerta de Degradação"


def detectar_picos_vales(lista):
    """Retorna os índices dos picos e dos vales (máximos e mínimos locais)."""
    picos = []
    vales = []
    for i in range(1, len(lista) - 1):
        if lista[i] > lista[i - 1] and lista[i] > lista[i + 1]:
            picos.append(i)
        if lista[i] < lista[i - 1] and lista[i] < lista[i + 1]:
            vales.append(i)
    return picos, vales


def gerar_relatorio(lista):
    """Imprime um resumo (máxima, mínima e média) das leituras válidas."""
    print("----- RELATÓRIO DO SATÉLITE -----")
    print("Leituras válidas:", len(lista))
    print("Máxima:", max(lista), "°C ->", classificar_termica(max(lista)))
    print("Mínima:", min(lista), "°C ->", classificar_termica(min(lista)))
    print("Média:", round(sum(lista) / len(lista), 1), "°C")
