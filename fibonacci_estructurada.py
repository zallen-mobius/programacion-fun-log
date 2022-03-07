#-- Programación lógica y funcional --
#-  López-Medina                     -
#-  Tarea                            -

n = int(input("Introduzca que número fibonnaci desea: "))
fib = ""

for z in range(0, n+1):
    if (z==0):
        fib = fib+"0"
    elif (z==1):
        fib = fib+"1"
    else:
        fib = fib+str(int(fib[-1])+int(fib[-2]))

print("Fibonacci hasta "+str(n)+":")
print(fib)