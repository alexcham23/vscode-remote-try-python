import random


def obtener_opcion_aleatoria():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def verificar_ganador(jugador, computadora):
    reglas={
        'piedra': 'tijeras',
        'tijeras': 'papel',
        'papel': 'piedra'
    }
    
    if jugador == computadora:
        return "Empate"
    elif reglas[jugador] == computadora:
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar():
    puntaje={'ganaste':0, 'perdiste':0, 'empate':0}

    while True:
        print("Elige: piedra, papel o tijeras")
        eleccion = input("Tu eleccion: ").lower()

        if eleccion not in ["piedra", "papel", "tijeras"]:
            print("Error: por favor elige una opcion valida")
            continue

        opcion_openente = obtener_opcion_aleatoria()
        resultado = verificar_ganador(eleccion, opcion_openente)

        print(f"Tu elegiste {eleccion}, la computadora eligio {opcion_openente}")

        puntaje[resultado] += 1

        jugar_de_nuevo = input("Quieres jugar de nuevo? (s/n): ").lower()

        if jugar_de_nuevo.lower() != "s":
            break
    
    print(f"Puntaje final: Ganaste {puntaje['ganaste']} veces, Perdiste {puntaje['perdiste']} veces, Empataste {puntaje['empate']} veces")
