# Cadenas de Markov: Predicción del Clima

Proyecto educativo en Python que simula un pronóstico del clima usando una cadena de Markov. El programa parte de un estado inicial, aplica una matriz de probabilidades de transición y genera una secuencia de estados climáticos para varios días.

## Descripción

Una cadena de Markov es un modelo probabilístico donde el siguiente estado depende únicamente del estado actual. En este proyecto se usa para predecir posibles cambios del clima entre tres estados:

- Soleado
- Nublado
- Lluvioso

El programa no predice clima real. Es una simulación basada en probabilidades definidas manualmente.

## Tecnologías Usadas

- Python 3
- NumPy
- Collections, módulo estándar de Python

## Archivo Principal

### `markov.py`

Este archivo contiene toda la lógica del proyecto. Su objetivo es simular el clima durante una cantidad determinada de días usando una matriz de transición.

## Explicación del Código

### Importación de librerías

```python
import numpy as np
```

Se importa NumPy para usar `np.random.choice`, función que permite elegir aleatoriamente el siguiente estado del clima respetando las probabilidades de la matriz de transición.

Más adelante también se importa:

```python
from collections import Counter
```

`Counter` se usa para contar cuántas veces aparece cada estado climático en el pronóstico generado.

## Estados del Clima

```python
estados = ["Soleado", "Nublado", "Lluvioso"]
```

Esta lista define los estados posibles del sistema. Cada estado representa una condición climática.

## Matriz de Transición

```python
matriz_transicion = [
    [0.8, 0.15, 0.05],
    [0.2, 0.6, 0.2],
    [0.25, 0.25, 0.5]
]
```

La matriz de transición indica la probabilidad de pasar de un estado actual a otro estado en el siguiente día.

Cada fila representa el estado actual y cada columna representa el posible siguiente estado:

| Estado actual | Soleado | Nublado | Lluvioso |
|---|---:|---:|---:|
| Soleado | 0.80 | 0.15 | 0.05 |
| Nublado | 0.20 | 0.60 | 0.20 |
| Lluvioso | 0.25 | 0.25 | 0.50 |

Ejemplo: si el día actual es `Soleado`, existe una probabilidad de 80% de que el siguiente día también sea `Soleado`, 15% de que sea `Nublado` y 5% de que sea `Lluvioso`.

## Configuración Inicial

```python
estado_inicial = "Soleado"
numero_dias = 10
```

Estas variables definen desde qué clima comienza la simulación y durante cuántos días se realizará el pronóstico.

- `estado_inicial`: estado climático con el que inicia la predicción.
- `numero_dias`: cantidad de días que se desean simular.

## Función `obtener_indice_estado`

```python
def obtener_indice_estado(estado):
    return estados.index(estado)
```

Esta función recibe el nombre de un estado y devuelve su posición dentro de la lista `estados`.

El índice es necesario para seleccionar la fila correcta dentro de la matriz de transición.

## Función `predecir_clima`

```python
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
```

Esta es la función principal del programa. Genera una lista con el pronóstico del clima.

Funcionamiento:

1. Guarda el estado inicial como primer día del pronóstico.
2. Obtiene el índice del estado actual.
3. Busca las probabilidades correspondientes en la matriz de transición.
4. Usa `np.random.choice` para seleccionar el siguiente estado según esas probabilidades.
5. Agrega el nuevo estado a la lista del pronóstico.
6. Repite el proceso hasta completar el número de días indicado.
7. Devuelve la lista final con todos los estados generados.

## Ejecución del Programa

```python
pronostico = predecir_clima(estado_inicial, numero_dias)
```

Esta línea ejecuta la simulación y guarda el resultado en la variable `pronostico`.

Después, el programa imprime en consola:

- Título del proyecto.
- Estado inicial.
- Número de días simulados.
- Pronóstico generado día por día.
- Estadísticas con la cantidad de días soleados, nublados y lluviosos.

## Ejemplo de Salida

La salida puede cambiar en cada ejecución porque el programa utiliza selección aleatoria basada en probabilidades.

```text
**************************************************
PREDICCION DEL CLIMA - CADENA DE MARKOV
**************************************************
Estado inicial: Soleado
Días a predecir: 10

Pronóstico para los próximos días:
**************************************************
  Día 1: Soleado
  Día 2: Soleado
  Día 3: Nublado
  Día 4: Nublado
  Día 5: Lluvioso
  Día 6: Lluvioso
  Día 7: Nublado
  Día 8: Soleado
  Día 9: Soleado
  Día 10: Soleado
Estadísticas de pronóstico:
**************************************************
Soleado: 5 días
Nublado: 3 días
Lluvioso: 2 días
```

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado Python 3.

También necesitas instalar NumPy:

```bash
pip install numpy
```

## Cómo Ejecutar el Proyecto

1. Clona o descarga este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Instala las dependencias:

```bash
pip install numpy
```

4. Ejecuta el archivo principal:

```bash
python markov.py
```

## Estructura del Proyecto

```text
cadenas-markov/
├── markov.py
└── README.md
```

## Conceptos Aplicados

- Cadenas de Markov
- Matrices de transición
- Probabilidad
- Simulación aleatoria
- Listas en Python
- Funciones
- Conteo de datos con `Counter`
- Uso básico de NumPy

## Posibles Mejoras

- Permitir que el usuario ingrese el estado inicial desde consola.
- Permitir que el usuario defina el número de días.
- Validar que el estado inicial exista en la lista de estados.
- Guardar el pronóstico en un archivo `.txt` o `.csv`.
- Graficar las estadísticas del pronóstico.
- Separar la lógica del programa de la impresión en consola.

## Autor

Proyecto desarrollado como práctica de fundamentos de inteligencia artificial y modelos probabilísticos por Angelica Flores
