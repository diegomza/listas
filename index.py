"""1 - Pedir números al usuario y cada valor se debe agregar a una lista,
se termina de guardar los numeros cuando se ingrese 0, el cero no se guarda,
una vez que se haya dejado de pedir mostrar la lista ordenada de menor a mayor,
sumar todos los numeros, mostrar la suma total y el promedio."""

print("Por favor ingrese un número. Para SALIR presione 0")

lista = []
num = 1
suma = 0
cont = 0
promedio = 0
band = True

if num != 0:
    while num != 0:
        num = int(input("Ingrese un valor -> "))
        lista.append(num)
        suma += num
        
if num == 0:
    print("Usted presionó 0 y está afuera del programa -- Gracias!! --")
    
lista.pop()        
len(lista)
promedio = suma / len(lista)
lista.sort()
print(lista)
print(f"La suma de los valores ingresados es {suma}")
print(f"El promedio de los valores ingresados es {promedio}")

    
    

"""2 - Hacer un menu donde se puedan agregar nombres de personas, se pueda eliminar un nombre,
modificar un nombre, eliminar la lista completa o mostrar todos los nombres, en caso de que
no haya nombres en la lista mostrar un mensaje que diga "No hay nombres en la lista"."""

print("Con el teclado numérico elija la opción deseada")

opc = 1
nombre = 0
lista2 = []
depurar = 0
nuevo_nombre = 0
num = 1
cont = 0

while opc != 0:
    print("1 - Agregar nombre")
    print("2 - Eliminar nombre")
    print("3 - Modificar nombre")
    print("4 - Eliminar lista")
    print("5 - Mostrar lista de nombres")
    print("0 - Salir")
    opc = int(input("-> "))
    if opc <=5 and opc >=0:
        if opc == 1:
            nombre = input("Ingrese el nombre que desea ingresar -> ")
            lista2.append(nombre)
        elif opc == 2:
            nombre = input("Ingrese el nombre que desea borrar -> ")
            lista2.remove(nombre)
        elif opc == 3:
            print(lista2)
            nombre = input("Ingrese el nombre que desea modificar -> ")
            if nombre not in lista2:
                print("El nombre no se encuentra en la lista")
                nombre = input("Intente nuevamente -> ")
            if nombre in lista2:
                pos = lista2.index(nombre)
                nuevo_nombre = input("Ingrese el nombre modificado -> ")
                lista2[pos] = nuevo_nombre
                print(lista2)            
        elif opc == 4:
            print(lista2)
            depurar = int(input("ATENCIÓN: Está seguro de eliminar la lista completa?? 1 = SI - 2 = NO -> "))
            if depurar == num:
                lista2.clear()
                print(lista2)
                print("No hay nombres en la lista")                
        elif opc == 5:
            cont = len(lista2)
            if cont == 0:
                print("No hay nombres en la lista")
            else:
                print(lista2)
        elif opc == 0:
            print("Uds presionó 0 y saldrá del programa. Gracias por participar :)")
    else:
        print("El valor ingresado no es válido. Itente nuevamente")        
        
       