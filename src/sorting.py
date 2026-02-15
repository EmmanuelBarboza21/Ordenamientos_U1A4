# src/sorting.py
from __future__ import annotations
from typing import List
import random

def bubble_sort(lista: List[int]) -> List[int]:
    """
    Ordena y devuelve una NUEVA lista usando Bubble Sort.
    Complejidad esperada: O(n^2).
    """
    a = lista.copy()
    n = len(a)

    for i in range(n):
        swapped = False
        # cada pasada empuja el mayor al final
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        # optimización: si no hubo intercambios, ya está ordenado
        if not swapped:
            break

    return a


def quicksort(lista: List[int]) -> List[int]:
    """
    Quicksort ITERATIVO (con pila) para evitar problemas de recursión en Python.
    Complejidad promedio: O(n log n). Peor caso: O(n^2).

    Justificación:
    - Python tiene límite de recursión; un quicksort recursivo puede fallar en peor caso.
    - La versión iterativa evita RecursionError y es más estable para pruebas grandes.
    - Usamos pivote aleatorio para reducir la probabilidad del peor caso.
    """
    a = lista.copy()
    if len(a) <= 1:
        return a

    # Pila de rangos (low, high)
    stack = [(0, len(a) - 1)]

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        # pivote aleatorio: reduce chance de peor caso en listas ya ordenadas/invertidas
        pivot_index = random.randint(low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]

        # partición tipo Lomuto
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        p = i + 1  # posición final del pivote

        # Empuja a la pila los sub-arreglos.
        # Tip: primero mete el más grande, así procesas antes el más pequeño (pila más chica).
        left = (low, p - 1)
        right = (p + 1, high)

        left_size = left[1] - left[0]
        right_size = right[1] - right[0]

        if left_size > right_size:
            if left[0] < left[1]:
                stack.append(left)
            if right[0] < right[1]:
                stack.append(right)
        else:
            if right[0] < right[1]:
                stack.append(right)
            if left[0] < left[1]:
                stack.append(left)

    return a
