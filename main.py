import matplotlib.pyplot as plt
from funcoes import pontos_telemetria
from funcoes import class_term
from funcoes import detectar_picos_vales
from funcoes import validar_temp
pontos = []
pontos_filtrados = []
classificados = []
pontos_filtrados = []



pontos_telemetria(pontos)


#validou e adicionou as temperaturas que estao dentro da margem de -100, 120
validar_temp(pontos, pontos_filtrados)

#classificando
class_term(pontos_filtrados,classificados)


#achando os picos
detectar_picos_vales(pontos_filtrados, pontos_filtrados)




# colocando num grafico
tempo = []
for i in range(1, len(pontos_filtrados)+1):
    tempo.append(i)

plt.plot(tempo, pontos_filtrados, marker= 'o', color='black')

plt.xlabel('tempo(minutos)')
plt.ylabel('temperatura (C°)')
plt.grid(True)


# área quente (positivos)
plt.fill_between(
    tempo, pontos_filtrados, 0,
    where=[t >= 0 for t in pontos_filtrados],
    color="orange",
    alpha=0.3,
    label="Acima de 0°C"
)

# área fria (negativos)
plt.fill_between(
    tempo, pontos_filtrados, 0,
    where=[t < 0 for t in pontos_filtrados],
    color="blue",
    alpha=0.3,
    label="Abaixo de 0°C"
)


plt.show()