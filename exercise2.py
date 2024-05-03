#Creamos la función comparar_cadenas_lexicograficas, que recibe dos cadenas de texto y devuelve "-1" si la primera cadena es lexicográficamente menor que la segunda, "1" si es mayor, y "0" si son iguales.

def comparar_cadenas_lexicograficas(cadena1: str, cadena2: str):
    #hacemos un condicional en donde si la primera cadena es menor a la segunda cadena, retornará un "-1"
    if cadena1 < cadena2:
        return "-1"
    #En caso contrario: si la cadena 2 resulta ser mayor que la cadena 2, retornará un "1"
    elif cadena1 > cadena2:
        return "1"
    #Si no pasa ninguno de los 2 casos, y resulta ser que ambas cadenas son iguales, retornará un "0"
    elif cadena1 == cadena2:
        return "0"

#pruebas de distintas posibilidades
print(comparar_cadenas_lexicograficas("aaa", "aaz"))
print(comparar_cadenas_lexicograficas("aaa", "aaa"))
print(comparar_cadenas_lexicograficas("aaz", "aaa"))