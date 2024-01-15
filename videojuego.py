""" def perder_vida():
    vidas = 3
    while vidas > 0:
        yield f"Te quedan {vidas} vida{'s' if vidas > 1 else ''}"
        vidas -= 1
    yield "Game Over"

# Crear el generador
perder_vida = perder_vida()

# Ejemplos de uso
for _ in range(4):
    print(next(perder_vida)) """


def perder_vida():
    vidas = 3
    while vidas > 0:
        yield f"Te quedan {vidas} vidas"
        vidas -= 1
    yield "Game Over"

# Crear el generador
perder_vida_generador = perder_vida()

# Simular el uso del generador
for mensaje in range(4):
    mensaje = next(perder_vida_generador)
    print(mensaje)
