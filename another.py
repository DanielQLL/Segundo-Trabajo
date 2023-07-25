import matplotlib.image as img
import matplotlib.pyplot as plt

def get_closest_node(no_visitados, distancia_corta):
    nod_no_visitado = None
    dist_corta = float('inf')
    for node in no_visitados:
        if distancia_corta[node] < dist_corta:
            nod_no_visitado = node
            dist_corta = distancia_corta[node]
    return nod_no_visitado

def dijkstra(grafo, inicio, fin):
    camino_corto = {node: None for node in grafo}
    camino_corto[inicio] = [inicio]

    distancia_corta = {node: float('inf') for node in grafo}
    distancia_corta[inicio] = 0

    nod_no_visitados = list(grafo)

    while nod_no_visitados:
        # Encontrar el nodo no visitado con la distancia más corta.
        nod_actual = get_closest_node(nod_no_visitados, distancia_corta)

        for nod_vecinos in grafo[nod_actual]:
            # Calcular 
            distancia = distancia_corta[nod_actual] + grafo[nod_actual][nod_vecinos]

            # Actualizar
            if distancia < distancia_corta[nod_vecinos]:
                distancia_corta[nod_vecinos] = distancia
                camino_corto[nod_vecinos] = camino_corto[nod_actual] + [nod_vecinos]

        # Marcar
        nod_no_visitados = [node for node in nod_no_visitados if node != nod_actual]

    return camino_corto[fin]

def ubicar_puntos(lista):
    valores_x = []
    valores_y = []
    transf_punt = {
        'A': [3177, 39],
        'B': [3187, 585],
        'C': [3191, 938],
        'D': [3210, 1231],
        'E': [2448, 71],
        'F': [2463, 600],
        'G': [2474, 962],
        'H': [2489, 1240],
        'I': [1903, 187],
        'J': [1918, 613],
        'K': [1930, 966],
        'L': [1950, 1261],
        'M': [1679, 1282],
        'N': [749, 788],
        'O': [887, 942],
        'P': [1040, 979],
        'Q': [1353, 1298],
        'R': [84, 754],
        'S': [366, 999],
        'T': [665, 1237],
        'U': [1087, 1595],
        'V': [205, 1192],
        'W': [504, 1427],
        'X': [865, 1885],
        'Y': [47, 1385],
        'Z': [86, 1923],
        'A1': [339, 1636],
        'B1': [434, 1527],
        'C1': [1968, 1548],
        'D1': [2262, 1796]
    }

    for i in lista:
        if i in transf_punt:
            valores_x.append(transf_punt[i][0])
            valores_y.append(transf_punt[i][1])
    return valores_x,valores_y


dict_auto = {
    'A': {'E': 110.98},
    'B': {'A': 78.74, 'F': 106.63},
    'C': {'B': 51.55},
    'D': {'C': 45.16},
    'E': {'I': 78.09, 'F':76.14},
    'F': {'E': 76.14, 'G': 53.54, 'J': 78.34},
    'G': {'F': 53.54, 'H': 41.87, 'C': 107.41},
    'H': {'G': 41.87, 'D': 110.55, 'D1': 96.13},
    'I': {'N': 191.97, 'J': 61.05},
    'J': {'I': 61.05, 'P': 144, 'K': 51.3},
    'K': {'J': 51.3, 'L': 45.14, 'G': 80.19},
    'L': {'K': 45.14, 'H': 78.84, 'C1': 41.66},
    'M': {'L': 42.37, 'C1': 58.62},
    'N': {'O': 29.21},
    'O': {'P': 23.45, 'T': 55},
    'P': {'K': 130.47, 'Q': 65.21, 'O': 23.45},
    'Q': {'M': 45.38},
    'R': {'S': 50.48, 'N': 98.89},
    'S': {'R': 50.48, 'T': 55.51, 'V': 37.71},
    'T': {'S': 55.51, 'O': 51.33, 'U': 79.84, 'W':36.22},
    'U': {'T': 79.84, 'Q': 58.81},
    'V': {'S': 37.71, 'W': 55.61, 'Y':38.41},
    'W': {'T': 36.22, 'V': 55.61, 'B1': 18.48},
    'X': {'U': 52.53, 'B1': 78.11},
    'Y': {'V': 38.41, 'A1': 56.18},
    'Z': {'A1': 54.23},
    'A1': {'B1': 21.85, 'Y': 56.18, 'Z': 54.23},
    'B1': {'A1': 21.85, 'W': 18.48, 'X': 78.11},
    'C1': {'L': 41.66, 'D1': 62.42},
    'D1': {'H': 96.13},
}
dict_peaton = {
    'A': {'E': 110.98, 'B': 78.74},
    'B': {'A': 78.74, 'F': 106.63, 'C':51.55},
    'C': {'B': 51.55, 'D': 45.16, 'G':107.41},
    'D': {'C': 45.16, 'H': 110.55},
    'E': {'I': 78.09, 'F':76.14,'A': 110.98},
    'F': {'E': 76.14, 'G': 53.54, 'J': 78.34, 'B': 106.63},
    'G': {'F': 53.54, 'H': 41.87, 'C': 107.41, 'K': 80.19},
    'H': {'G': 41.87, 'D': 110.55, 'D1': 96.13, 'L': 78.84},
    'I': {'E': 78.09, 'J': 61.05, 'N': 191.97},
    'J': {'F': 78.34, 'I': 61.05, 'K': 51.3, 'P': 144},
    'K': {'J': 51.3, 'L': 45.14, 'G': 80.19, 'P': 130.47},
    'L': {'K': 45.14, 'H': 78.84, 'C1': 41.66, 'M': 42.37},
    'M': {'L': 42.37, 'C1': 58.62, 'Q': 45.38},
    'N': {'O': 29.21, 'I': 191.97, 'R': 98.89},
    'O': {'P': 23.45, 'T': 55, 'N': 29.21},
    'P': {'K': 130.47, 'Q': 65.21, 'O': 23.45, 'J': 144},
    'Q': {'M': 45.38, 'P': 65.21, 'U': 58.81},
    'R': {'S': 50.48, 'N': 98.89},
    'S': {'R': 50.48, 'T': 55.51, 'V': 37.71},
    'T': {'S': 55.51, 'O': 51.33, 'U': 79.84, 'W':36.22},
    'U': {'T': 79.84, 'Q': 58.81, 'X': 52.53},
    'V': {'S': 37.71, 'W': 55.61, 'Y':38.41},
    'W': {'T': 36.22, 'V': 55.61, 'B1': 18.48},
    'X': {'U': 52.53, 'B1': 78.11},
    'Y': {'V': 38.41, 'A1': 56.18},
    'Z': {'A1': 54.23},
    'A1': {'B1': 21.85, 'Y': 56.18, 'Z': 54.23},
    'B1': {'A1': 21.85, 'W': 18.48, 'X': 78.11},
    'C1': {'L': 41.66, 'D1': 62.42, 'M': 58.62},
    'D1': {'C1': 62.42, 'H': 96.13},
}

inicio = 'I'
fin = 'E'
print("Escoja como se tranportara: ")
print("1. Auto")
print("2. Pie")
a=int(input())
if a==1:
    camino_corto = dijkstra(dict_auto, inicio, fin)
elif a==2:
    camino_corto = dijkstra(dict_peaton,inicio,fin)

print(f"Camino más corto desde {inicio} hasta {fin}: {camino_corto}")
lis_x , lis_y=ubicar_puntos(camino_corto)
fig, ax = plt.subplots()
imagen= img.imread("mapa_page-0001.jpg")
plt.axis('off')
plt.imshow(imagen)
ax.plot(lis_x,lis_y, marker="o")
plt.show()
