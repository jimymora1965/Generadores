# Definir una función generadora llamada perder_vida
def perder_vida():
    # Inicializar la variable vidas con el valor 3
    vidas = 3
    
    # Iniciar un bucle while que se ejecutará mientras vidas sea mayor que 0
    while vidas > 0:
        # Utilizar la declaración yield para devolver un mensaje indicando cuántas vidas quedan
        yield f"Te quedan {vidas} vidas"
        
        # Decrementar el valor de vidas en 1 en cada iteración del bucle
        vidas -= 1
    
    # Cuando el bucle while termine (cuando vidas sea igual a 0), utilizar yield para devolver "Game Over"
    yield "Game Over"

# Crear una instancia del generador y almacenarla en la variable perder_vida_generador
perder_vida_generador = perder_vida()

# Utilizar un bucle for para simular el uso del generador
for _ in range(4):
    # Llamar a next en el generador para obtener el siguiente mensaje y almacenarlo en la variable mensaje
    mensaje = next(perder_vida_generador)
    
    # Imprimir el mensaje en la consola
    print(mensaje)
