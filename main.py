"""Simulação e análise da telemetria térmica de um satélite em LEO (500 km)."""

import math

import matplotlib.pyplot as plt

import funcoes

# ---------- Órbita (3ª Lei de Kepler) ----------
RAIO_TERRA = 6371                # km
ALTITUDE = 500                   # km
MU_TERRA = 398600                # parâmetro gravitacional da Terra (km³/s²)
TEMPO_SOL = 59                   # minutos no sol em cada órbita
# o resto da órbita (~36 min) é eclipse

# ---------- Telemetria ----------
DURACAO = 150                    # minutos simulados
INTERVALO = 3                    # 1 leitura a cada 3 min
TEMP_INICIAL = 10                # °C
TEMP_SOL = 85                    # temperatura de equilíbrio no sol (°C)
TEMP_ECLIPSE = -75               # temperatura de equilíbrio no eclipse (°C)
TAXA = 0.1                       # constante de aproximação (resfriamento de Newton)


def calcular_periodo():
    """Período orbital em minutos (~94,5) pela 3ª Lei de Kepler."""
    a = RAIO_TERRA + ALTITUDE    # raio da Terra + altitude (km)
    return 2 * math.pi * math.sqrt(a**3 / MU_TERRA) / 60


def gerar_telemetria(periodo):
    """Gera as leituras de temperatura ao longo do tempo.

    A temperatura vai se aproximando aos poucos de 85 °C no sol
    e de -75 °C no eclipse (Lei do Resfriamento de Newton).
    """
    tempos = []
    temperaturas = []
    temp = TEMP_INICIAL

    for minuto in range(0, DURACAO + 1, INTERVALO):
        tempos.append(minuto)
        temperaturas.append(round(temp, 1))

        if minuto % periodo < TEMPO_SOL:
            alvo = TEMP_SOL      # sol
        else:
            alvo = TEMP_ECLIPSE  # eclipse

        temp = temp + TAXA * (alvo - temp)

    # duas leituras com erro de sensor, para testar o filtro
    temperaturas[12] = 250
    temperaturas[41] = -180

    return tempos, temperaturas


def filtrar_leituras(tempos, temperaturas):
    """Descarta as leituras fora da faixa do sensor."""
    tempos_ok = []
    temps_ok = []
    for i in range(len(temperaturas)):
        if funcoes.validar_temperatura(temperaturas[i]):
            tempos_ok.append(tempos[i])
            temps_ok.append(temperaturas[i])
        else:
            print("Erro de sensor no minuto", tempos[i], "->", temperaturas[i], "°C descartado")
    return tempos_ok, temps_ok


def mostrar_leituras(tempos_ok, temps_ok, picos, vales):
    """Imprime cada leitura com sua classificação, e os picos e vales."""
    for i in range(len(temps_ok)):
        print(tempos_ok[i], "min |", temps_ok[i], "°C |", funcoes.classificar_termica(temps_ok[i]))

    for i in picos:
        print("Pico no minuto", tempos_ok[i], "->", temps_ok[i], "°C")
    for i in vales:
        print("Vale no minuto", tempos_ok[i], "->", temps_ok[i], "°C")


def plotar_grafico(tempos_ok, temps_ok, picos, vales, periodo):
    """Gera o gráfico da telemetria e salva em grafico_telemetria.png."""
    plt.figure(figsize=(11, 5))

    plt.plot(tempos_ok, temps_ok, marker="o", color="navy", label="Temperatura")

    # limites da tabela
    plt.axhline(funcoes.LIMITE_CRITICO_QUENTE, color="red", linestyle="--",
                label="Limite crítico (70 / -40 °C)")
    plt.axhline(funcoes.LIMITE_CRITICO_FRIO, color="red", linestyle="--")
    plt.axhline(funcoes.LIMITE_ATENCAO_QUENTE, color="orange", linestyle="--",
                label="Limite de atenção (50 / -20 °C)")
    plt.axhline(funcoes.LIMITE_ATENCAO_FRIO, color="orange", linestyle="--")

    # eclipse em cinza (o 2º eclipse só começaria depois dos 150 min)
    plt.axvspan(TEMPO_SOL, periodo, color="gray", alpha=0.3, label="Eclipse")

    # picos e vales
    for i in picos:
        plt.plot(tempos_ok[i], temps_ok[i], "r^", markersize=12)
    for i in vales:
        plt.plot(tempos_ok[i], temps_ok[i], "bv", markersize=12)

    plt.title("Temperatura do Satélite - LEO 500 km (1,7 órbitas)")
    plt.xlabel("Tempo (minutos)")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True, alpha=0.3)
    plt.xlim(0, DURACAO)
    plt.legend(loc="lower left")
    plt.savefig("grafico_telemetria.png", dpi=300)
    plt.show()


def main():
    periodo = calcular_periodo()
    print("Período orbital:", round(periodo, 1), "min")

    tempos, temperaturas = gerar_telemetria(periodo)
    tempos_ok, temps_ok = filtrar_leituras(tempos, temperaturas)

    picos, vales = funcoes.detectar_picos_vales(temps_ok)
    mostrar_leituras(tempos_ok, temps_ok, picos, vales)

    funcoes.gerar_relatorio(temps_ok)
    plotar_grafico(tempos_ok, temps_ok, picos, vales, periodo)


if __name__ == "__main__":
    main()