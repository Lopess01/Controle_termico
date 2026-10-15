# Controle Térmico de Satélite

Simulação e análise da telemetria térmica de um satélite em órbita baixa (LEO, 500 km).

## O que o programa faz

1. Calcula o período orbital (~94,5 min) pela 3ª Lei de Kepler.
2. Gera 150 min de telemetria (1 leitura a cada 3 min): a temperatura tende a 85 °C no sol
   e a -75 °C no eclipse (Lei do Resfriamento de Newton).
3. Descarta leituras com erro de sensor (fora de -100 °C a 120 °C).
4. Classifica cada leitura:

   | Faixa (°C)        | Classificação                                  |
   |-------------------|------------------------------------------------|
   | < -40             | Cold Case Crítico - Alerta de Falha Imediata   |
   | -40 a -20         | Frio (Atenção) - Ligar Aquecedores             |
   | -20 a 50          | Nominal (Ideal) - Operação Padrão              |
   | 50 a 70           | Quente (Atenção) - Desligar Cargas Úteis       |
   | > 70              | Hot Case Crítico - Alerta de Degradação        |

5. Detecta picos e vales, imprime um relatório e gera o gráfico `grafico_telemetria.png`.

## Estrutura

- `main.py` — simulação da órbita, geração da telemetria e gráfico.
- `funcoes.py` — validação, classificação, detecção de picos/vales e relatório.

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

