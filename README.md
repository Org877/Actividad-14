# Actividad-14
# Multiplicación de Enteros Gigantes mediante Algoritmo de Karatsuba (Divide y Vencerás)

Implementación en Python del **Algoritmo de Karatsuba** basada en la estrategia de diseño de algoritmos **Divide y Vencerás**, desarrollada como práctica de análisis de complejidad algorítmica.

##  Descripción del Proyecto
El algoritmo de Karatsuba reduce la complejidad temporal de la multiplicación tradicional de enteros de $O(N^2)$ a aproximadamente $O(N^{\log_2 3}) \approx O(N^{1.585})$, logrando esto mediante la descomposición del problema en tres fases principales:

1. **División:** Partición de los números de $N$ dígitos en mitades superiores e inferiores ($X_1, X_0$ y $Y_1, Y_0$).
2. **Conquista:** Cálculo recursivo de solo 3 productos parciales en lugar de los 4 tradicionales ($z_2, z_0, z_1$).
3. **Integración:** Combinación de los resultados parciales mediante potencias de base 10.

---

##  Análisis de Complejidad

### Complejidad Temporal ($T(N)$)
* **Multiplicación Tradicional (Escolar):** $T(N) = 4T(N/2) + O(N) \implies O(N^2)$
* **Algoritmo de Karatsuba:** $T(N) = 3T(N/2) + O(N) \implies O(N^{\log_2 3}) \approx O(N^{1.585})$

### Complejidad Espacial ($S(N)$)
* El espacio está dominado por la profundidad de la pila de llamadas recursivas y la manipulación de cadenas/enteros, resultando en una complejidad de $O(N \log N)$ (o $O(N)$ optimizado).

---

##  Instrucciones de Ejecución

### Pruebas Unitarias
Para validar el correcto funcionamiento con números de 20, 50 y 100 dígitos:

