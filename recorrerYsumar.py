import pandas as pd

archivo = pd.read_excel("Datos.xlsx")
data = archivo.to_dict("list")
# "list" significa que vamos a almacenar a cada columna como una lista con su contenido

print(data)
print(data['Nombre'])     # Accedemos a los datos de una columna
print(data['Nombre'][2])  # Accedemos al índice 2 de la columna 'Nombres'

lista = [12, 45, 67, 32, 89, 73, 34, 12, 10]
sum = 0
for i in lista:
    sum += i
print(sum)
