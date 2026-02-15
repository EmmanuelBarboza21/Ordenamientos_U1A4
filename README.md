# Evaluación de Métodos de Ordenamiento (Burbuja vs Quicksort) — U1A4

## Objetivo

Implementar y evaluar en Python dos métodos de ordenamiento (Bubble Sort y Quicksort) usando Visual Studio Code, comparando su rendimiento mediante pruebas controladas (`timeit`) en distintos tamaños de entrada y escenarios de datos.

---

## Requisitos

- Python 3.11 (o 3.10+ recomendado)
- No se requieren librerías externas (solo librerías estándar de Python)

---

## Estructura del repositorio

Ordenamientos_U1A4/
│
├── src/
│ ├── sorting.py
│ └── benchmark.py
│
├── results/
│ └── benchmark_results.csv
│
├── .gitignore
└── README.md

---

## Algoritmos implementados

### 1️⃣ Bubble Sort
Algoritmo de ordenamiento basado en comparaciones sucesivas e intercambios adyacentes.

- Complejidad promedio: **O(n²)**
- Peor caso: **O(n²)**
- Ventaja: implementación sencilla
- Desventaja: bajo rendimiento en listas grandes

### 2️⃣ Quicksort (versión iterativa)

Se implementó una versión iterativa para evitar problemas de límite de recursión en Python. Se utiliza pivote aleatorio para reducir la probabilidad de peor caso.

- Complejidad promedio: **O(n log n)**
- Peor caso: **O(n²)**
- Ventaja: excelente escalabilidad
- Justificación de versión iterativa: evita errores de recursión profunda y mejora estabilidad en pruebas grandes.

---

## Cómo ejecutar

1. (Opcional, recomendado) Crear y activar entorno virtual:

```bash
python -m venv .venv
Ejecutar el benchmark:
python src/benchmark.py
Los resultados se guardarán automáticamente en:
results/benchmark_results.csv
Descripción de las pruebas

Se evaluaron ambos algoritmos bajo las siguientes condiciones:

Tamaños de entrada

100

1 000

5 000

10 000

Escenarios

Lista aleatoria

Lista invertida

Configuración experimental

5 repeticiones por combinación (tamaño / escenario / algoritmo)

Medición con timeit

Cálculo de:

Tiempo promedio (segundos)

Desviación estándar

Resultados

Los resultados completos pueden consultarse en:
results/benchmark_results.csv
Se midió el rendimiento comparando:

Tamaño de entrada

Escenario de datos

Algoritmo utilizado

Promedio de tiempo

Desviación estándar

Los datos experimentales confirman la diferencia de escalabilidad entre ambos algoritmos.

Análisis comparativo
Escalabilidad

Bubble Sort presenta crecimiento cuadrático O(n²). Esto implica que al aumentar el tamaño de la lista, el tiempo de ejecución crece de manera acelerada, especialmente en listas invertidas, donde se aproxima al peor caso.

Quicksort presenta comportamiento promedio O(n log n), lo que permite que el tiempo crezca de forma mucho más controlada conforme aumenta el tamaño de entrada.

Relación con la teoría

Los resultados obtenidos concuerdan con la complejidad teórica esperada:

Bubble Sort → O(n²)

Quicksort → O(n log n)

La diferencia se vuelve especialmente evidente en tamaños grandes como 5 000 y 10 000 elementos.

Impacto práctico en robótica

En aplicaciones de robótica, el tiempo de cómputo es crítico para:

Procesamiento de datos de sensores

Toma de decisiones en tiempo real

Control de movimiento

Sistemas embebidos con recursos limitados

Un algoritmo con complejidad O(n²) puede convertirse en un cuello de botella cuando el volumen de datos crece.

En contraste, algoritmos como Quicksort permiten procesar información de forma más eficiente, reduciendo latencia y mejorando la capacidad de respuesta del sistema robótico.

Conclusión

Bubble Sort es adecuado únicamente para conjuntos de datos pequeños o fines educativos.

Quicksort demostró ser significativamente más eficiente y escalable, siendo más apropiado para aplicaciones reales donde el rendimiento es un factor crítico.

Los resultados experimentales validan la importancia de elegir algoritmos con mejor complejidad temporal en sistemas que requieren eficiencia computacional.
