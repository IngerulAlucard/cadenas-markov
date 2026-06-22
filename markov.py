import numpy as np

estados = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición de estados
matriz_transicion = [
    [0.8, 0.15, 0.05], #Transición desde Soleado
    [0.2, 0.6, 0.2],   #Transición desde Nublado
    [0.25, 0.25, 0.5]    #Transición desde Lluvioso
]

#Establecemos el estado inicial y el número de días para los cuales queremos predecir el clima:
estado_inicial = "Soleado"
numero_dias = 10

# Definimos una función para obtener el índice de un estado dado:
def obtener_indice_estado(estado):
    return estados.index(estado)

# creamos la función principal que realizará la predicción del clima:
def predecir_clima(estado_inicial, numero_dias):
    estado_actual = estado_inicial
    pronostico = [estado_actual]
    for _ in range(numero_dias - 1):
        indice_actual = obtener_indice_estado(estado_actual)
        probabilidades = matriz_transicion[indice_actual]
        siguiente_estado = np.random.choice(
            estados, 
            p=probabilidades
        )
        pronostico.append(siguiente_estado)
        estado_actual = siguiente_estado
    return pronostico

# ejecutamos la función y mostramos el pronóstico:
pronostico = predecir_clima(estado_inicial, numero_dias)
print("*" * 50)
print("🌦️ PREDICCION DEL CLIMA - CADENA DE MARKOV🌦️")
print("*" * 50)
print(f"🌍 Estado inicial: {estado_inicial}")
print(f"📅 Días a predecir: {numero_dias}\n")
print("📊 Pronóstico para los próximos días:")
print("*" * 50)
for dia, estado in enumerate(pronostico):
    print(f"  Día {dia+ 1}: {estado}")
print("Estadísticas de pronóstico:")
print("*" * 50)
from collections import Counter
conteo_estados = Counter(pronostico)
print(f"🌞 Soleado: {conteo_estados['Soleado']} días")
print(f"☁️ Nublado: {conteo_estados['Nublado']} días")
print(f"🌧️ Lluvioso: {conteo_estados['Lluvioso']} días")

