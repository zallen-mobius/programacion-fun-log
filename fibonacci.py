#--- Programación lógica y funcional ---
#-   López-Medina                      -
#-   Tarea                             -

def obtener_n():
    '''Funcion que pide al usuario ingresar un número n.'''
    n = int(input("Introduzca que número fibonnaci desea: "))
    return n

def iniciar_fib():
    '''Funcion que crea el string donde se almacenara una secuencia de fibonacci.'''
    cad = ""
    return cad

def fibonacci(n, fib):
    '''Funcion que ejecuta el algoritmo para crear una secuencia fibonacci hasta un 'n' dado.'''
    for z in range(0, n+1):
        if (z==0):
            fib = fib+"0"
        elif (z==1):
            fib = fib+"1"
        else:
            fib = fib+", "+str(int(fib[-1])+int(fib[-2]))
    return fib

def imprimir(imp, num):
    '''Funcion que imprime el resultado correspondiente a un numero dado.'''
    print("Fibonacci hasta "+str(num)+":")
    print(imp)
    return 0

numero = obtener_n()
imprimir(fibonnaci(numero,iniciar_fib), numero)
