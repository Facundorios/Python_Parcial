#Importacion de la libreria de matplotlib, para el creación de graficos.
import matplotlib.pyplot as plt

#Importamos desde el archivo anterior el df, que vendria siendo el dataFrame
from exercise3 import df

#Definimos los esjes correspondientes. X son los meses e Y son el total de ventas. 
x = df["mes"]
y = df["total_ventas"]

plt.title("Nivel de ventas a lo largo del 2023 y 2024")
plt.plot(x,y)
plt.show()