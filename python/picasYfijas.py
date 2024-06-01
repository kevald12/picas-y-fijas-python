import random

def picas_y_fijas():
    clave = 0
    intentos = 0 
    numero = 0 
    fijas = 0
    picas = 0
    max_intentos = 12
    min_cifra = 1
    max_cifra = 9

    mensaje = "Ingrese el número secreto (4 cifras sin repetir): "
    numero = int(input(mensaje))

    while True:
        if len(set(str(numero))) != 4:
            mensaje ="El número ingresado no tiene 4 cifras unicas, intenta de nuevo"
            print (mensaje)
            continue
        break

    clave = random.randint(1000, 10000)
    mensaje = "Intenta adivinar el número secreto"
    print(mensaje)

    while intentos < max_intentos:
        mensaje = "Ingrese su intento:  "
        intento = int(input(mensaje))
        picas = 0
        fijas = 0

        for i in range(4):
            cifra = clave % 10
            posicion = i % 4

            if cifra == intento % 10:
                if posicion == 0:
                    fijas += 1
                elif posicion == 1:
                    fijas += 1
                elif posicion == 2:
                    picas += 1
                elif posicion == 3:
                    fijas += 1

            clave = clave // 10

        mensaje = "Picas: " + str(picas) + " - Fijas: " + str(fijas) + "\n"
        print(mensaje)

        if picas == 4:
            mensaje = "¡Felicidades! Adivinó el número secreto en " + str(intentos) + " intentos."
            print(mensaje)
            break
        elif intentos == max_intentos - 1:
            mensaje = "Se acabaron los intentos. El número secreto era " + str(clave) + "."
            print(mensaje)

    print('Presione "Enter" para jugar de nuevo, "Esc" para salir.')
    input()

if __name__ == "__main__":
    picas_y_fijas()