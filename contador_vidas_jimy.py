def contador_vidas():
    vidas = 3
    while vidas > 0:
        yield f"Te quedan {vidas} vidas"
        vidas -= 1
    yield "Game Over"

mis_vidas = contador_vidas()

for _ in range(4):
    mensaje_actual = next(mis_vidas)
    print(mensaje_actual)


""" En este caso, la variable _ es comúnmente utilizada cuando no necesitas la variable del bucle en el cuerpo del bucle. Entonces, puedes considerar reemplazar mensaje con _ para indicar que la variable no se utiliza. """