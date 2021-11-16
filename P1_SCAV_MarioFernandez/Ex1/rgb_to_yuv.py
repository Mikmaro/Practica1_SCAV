# Mario Fernández
# Exercise 1

# Si se quieren modificar los valores, más abajo en el main se pueden cambiar

def RGB_TO_YUV(R, G, B):
    # Implementar las líneas que están presentes en la teoría (diapo 46)
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    U = -0.148 * R - 0.291 * G + 0.439 * B + 128
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128

    print("THE RGB VALUES", R, ",", G, "AND", B, "IN YUV ARE:", Y, ",", U, "AND", V)


def YUV_TO_RGB(Y, U, V):
    # Implementar las líneas que están presentes en la teoría (diapo 46)
    R = 1.164 * (Y - 16) + 1.596 * (V - 128)
    G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128)
    B = 1.164 * (Y - 16) + 2.018 * (U - 128)
    print("THE YUV VALUES", Y, ",", U, "AND", V, "IN RGB ARE:", R, ",", G, "AND", B)


if __name__ == '__main__':
    RGB_TO_YUV(10, 10, 10)  # aquí se pueden modificar los valores
    YUV_TO_RGB(100, 100, 100)  # aquí se pueden modificar los valores
