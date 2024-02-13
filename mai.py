while True:
    import random

    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contraseña = ""
    longitud  = int(input("¿Que tan larga quieres la contraseña?: "))

    for i in range(longitud):
        a = random.choice(caracteres)
        contraseña += a
    print("Tu contraseña es: ", contraseña)




    


