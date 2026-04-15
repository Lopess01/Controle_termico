# fazendo os pontos de telemetria
import random

def pontos_telemetria(d):
    for i in range(50):
        n = round(random.randint(-150,150), 2)
        d.append(float(n))
    
# validando temperatura
def validar_temp(t, f):
    for i in t:
        if -100 < i < 120:
            f.append(i)   

# classificando as temperaturas
def class_term(filtrados, classificados):
    for temp in filtrados:
        if temp < - 40:
            classificados.append([temp, 'critical cold case'])
        elif -40 < temp < -20:
            classificados.append([temp,'frio(atenção)'])
        elif -20 < temp < 50:
            classificados.append([temp, 'ideal'])
        elif 50 < temp < 70:
            classificados.append([temp, 'quente'])
        elif temp > 70:  
            classificados.append([temp, 'critical hot case'])

def detectar_picos_vales(pontos_filtrados, picos):
    for temp in range(1, len(pontos_filtrados) - 1):
        if pontos_filtrados[temp] > pontos_filtrados[temp + 1] and pontos_filtrados[temp] > pontos_filtrados[temp-1]:
            picos.append(temp)
    for temp in range(1, len(pontos_filtrados) - 1):
        if pontos_filtrados[temp] < pontos_filtrados[temp + 1] and pontos_filtrados[temp] < pontos_filtrados[temp-1]:
            picos.append(temp)



        

            