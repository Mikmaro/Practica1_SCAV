# Mario Fernández
# Exercise 4

# Investigando un poco por la red buscando inspiración encontré un código interesante en ...
# ... py4u.net/discuss/265519, así que retocandolo un poco encontramos el siguiente algoritmo

# Si se quiere editar la lista (data), se puede modificar más abajo, introduciendo los números ...
# ... que se deseen

def run_length_alorithm(data):
    data_final = []  # lista vacía que se irá llenando para el output
    repeated = 1  # se inicializa, si repeated es mayor que 1 significa que el "0" está repetido más de una vez

    # Primero analizamos si el input es un solo numero, y si este es un 0
    if len(data) == 1 and data[0] == 0:
        data_final.append((data[0], repeated))
        print("The bytes are:", data)
        print("The encoded bytes are:", data_final)

    # En caso que el input sea un número y que este número no sea un 0
    elif len(data) == 1 and data[0] != 0:
        print("The bytes are:", data)
        print("The encoded bytes are:", data)

    else:
        for i in range(1, len(data)):
            if data[i] == data[i - 1] and data[i] == 0:
                repeated += 1
                # esto significará que hay más de un cero seguido,
                # por lo que se incrementa este contador
            else:
                if repeated == 1 and data[i - 1] != 0:
                    data_final.append(data[i - 1])
                    # si no hay repetición de numeros y el numero anterior no es un
                    # cero, se añaden estos numeros a la lista data_final
                else:
                    data_final.append((data[i - 1], repeated))
                    # si un cero ha sido repetido una o
                    # varias veces, se añade a la
                    # lista el número "0" y las veces que ha sido repetido consecutivamente
                    repeated = 1  # se resetea a 1 el contador de repeticiones de un número
        if repeated != 1 and data[i] == 0:
            data_final.append((data[i], repeated))
            # esto es cuando haya alguna repetición
            # de cero (al final del array),
            # mostrar el número "0" y las veces
            # que esten repetidos consecutivamente
        elif repeated == 1 and data[-1] == 0:
            # una pequeña comprobación de si el último numero es un "0" y no hay
            # ningun número más
            data_final.append((data[i], repeated))
        else:
            data_final.append((data[i]))
            # por lo que si el número no es "0",
            # añadimos estos numeros tal cual a la lista data_final

        print("The bytes are:", data)
        print("The encoded bytes are:", data_final)


if __name__ == '__main__':
    data = [0, 1, 0, 0, 1, 1, 2, 0]
    run_length_alorithm(data)
