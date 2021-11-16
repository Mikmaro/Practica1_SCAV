# Mario Fernández
# Exercise 5

import scipy
from scipy.fftpack import fft, dct, ifft, idct
import numpy as np

'''
De primeras intenté programar a mano el algoritmo de la DCT,
utilizando una formula de las muchas que encontré en Wikipedia.
Aún así, también he implementado con la ayuda de las libererías
la dct, dónde para convertir el input usando la dct debí:
1-Utilizar la fft
2-Usar la función de dct
https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.idct.html


En cambio, para decodificar usé los pasos inversos:
1-Utilizar la ifft
2-Utilizar idct
https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.dct.html

'''


def dct_algorithm(array):  # algoritmo mío hecho "a mano"
    final = []
    for i in range(len(array)):
        X = array[i] * np.cos((np.pi / len(array)) * (i + (1 / 2)) * i)
        final.append(X)
    print(final)


if __name__ == '__main__':
    matrix = np.array([1, 2, 3, 0])

    print("El array de entrada es:", matrix)

    fft = fft(matrix).real  # paso previo que encontré que se debía hacer

    print("Ahora el array utilizando la DCT es:", dct(fft, 1))

    ifft_real = ifft(dct(fft, 1)).real  # paso previo que encontré que se debía hacer

    print("Y codificando resulta el array:", idct(ifft_real, 1) / 6)

    # dct_algorithm(matrix)

    # si se quiere se descomenta para ver lo que muestra la funcion implementada por mí
