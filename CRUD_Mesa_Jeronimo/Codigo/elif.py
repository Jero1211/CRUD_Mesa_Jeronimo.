while True:
    # Solicitar la edad al usuario
    edad_input = input("Por favor, ingresa tu edad (o escribe 'salir' para terminar): ")
    
    # Opción para salir del bucle
    if edad_input.lower() == 'salir':
        print("Programa terminado.")
        break
    
    try:
        # Convertir la entrada a un número entero
        edad = int(edad_input)

        # Determinar la categoría según la edad
        if edad < 18:
            print("Eres menor de edad.")
        elif 18 <= edad < 65:
            print("Eres adulto.")
        else:
            print("Eres de la tercera edad.")
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")
        