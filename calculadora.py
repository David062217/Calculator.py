l = 0
while l < 1:
    i = 0
    while i < 1:    
        primero = input("ingrese su primer digito ")
        try: 
            primero = int(primero)
            i += 1
        except:
            primero = "k" 
        if primero == "k":
            print("El valor ingresado no es un numero")
    j = 0
    while j < 1:        
        segundo = input("ingrese su segundo digito ")
        try: 
            segundo = int(segundo)
            j += 1
        except:
            segundo = "k" 
        if segundo == "k":
            print("El valor ingresado no es un numero") 

    k = 0
    while k < 1:
        simbolo = input("ingrese su operacion: + (suma) - (resta) * (multiplicacion) / (division) ")
        if simbolo == "+":
            print("El resultado es:",primero + segundo)
            k += 1
        elif simbolo == "-":
            print("El resultado es:",primero - segundo)
            k += 1
        elif simbolo == "*":
            print("El resultado es:",primero * segundo)
            k += 1
        elif simbolo == "/":
            print("El resultado es:",primero / segundo)  
            k += 1  
        else:
            print("El simbolo ingresado no es valido, por favor ingrese algun simbolo de los anteriores")

    m = 0
    while m < 1:
        again = input("¿Desea hacer otra operacion? s (si) n (no) ")
        if again == "n":
            print("Hasta luego")
            l += 1
            m += 1
        elif again == "s":
            print("Bienvenido")
            m += 1
        else:
            print("El digito es invalido")