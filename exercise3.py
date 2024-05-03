#Importacion de la libreria "pandas", para el manejo de los datos.
import pandas as pd

#Copiamos los datos
ventas_mensuales = [
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},
{"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
{"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
{"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
{"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
{"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]

#Definimos "df", que será la tabla donde tendremos nuestros datos. y le pasamos como columnas los datos "mes", "total_ventas" y "año"
df = pd.DataFrame(ventas_mensuales, columns=["mes", "total_ventas", "año"])

#Sacamos el total de ventas por cada trimestre
df["Suma"] = df["total_ventas"].cumsum()


#Hacemos la función para mostrar el total de las ventas trimestrales. Lo que hacemos en este ecaso es definif ua variable en donde estoy llamando a la columna "Suma", la cual previamente habia definido como la suma total de todas las ventas. Con ello, lo que hagoes llamar a a los valores del arreglo correpondientes, dado que el arreglo comienza desde la posición 0, decido llamar a las posiciones 3, 7 ,11, 15, 20 y 23, que representan el ultimo mes de cada cuatrimestre
def venta_trimestral():
    suma = df["Suma"]
    print("--------------------------------------------------------")
    print(f'Total del primer trimestre: {suma[3]}$  (Abril 2023)')
    print(f'Total del segundo trimestre: {suma[7]}$ (Agosto 2023)')
    print(f'Total del tercer trimestre: {suma[11]}$ (Diciembre 2023)')
    print("--------------------------------------------------------")
    print(f'Total del cuarto trimestre: {suma[15]}$ (Abril 2024)')
    print(f'Total del quinto trimestre: {suma[20]}$ (Agosto 2024)')
    print(f'Total del sexto trimestre: {suma[23]}$ (Diciembre 2024)')
    print("--------------------------------------------------------")


# Hacemos la función para obtener los valores de las ventas mayores a $20.000: primero obtenemos mes y ventas de las columnas del DataFrame. Con estos elementos, utilizamos un for i con el rango de las ventas, en donde a cada venta (ventas[i]), dentro del mismo for utilizamos un condicional en donde preguntamos si cada venta es mayor a 20.000 (Es importante destacar el hecho de que si no re definimos el tipo de valor de ventas, no lo tomará comoun numero). Una vez cumplida esa condición, la función mostrará las ventas mayores a 20.000.

#Destaco el hecho de que, al ser de la misma columna, no hace falta hacer un fo apra meses, bastaría con pasarle el [i], para que se entienda que se esta hablando de la misma información. 
def ventas_mayores_20():
    ventas = df["total_ventas"]
    mes = df["mes"]

    print("Meses que producieron más de 20.000 ventas:")
    for i in range(len(ventas)):
        int(ventas[i])
        if ventas[i] > 20000:
            print(f'{mes[i]}: ${ventas[i]}')
            
            
#Para obtener la mayor venta del mes, utilizamos un metodo max(), en la columna del total de ventas, esto automaticamente dectectará el valor mas grande que se halle dentro de la columna.
#Posteriormente mostramos los datos.
def mayor_mes_venta():
    año = df["año"]
    mes = df["mes"]
    ventas = df["total_ventas"].max()    
    print(f'La mayor venta fue de: ${ventas}, en el {mes[23]}, del {año[23]}')
            
#Para sacar el promedio de ventas, utilizamos el metodo cumsum(), para obtener el total de todos los ingresos, para despues dividirlo por la cantidad de meses. Llamamos el ultimo valor de "promedio" y lo dividimos por 24.
def promedio_ventas():
    promedio = df["total_ventas"].cumsum() 
    print(f'El promedio es de de ventas mensuales es de: $ {(promedio[23] / 24).round(2)}')

#Creamos el dataframe con las 2 columnas requeridas.
def crear_dataframe():
    dataFrame = pd.DataFrame(ventas_mensuales, columns=["mes", "total_ventas"]) 
    print(dataFrame)

#venta_trimestral()            
#ventas_mayores_20()
#mayor_mes_venta()
#promedio_ventas()
crear_dataframe()