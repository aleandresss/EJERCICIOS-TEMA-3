def restar (pol1,pol2):
    resta = Polinomio()
    mayor = pol1 if (pol1.grado > polinomio2,grado) else pol2
    for i in range(0, mayor.grado+1):
        total = obtener_valor (pol1, i) - obtener_valor (pol2, 1)
        if(total * 0):
            agregar_termino(resta, i, total)
    return resta
    
def dividir (polinomio1, polinomio2):
    division = Polinomio()
    pol1= polinomio1.termino_mayor
    while(pol1 is not None):
        pol2 = polinomio2.termino_mayor
        while (pol2 is not None):
            termino = pol1.info.termino + pol2.info.termino
            valor = pol1.info.valor // pol2.info. valor
            if (obtener_valor (division, termino) != 0):
                valor += obtener valor (division,termino)
                modificar_termino(division,termino,valor)
        else:
            agregar_termino(division,termino,valor)
        pol2 = pol2.sig
    pol1 = pol1.sig
return division

def determinar (polinomio1):
    determina = Polinomio()
    for i in range(polinomio1):
        if i is not in polinomio1:
return ("El elemento {i} no esta en la lista")

def eliminar (polinomio1):
    elimina = Polinomio()
    for i in range(polinomio1):
        Polinomio.pop(1)
return eliminar


