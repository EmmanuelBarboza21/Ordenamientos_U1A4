# src/benchmark.py
from __future__ import annotations
import timeit
import random
import statistics
import csv
from typing import Callable, List, Dict, Any

from sorting import bubble_sort, quicksort


def generar_lista_aleatoria(n: int, seed: int) -> List[int]:
    rng = random.Random(seed)
    return [rng.randint(0, 1_000_000) for _ in range(n)]


def generar_lista_invertida(n: int) -> List[int]:
    # lista invertida: peor escenario típico para bubble
    return list(range(n, 0, -1))


def generar_lista_casi_ordenada(n: int, seed: int, swaps: int = 10) -> List[int]:
    # lista casi ordenada: empieza ordenada y hacemos pocos swaps
    rng = random.Random(seed)
    a = list(range(n))
    for _ in range(swaps):
        i = rng.randrange(n)
        j = rng.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a


def medir_tiempo(algoritmo: Callable[[List[int]], List[int]], data: List[int], repeticiones: int) -> Dict[str, float]:
    # OJO: dentro del timeit llamamos una función que copia la lista internamente
    # para que cada corrida ordene el MISMO desorden inicial.
    tiempos = timeit.repeat(
        stmt=lambda: algoritmo(data),
        repeat=repeticiones,
        number=1
    )
    promedio = statistics.mean(tiempos)
    desv = statistics.pstdev(tiempos)  # desviación estándar poblacional
    return {"avg": promedio, "std": desv}


def imprimir_tabla(filas: List[Dict[str, Any]]) -> None:
    # tabla sencilla por consola (sin librerías)
    headers = ["tamaño", "escenario", "algoritmo", "repeticiones", "promedio_s", "std_s"]
    widths = {h: len(h) for h in headers}

    for f in filas:
        widths["tamaño"] = max(widths["tamaño"], len(str(f["size"])))
        widths["escenario"] = max(widths["escenario"], len(f["scenario"]))
        widths["algoritmo"] = max(widths["algoritmo"], len(f["algorithm"]))
        widths["repeticiones"] = max(widths["repeticiones"], len(str(f["reps"])))
        widths["promedio_s"] = max(widths["promedio_s"], len(f"{f['avg']:.6f}"))
        widths["std_s"] = max(widths["std_s"], len(f"{f['std']:.6f}"))

    def row(values: Dict[str, str]) -> str:
        return " | ".join(values[h].ljust(widths[h]) for h in headers)

    print(row({h: h for h in headers}))
    print("-" * (sum(widths.values()) + 3 * (len(headers) - 1)))

    for f in filas:
        print(row({
            "tamaño": str(f["size"]),
            "escenario": f["scenario"],
            "algoritmo": f["algorithm"],
            "repeticiones": str(f["reps"]),
            "promedio_s": f"{f['avg']:.6f}",
            "std_s": f"{f['std']:.6f}",
        }))


def guardar_csv(filas: List[Dict[str, Any]], ruta: str) -> None:
    headers = ["size", "scenario", "algorithm", "reps", "avg_seconds", "std_seconds"]
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in filas:
            writer.writerow({
                "size": r["size"],
                "scenario": r["scenario"],
                "algorithm": r["algorithm"],
                "reps": r["reps"],
                "avg_seconds": r["avg"],
                "std_seconds": r["std"],
            })


def main() -> None:
    tamanos = [100, 1000, 5000, 10000]
    repeticiones = 5  # mínimo 5 como pide la práctica

    algoritmos = [
        ("bubble_sort", bubble_sort),
        ("quicksort", quicksort),
    ]

    filas: List[Dict[str, Any]] = []

    # Para reproducibilidad: mismas listas por tamaño/escenario
    for n in tamanos:
        # Escenario 1: aleatoria
        data_random = generar_lista_aleatoria(n, seed=12345 + n)

        # Escenario 2: invertida (puedes cambiar a casi ordenada si tu profe lo pide)
        data_reversed = generar_lista_invertida(n)

        escenarios = [
            ("aleatoria", data_random),
            ("invertida", data_reversed),
            # Alternativa: ("casi_ordenada", generar_lista_casi_ordenada(n, seed=999 + n, swaps= max(10, n//1000)))
        ]

        for escenario_nombre, data in escenarios:
            for alg_name, alg_fn in algoritmos:
                med = medir_tiempo(alg_fn, data, repeticiones)
                filas.append({
                    "size": n,
                    "scenario": escenario_nombre,
                    "algorithm": alg_name,
                    "reps": repeticiones,
                    "avg": med["avg"],
                    "std": med["std"],
                })

    imprimir_tabla(filas)
    guardar_csv(filas, "results/benchmark_results.csv")
    print("\nListo: resultados guardados en results/benchmark_results.csv")


if __name__ == "__main__":
    main()
