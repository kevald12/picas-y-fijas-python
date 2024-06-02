import random
#se importan random para poder generar los numeros aleatorios 

def generar_clave():
    clave = random.sample(range(10), 4)
    return clave

def validar_intento(clave, intento):
    picas = 0
    fijas = 0
    for i in range(4):
        if intento[i] in clave:
            if intento[i] == clave[i]:
                fijas += 1
            else:
                picas += 1
    return picas, fijas

def jugar():
    clave = generar_clave()
    intentos = 0
    while intentos < 12:
        intento = list(map(int, input("Introduce un número de 4 cifras: ").strip()))
        if len(intento) != 4:
            print("Debes introducir un número de 4 cifras.")
            continue
        picas, fijas = validar_intento(clave, intento)
        intentos += 1
        print(f"Intentos: {intentos} - Picas: {picas} - Fijas: {fijas}")
        if fijas == 4:
            break


    else:
        print("Mal, este juego no es para ti.")
        print(f"La clave era: {''.join(map(str, clave))}")
        return
    if fijas == 4 and intentos < 2:
        print("Excelente, eres un maestro estas fuera del alcance de los demás.")
    elif fijas == 4 and intentos < 4:
        print("Muy bueno, puedes ser un gran competidor.")
    elif fijas == 4 and intentos < 8:
        print("Bien, estas progresando debes buscar tus límites.")
    elif fijas == 4 and intentos < 10:
        print("Regular, Aún es largo el camino por recorrer.")

jugar()