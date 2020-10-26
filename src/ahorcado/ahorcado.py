import funciones as fn
import dibujos as db
import sources as sc

def ahorcado():
    palabra = fn.buscarpalabra(sc.palabra)
    print(palabra)
    return palabra


if __name__ == "__main__":
    ahorcado()