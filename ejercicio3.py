class naves():
    def __init__(self,nombre,largo,tripulacion,pasajeros) -> None:
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros 
    def __str__(self): #str imprime
        return "(El nombre de la nave es {}, tiene un largo de {} metros y {}{} cantidad de tripulacion y pasajeros)".format(self.nombre,self.largo,self.tripulacion,self.pasajeros)

#determinar cuáles son las cinco naves con mayor cantidad de pasajeros
from naves import*
class cantidad (naves):
    def __init__(self,nombre,largo,tripulacion,pasajeros):
        cantidad.__init__(self,nombre,largo,tripulacion)
        self.pasajeros = pasajeros

    for i in range (naves):
        cantidad = sorted(naves.reverse = True) #lo ordeno de mayor a menor 
        return cantidad [0,1,2,3,4] #retorno las 5 primeroas naves 
        

#indicar cuál es la nave que requiere mayor cantidad de tripulación
from naves import*
class cantidad (naves):
    def __init__(self,nombre,largo,tripulacion,pasajeros):
        cantidad.__init__(self,nombre,largo,pasajeros)
        self.tripulacion = tripulacion

    for i in range (naves):
        cantidad = sorted(naves.reverse = True) #lo ordeno 
        return cantidad[0]

#mostrar todas las naves que comienzan con AT
from naves import*
class AT (naves):
    def __init__(self,nombre,largo,tripulacion,pasajeros):
        cantidad.__init__(self,largo,tripulacion,pasajeros)
        self.nombre = nombre

    def empieza_con(cadena, subcadena):
    longitud_subcadena = len(subcadena)
    extraido = cadena[0:longitud_subcadena]
    if extraido == subcadena:
        return True
    else:
        return False

    print(empieza_con("at...", "a"))  # True
    print(empieza_con("at...", "x"))  # False

#listar todas las naves que pueden llevar seis o más pasajeros;
from naves import*
class cantidad (naves):
    def __init__(self,nombre,largo,tripulacion,pasajeros):
        cantidad.__init__(self,nombre,largo,tripulacion)
        self.pasajeros = pasajeros

    for cantidad in range (naves):
        while cantidad> 6
        return "(Esta nave puede llevar 6 o más pasajeros"
        
        
