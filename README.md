### Examen parcial de Python


### Funcionalidades Principales:

# 1. Ejercicio de algoritmia (3)
  (Ordenar algo lexicográficamente significa organizar elementos alfabéticamente, de la misma forma que se listan las palabras en un diccionario)

# Especificaciones de la Función:
## Nombre de la función:
● El nombre de la función debe ser: comparar_cadenas_lexicograficas

## Parámetros:
- cadena1 (str): La primera cadena a comparar.
- cadena2 (str): La segunda cadena a comparar.

## Retorno:
- Si la primera cadena es menor que la segunda, retornar "-1".

- Si la segunda cadena es menor que la primera, retornar "1".

- Si las cadenas son iguales, retornar "0".
Ejemplo

- Si tenemos las cadenas "abc" y "abd", al compararlas lexicográficamente, la
cadena "abc" sería considerada menor que "abd", ya que en la tercera posición
la letra "c" tiene un valor ASCII menor que "d".

# Ejecucion:

```
py exercise2.py
```

--- 
# 2. Ejercicio de Pandas (2.5)

Se proporcionará una lista de ventas mensuales y su tarea es realizar análisis básico sobre estas ventas.
```
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
```

- 1. Agrupa los datos por trimestre y calcula el total de ventas para cada trimestre.
- 2. Filtrar y mostrar solo los meses donde las ventas superen 20000.
- 3. Encontrar el mes con el mayor volumen de ventas y mostrar esta información.
- 4. Calcular el promedio de ventas mensuales y mostrar esta información.
- 5. Crea un DataFrame que incluya dos columnas una para los meses y otra para el total de ventas de cada mes.

# Ejecucion:

```
py exercise2.py
```

---

# 3. Ejercicios de Graficos (2,5)
- Basándote en el DataFrame creado, realiza un análisis de gráficos para visualizar la tendencia de ventas a lo largo de los meses. Utiliza un gráfico de líneas donde el eje x represente los meses y el eje y represente el total de ventas de cada mes.

# Ejecucion:

```
py exercise3.py
```

# IMPORTANTE 

1. Para inicalizar los ejercicios, deberá de inicializar un entorno virtual, utilizando una herramaienta llamada virtualenv, en donde despues de crear su entorno, deberá de instalar las librerias correspondientes:

```
pip install pandas
```
```
pip install matplotlib
```
2. Una vez hecho eso, asegurese de que sus dependencias hayan sido creadas correctamente.
3. Ejecute los archivos para obtener el resultado final. 