"""1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
ingresado por parámetro."""
def esprimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True
def mostrarprimos(n):
    primos = []
    for nume in range(1, n+1):
        if esprimo(nume):
            primos.append(nume)
    return primos
numeroingresado = int(input("Ingrese un número: "))
devuelveprimos = mostrarprimos(numeroingresado)
print("Números primos hasta", numeroingresado, ":")
print(devuelveprimos)

"""2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich,
hasta que el usuario ingrese 'salir'. 
Cada vez que se ingrese un condimento, muestre un mensaje avisando que ya se agregó el condimento al sándwich."""
 #test condicional en el ciclo while para detener la ejecución.
def armarsandwich():
    condimentos = []
    sucondimento = input("Ingrese un condimento para el sándwich o 'salir' para terminar: ")
    while sucondimento != 'salir':
        condimentos.append(sucondimento)
        print("se agrego el condimento", sucondimento, "al sándwich.")
        sucondimento = input("Ingrese otro condimento o 'salir' para terminar: ")
    return condimentos
sandwich = armarsandwich()
print("Los condimentos del sándwich son:",sandwich)

# Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 
def armarsandwich():
    condimentos = []
    condimento = input("Ingrese un condimento para el sándwich o 'salir' para terminar: ")
    while True:
        if condimento == 'salir':
            break
        else:
            condimentos.append(condimento)
            print("Se agrego el condimento", condimento, "al sándwich.")
            condimento = input("Ingrese otro condimento o 'salir' para terminar: ")
    return condimentos
sandwich = armarsandwich()
print("Los condimentos del sándwich son:",sandwich)

"""3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
usando argumentos por posición."""
def hacer_remera(tamaño, mensaje):
    print("su remera es de tamaño", tamaño)
    print("El mensaje impreso en la remera es:", mensaje)
hacer_remera("s", "Trust the Process")
 #Llámela una segunda vez usando argumentos por clave. 
hacer_remera(tamaño="M", mensaje="Trust the Process")

"""B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
valores por defecto,""" 
def hacer_remera(tamaño="L", mensaje="Me gusta pyton"):
    print("Se creo una remera de tamaño", tamaño)
    print("Mensaje impreso en la remera:", mensaje)
hacer_remera()
#y la segunda con valores diferentes. 
hacer_remera("XL", "Confia en el proceso")

"""4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
número es la suma de los dos números inmediatamente anteriores """
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    seriedefibonacci = [0, 1]
    for i in range(2, n):
        seriedefibonacci.append(seriedefibonacci[i-1] + seriedefibonacci[i-2])
    return seriedefibonacci
numero = int(input("Ingrese un limite para la serie: "))
serie = fibonacci(numero)
print("Serie de Fibonacci con", numero, "elementos:",serie)






