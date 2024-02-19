import random

def tirar_dado():
    """Simula tirar un dado de 6 caras."""
    return random.randint(1, 6)

def jugar():
    """Simula un juego entre Álvaro y Bárbara."""
    alvaro = tirar_dado()
    barbara = tirar_dado()

    print(f'Álvaro tiró un {alvaro}')
    print(f'Bárbara tiró un {barbara}')

    if alvaro > barbara:
        print('Álvaro gana!')
    elif alvaro < barbara:
        print('Bárbara gana!')
    else:
        print('¡Empate!')

if __name__ == "__main__":
    print("Bienvenido al juego de dados entre Álvaro y Bárbara.")
    jugar()