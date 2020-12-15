import os

def comprarPasaje():
    os.system('cls')
    print("*****************")
    print("Proceso de compra")
    print("*****************")
    cantPasajes = int(input("\nCuantos pasajes desea comprar: "))
    if cantPasajes <= 0 or cantPasajes > 33:
        print("\nCantidad de pasajes incorrecta, porfavor ingrese una cantidad entre 1 a 33.")
        c = input("\nPresione ENTER para continuar.")
        os.system('cls')
    else:
        os.system('cls')
        for i in range(cantPasajes):
            global rutPasajero
            rutPasajero=0
            print(f"Ingrese rut pasajero {i+1} (ej:12345678)")
            global listaRut
            listaRut = []
            while rutPasajero<11111110:
                rutPasajero=int(input("RUT: "))
                listaRut.append(rutPasajero)
            print("\nIngrese fila y asiento del pasajero.")
            print(f"Fila A {filaA}")
            print(f"Fila B {filaB}")
            print(f"Fila C {filaC}")
            print(f"\nFila D {filaD}")
            print(f"Fila E {filaE}")
            print(f"Fila F {filaF}")
            asignarAsiento()
        return listaRut

def listaPasajeros():
    os.system('cls')
    print("\n********************")
    print("Lista pasajeros (rut)")
    print("********************")
    for i in range(len(listaRut)):
        print(f"\n{listaRut[i]}")
        c = input("\nPresione ENTER para continuar.")
        os.system("cls")
        
def mostrarAsientos():
    os.system("cls")
    print("\nLos asientos acupados se le asigno una X")
    print(f"\nFila A {filaA}")
    print(f"Fila B {filaB}")
    print(f"Fila C {filaC}")
    print(f"\nFila D {filaD}")
    print(f"Fila E {filaE}")
    print(f"Fila F {filaF}")
    c = input("\nPresione ENTER para continuar.")
    os.system("cls")
    

def buscarPasajero():
    os.system('cls')
    print("********************")
    print("BUSQUEDA DE PASAJERO")
    print("********************")
    buscarRut=int(input("\nIngrese el RUT del pasajero que desea buscas, sin guion ni puntos: "))
    buscarRut in rutF
    if buscarRut in rutF:
        asientoPasajero=rutF.index(busca_rut)
        print(F"El pasajero {buscarRut} está ubicado en asiento {asientoPasajero+1} / fila F")
    else:
        if buscarRut in rutE:
            asientoPasajero=rutE.index(buscarRut)
            print(F"El pasajero {buscarRut} está ubicado en asiento {asientoPasajero+1} / fila E")
        else:
            if buscarRut in rutD:
                asientoPasajero=rutD.index(buscarRut)
                print(F"El pasajero {buscarRut} está ubicado en asiento {asientoPasajero+1} / fila D")
            else:
                if buscarRut in rutC:
                    asientoPasajero=rutC.index(buscarRut)
                    print(F"El pasajero {buscarRut} está ubicado en asiento {asientoPasajero+1} / fila C")
                else:
                    if buscarRut in rutB:
                        asientoPasajero=rutB.index(buscarRut)
                        print(F"El pasajero {buscarRut} está ubicado en asiento {asientoPasajero+1} / fila B")
                    else:
                        if buscarRut in rutA:
                            asientoPasajero=rutA.index(buscarRut)
                            print(F"El pasajero {buscarRut} está ubicado en asiento {asientoPasajero+1} / fila A")
                        else:
                            print("\n*****************************************************************")
                            print(f"El pasajero {buscarRut} no se encuestra registrado en el sistema.")
                            print("*****************************************************************")
    c = input("\nPresione ENTER para continuar")
    os.system("cls")
    
