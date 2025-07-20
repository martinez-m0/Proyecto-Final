import random
import os

# Función para leer palabras de archivo
def cargar_palabras(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return [linea.strip().upper() for linea in f.readlines() if linea.strip()]

# Configuraciones por dificultad
config = {
    "facil": {"archivo": "facil.txt", "intentos_max": 8},
    "media": {"archivo": "media.txt", "intentos_max": 6},
    "dificil": {"archivo": "dificil.txt", "intentos_max": 4},
    "naruto": {"archivo": "naruto.txt", "intentos_max": 6},
    "pokemon": {"archivo": "pokemon.txt", "intentos_max": 6},
    "tildes": {"archivo": "tildes.txt", "intentos_max": 6},
    "animales":{"archivo": "animales.txt", "intentos_max": 6}
}

# Elegir dificultad
while True:
    dificultad = input("Elige la dificultad (facil/media/dificil/naruto/pokemon/animales/tildes): ").lower()
    if dificultad in config:
        break
    print("Opción no válida. Intenta de nuevo.")

#  Construir ruta completa para buscar siempre en la carpeta correcta
ruta_base = os.path.dirname(__file__)
archivo_palabras = os.path.join(ruta_base, config[dificultad]["archivo"])
palabras = cargar_palabras(archivo_palabras)

palabra = list(random.choice(palabras))
intentos_max = config[dificultad]["intentos_max"]

# Muñeco y base 
ahorcado = [
    "              !==============N",
    "              O              N",
    "            / | \\            N",
    "            \\ | /            N",
    "             / \\             N",
    "            /   \\            N",
    "           _\\   /_           N",
    "_____________________________N"
]

estructura_base = [
    "              !==============N",
    "                             N",
    "                             N",
    "                             N",
    "                             N",
    "                             N",
    "                             N",
    "_____________________________N"
]

# Inicialización del juego
letras_todas = []
fallos = 0
resultado = ["_" for _ in palabra]

# Bucle principal
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("**********  Juego del ahorcado  **********")
    print("hecho por: Samuel Gutierres, Miguel Martinez")
    print("Estás jugando en modo:", dificultad.capitalize(), "- Te quedan", intentos_max - fallos, "intentos")
    print("Grupo: Master chill")

    for i in range(fallos):
        print(ahorcado[i])
    for i in range(len(estructura_base) - fallos):
        print(estructura_base[i + fallos])

    print("\n     ", end=" ")
    for letra in resultado:
        print(letra, end=" ")
    print("\n")

    if resultado == palabra:
        print("***** HAS GANADO GG *****")
        break

    if fallos >= intentos_max:
        print("la palabra era: ", "".join(palabra))
        print("***** HAS PERDIDO POR BOT *****")
        break

    while True:
        letra_usuario = input("Dime una letra: ").upper()
        if len(letra_usuario) != 1:
            print("Introduce solo una letra")
        elif letra_usuario in letras_todas:
            print("Esa letra ya la dijiste, cambia")
        elif letra_usuario not in "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ":
            print("Introduce una letra válida")
        else:
            letras_todas.append(letra_usuario)
            break

    if letra_usuario in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra_usuario:
                resultado[i] = letra_usuario
    else:
        fallos += 1
