def atraccion():
  
    edad = int(input("Introduce tu edad: "))
    

    if edad < 10:
        print("Lo siento, no puedes ir a la atracción porque eres muy joven.")
    elif 10 <= edad <= 17:
        print("¡Puedes ir a la atracción, pero necesitas estar acompañado de un adulto.")
    else:
        print("¡Puedes ir a la atracción sin restricciones! Disfruta.")

atraccion()