def asignarAsiento():
    print("\nPrecio asientos:")
    print("\nAsiento común\t\t\t(C), $60.000 pesos")
    print("Espacio adicional para piernas  (E), $80.000 pesos")
    print("No reclina\t\t\t(N), $50.000 pesos")
    filaPasajero="X"
    global contadorAsientoEspacio
    global contadorAsientoComun
    global contadorAsientoNoReclina
    while filaPasajero not in ("A", "B", "C", "D", "E", "F"):
        filaPasajero = input("\nIngrese Fila [A-B-C-D-E-F]: ").upper()
    asientoPasajero = int(input("Ingrese Asiento: "))
    if asientoPasajero in (1,2,3,4,5,18):                  
        contadorAsientoEspacio += 1
    if asientoPasajero in (6,7,8,9,11,12,13,14,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33):
        contadorAsientoComun += 1
    if asientoPasajero in (10,17):
        contadorAsientoNoReclina += 1
    if filaPasajero=="F":
        del filaF[asientoPasajero-1]                                   
        del rutF[asientoPasajero-1]
        filaF.insert((asientoPasajero-1),"X")
        rutF.insert((asientoPasajero-1),rutPasajero)
    if filaPasajero=="E":
        del filaE[asientoPasajero-1]
        del rutE[asientoPasajero-1]
        filaE.insert((asientoPasajero-1),"X")
        rutE.insert((asientoPasajero-1),rutPasajero)
    if filaPasajero=="D":
        del filaD[asientoPasajero-1]
        del rutD[asientoPasajero-1]
        filaD.insert((asientoPasajero-1),"X")
        rutD.insert((asientoPasajero-1),rutPasajero)
    if filaPasajero=="C":
        del filaC[asientoPasajero-1]
        del rutC[asientoPasajero-1]
        filaC.insert((asientoPasajero-1),"X")
        rutC.insert((asientoPasajero-1),rutPasajero)
    if filaPasajero=="B":
        del filaB[asientoPasajero-1]
        del rutB[asientoPasajero-1]
        filaB.insert((asientoPasajero-1),"X")
        rutB.insert((asientoPasajero-1),rutPasajero)
    if filaPasajero=="A":
        del filaA[asientoPasajero-1]
        del rutA[asientoPasajero-1]
        filaA.insert((asientoPasajero-1),"X")
        rutA.insert((asientoPasajero-1),rutPasajero)
    asientoPasajero=0
    print("\nOperación relizada correctamente.")
    c = input("\nPresione ENTER para continuar.")
    os.system('cls')
    
def reasignarAsiento():
    os.system('cls')
    rutPasajero = 0
    print("************************")
    print("REASIGNACION DE ASIENTOS")
    print("************************")
    rutPasajero = int(input("Indique el RUT del pasajero que desea reasignar, sin guion ni puntos: "))
    if rutPasajero in rutF:
        asiento=rutF.index(rutPasajero)
        rutF.remove(rutPasajero)
        del filaF[(asiento)]
        filaF.insert(asiento,str(asiento+1))
        pregunta = input(f"El pasajero RUT {rutPasajero} ha sido eliminado. Desea reasignarlo? [s|n]: ")
        if pregunta == "s":
            asignarAsiento()
    else:
        if rutPasajero in rutE:
            asiento=rutE.index(rutPasajero)
            rutE.remove(rutPasajero)
            del filaE[(asiento)]
            filaE.insert(asiento,str(asiento+1))
            pregunta = input(f"El pasajero RUT {rutPasajero} ha sido eliminado. Desea reasignarlo? [s|n]: ")
            if pregunta == "s":
                asignarAsiento()
        else:
            if rutPasajero in rutD:
                asiento=rutD.index(rutPasajero)
                rutD.remove(rutPasajero)
                del filaD[(asiento)]
                filaD.insert(asiento,str(asiento+1))
                pregunta = input(f"El pasajero RUT {rutPasajero} ha sido eliminado. Desea reasignarlo? [s|n]: ")
                if pregunta == "s":
                    asignarAsiento()
            else:
                if rutPasajero in rutC:
                    asiento=rutC.index(rutPasajero)
                    rutC.remove(rutPasajero)
                    del filaC[(asiento)]
                    filaC.insert(asiento,str(asiento+1))
                    pregunta = input(f"El pasajero RUT {rutPasajero} ha sido eliminado. Desea reasignarlo? [s|n]: ")
                    if pregunta== "s":
                        asignarAsiento()
                else:
                    if rutPasajero in rutB:
                        asiento=rutB.index(rutPasajero)
                        rutB.remove(rutPasajero)
                        del filaB[(asiento)]
                        filaB.insert(asiento,str(asiento+1))
                        pregunta = input(f"El pasajero RUT {rutPasajero} ha sido eliminado. Desea reasignarlo? [s|n]: ")
                        if pregunta == "s":
                            asignarAsiento()
                    else:
                        if rutPasajero in rutA:
                            asiento=rutA.index(rutPasajero)
                            rutA.remove(rutPasajero)
                            del filaA[(asiento)]
                            filaA.insert(asiento,str(asiento+1))
                            pregunta = input(f"El pasajero RUT {rutPasajero} ha sido eliminado. Desea reasignarlo? [s|n]: ")
                            if pregunta == "s":
                                asignarAsiento()

def gananciasTotales():
    os.system('cls')
    totalAsientosDinero = (contadorAsientoComun*60000)+(contadorAsientoNoReclina*50000)+(contadorAsientoEspacio*80000)
    totalAsientos = contadorAsientoComun + contadorAsientoNoReclina + contadorAsientoEspacio
    print("*****************")
    print("Ganancias totales")
    print("*****************")
    print("\nTipo de asiento\t\t\tCantidad\tTotal")
    print(f"Asiento común\t     $60.000\t{contadorAsientoComun}\t\t{contadorAsientoComun*60000}")
    print(f"Espacio para piernas $80.000\t{contadorAsientoEspacio}\t\t{contadorAsientoEspacio*80000}")
    print(f"No reclina\t     $50.000\t{contadorAsientoNoReclina}\t\t{contadorAsientoNoReclina*50000}")
    print(f"TOTAL\t\t\t\t{totalAsientos}\t\t{totalAsientosDinero}")
    c = input("\nPresione ENTER para continuar.")
    os.system('cls')

