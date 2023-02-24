while True:
    try:
        x = int(input("introdusca un numero: "))
        
    except ValueError:
        print("¡Ups! Ese no era un número válido. Intentar otra vez...")
        
    else:
        print(x)