import numpy as np

# Función para ingresar una matriz 3x3
def ingresar_matriz(nombre):
    matriz = []
    print(f"Ingresa los elementos de la matriz {nombre} (3x3):")
    for i in range(3):
        fila = []
        for j in range(3):
            elemento = float(input(f"Elemento ({i+1},{j+1}) de la matriz {nombre}: "))
            fila.append(elemento)
        matriz.append(fila)
    return np.array(matriz)

# Función para calcular la inversa de una matriz
def calcular_inversa(matriz):
    try:
        inversa = np.linalg.inv(matriz)
        return inversa
    except np.linalg.LinAlgError:
        return None

# Ingresar las matrices
matriz_a = ingresar_matriz("Robot")
matriz_b = ingresar_matriz("Entorno")

# Multiplicar las matrices
producto = np.dot(matriz_a, matriz_b)
print("El producto de las matrices Robot y Entorno es:")
print(producto)
print("Tranformación Robot-Entorno")
print("Esta nueva matriz representa la transformación lineal compuesta")



# Calcular la inversa del producto
inversa_producto = calcular_inversa(producto)

# Mostrar la inversa del producto si existe
if inversa_producto is not None:
    print("La inversa del producto de las matrices Robot y Entorno es:")
    print(inversa_producto)
    print("Tranformación Entorno-Robot")
    print("Esta nueva matriz representa la transformación lineal compuesta inversa")
    
    
    
else:
    print("El producto de las matrices no tiene inversa.")