def mostrarUbicacionesDisponible():
    os.system('cls')
    print("\n************************")
    print("Ubicaciones disponibles")
    print("************************")
    print("\nAsintos disponibles asignados con una D.")
    print("Asientos reservados asignador con el RUT del pasajero.")
    print(f"\nFila A {rutA}")
    print(f"Fila B {rutB}")
    print(f"Fila C {rutC}")
    print(f"\nFila D {rutD}")
    print(f"Fila E {rutE}")
    print(f"Fila F {rutF}")
    c = input("\nPresione ENTER para continuar.")
    os.system('cls')
    
def menu():
    os.system('cls')
    salir = 7
    print("*****************************")
    print("SISTEMA DE RESERVA DE PASAJES")
    print("     Linea aérea Flash")
    print("*****************************")
    while salir == 7:
        listaMenu = ["Compra Pasajes","Mostrar Ubicaciones Disponibles", "Ver Listado de Pasajeros", "Buscar Pasajero", "Reasignar Asiento","Mostrar Ganancias Totales","Salir"]
        for i in listaMenu:
            index = listaMenu.index(i)
            print(f"{index+1}: {i}")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            comprarPasaje()
        elif opcion == 2:
            mostrarUbicacionesDisponible()
        elif opcion == 3:
           listaPasajeros()
        elif opcion == 4:
            buscarPasajero()
        elif opcion == 5:
            reasignarAsiento()
        elif opcion == 6:
            gananciasTotales()
        elif opcion == 7:
            break
        else:
            print("Opcion ingresada no valida, intentelo nuevamente.")
            
contadorAsientoEspacio = 0
contadorAsientoComun = 0
contadorAsientoNoReclina = 0
            
filaF=["E1", "E2", "E3", "E4", "E5", "C6", "C7", "C8", "C9", "N10", "C11", "C12", "C13", "C14", "C15", "C16", "N17", "E18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33"]
filaE=["E1", "E2", "E3", "E4", "E5", "C6", "C7", "C8", "C9", "N10", "C11", "C12", "C13", "C14", "C15", "C16", "N17", "E18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33"]
filaD=["E1", "E2", "E3", "E4", "E5", "C6", "C7", "C8", "C9", "N10", "C11", "C12", "C13", "C14", "C15", "C16", "N17", "E18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33"]
filaC=["E1", "E2", "E3", "E4", "E5", "C6", "C7", "C8", "C9", "N10", "C11", "C12", "C13", "C14", "C15", "C16", "N17", "E18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33"]
filaB=["E1", "E2", "E3", "E4", "E5", "C6", "C7", "C8", "C9", "N10", "C11", "C12", "C13", "C14", "C15", "C16", "N17", "E18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33"]
filaA=["E1", "E2", "E3", "E4", "E5", "C6", "C7", "C8", "C9", "N10", "C11", "C12", "C13", "C14", "C15", "C16", "N17", "E18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33"]


rutF=["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D", "14D", "15D", "16D", "17D", "18D", "19D", "20D", "21D", "22D", "23D", "24D", "25D", "26D", "27D", "28D", "29D", "30D", "31D", "32D", "33D"]
rutE=["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D", "14D", "15D", "16D", "17D", "18D", "19D", "20D", "21D", "22D", "23D", "24D", "25D", "26D", "27D", "28D", "29D", "30D", "31D", "32D", "33D"]
rutD=["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D", "14D", "15D", "16D", "17D", "18D", "19D", "20D", "21D", "22D", "23D", "24D", "25D", "26D", "27D", "28D", "29D", "30D", "31D", "32D", "33D"]
rutC=["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D", "14D", "15D", "16D", "17D", "18D", "19D", "20D", "21D", "22D", "23D", "24D", "25D", "26D", "27D", "28D", "29D", "30D", "31D", "32D", "33D"]
rutB=["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D", "14D", "15D", "16D", "17D", "18D", "19D", "20D", "21D", "22D", "23D", "24D", "25D", "26D", "27D", "28D", "29D", "30D", "31D", "32D", "33D"]
rutA=["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D", "14D", "15D", "16D", "17D", "18D", "19D", "20D", "21D", "22D", "23D", "24D", "25D", "26D", "27D", "28D", "29D", "30D", "31D", "32D", "33D"]

menu()
