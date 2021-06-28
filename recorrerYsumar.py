import pandas as pd

archivo = pd.read_excel("Datos.xlsx")
data = archivo.to_dict("list")
# "list" significa que vamos a almacenar a cada columna como una lista con su contenido

print(data)

lista = [12, 45, 67, 32, 89, 73, 34, 12, 10]
sum = 0
for i in lista:
    sum += i
print(sum)
