from funcoes import pontos_telemetria
from funcoes import validar_temp
from funcoes import class_term
from funcoes import detectar_picos_vales
pontos = []
pontos_filtrados = []
classificados = []
picos = []


pontos_telemetria(pontos)

#validou e adicionou as temperaturas que estao dentro da margem de -100, 120
validar_temp(pontos, pontos_filtrados)

#classificando
class_term(pontos_filtrados,classificados)
classificados = sorted(classificados)

#achando os picos
detectar_picos_vales(pontos_filtrados, picos)
print(picos)
