import time
import random
import sys

# Aumentar el límite de recursión y conversión de enteros largos en Python si es necesario
sys.setrecursionlimit(2000)

def karatsuba(x: int, y: int) -> int:
    
   # Implementación recursiva del algoritmo de Karatsuba.
    # fases: División, Conquista e Integración.
    
    # Caso base: números de un solo dígito
    if x < 10 or y < 10:
        return x * y

    # Determinar el tamaño de los números
    str_x, str_y = str(x), str(y)
    n = max(len(str_x), len(str_y))
    m = n // 2

    # 1. DIVISIÓN
    # Dividir x e y en partes altas (X1, Y1) y bajas (X0, Y0)
    power_ten = 10**m
    x1, x0 = divmod(x, power_ten)
    y1, y0 = divmod(y, power_ten)

    # 2. CONQUISTA (3 llamadas recursivas en lugar de 4)
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0

    # 3. INTEGRACIÓN
    return (z2 * (10**(2 * m))) + (z1 * power_ten) + z0


def benchmark_multiplication(num_digits: int):
    # Genera dos números aleatorios de `num_digits` dígitos y mide el tiempo
    # y correctitud de Karatsuba frente a la multiplicación nativa.
    
    # Generar enteros gigantes
    lower_bound = 10**(num_digits - 1)
    upper_bound = (10**num_digits) - 1
    x = random.randint(lower_bound, upper_bound)
    y = random.randint(lower_bound, upper_bound)

    # 1. Medir Karatsuba
    start_time = time.perf_counter()
    res_karatsuba = karatsuba(x, y)
    time_karatsuba = time.perf_counter() - start_time

    # 2. Medir Multiplicación Nativa
    start_time = time.perf_counter()
    res_native = x * y
    time_native = time.perf_counter() - start_time

    # Validar que los resultados coinciden
    assert res_karatsuba == res_native, f"Error de cálculo para {num_digits} dígitos!"

    print(f"--- Pruebas para {num_digits} Dígitos ---")
    print(f"Resultado correcto: Sí (Verificado)")
    print(f"Tiempo Karatsuba : {time_karatsuba:.6f} segundos")
    print(f"Tiempo Nativo    : {time_native:.6f} segundos\n")


if __name__ == "__main__":
    print("Iniciando pruebas del Algoritmo de Karatsuba \n")
    for digits in [20, 50, 100, 500, 1000]:
        benchmark_multiplication(digits)