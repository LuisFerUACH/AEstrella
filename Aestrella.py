class Edo:
    def __init__(self, nombre, padre,g ,h ,f):
        self.nombre = nombre
        self.padre = padre
        self.g = g
        self.h = h
        self.f = f

## Esto define a la funcion miembro
def miembro ( edo , lista ) :
    resp = False
    cuenta =0
    donde = -1
    adentro = False
    for nodo in lista:
        if nodo.nombre == edo:
            donde = cuenta
            adentro = True
            break
        cuenta = cuenta +1
    return adentro , donde

## Esto define la funcion para expandir la lista Abiertos
def expandir(actual, meta, proble, dlr, Abiertos, Cerrados):
    hijos = proble [actual.nombre]
    for hijo in hijos:
        mC , _ = miembro(hijo, Cerrados)
        mA , pA = miembro(hijo, Abiertos)
        if not mC:
            gnue =(actual.g + dlr[actual.nombre][hijo])
            hnue = dlr[hijo][meta]
            fnue = gnue + hnue
            if mA:
                fori = Abiertos[pA].f
                if fnue < fori:
                    Abiertos[p2]= Edo(hijo, actual.nombre, gnue, hnue, fnue)
            else:
                Abiertos.append(Edo(hijo, actual.nombre, gnue, hnue, fnue))
    return Abiertos

## Esta es la funcion para extraer el siguiente estado a visitar
def siguiente(Abiertos):
    fmejor =100
    mejor = None
    donde = -1
    cuenta =0
    for nodo in Abiertos:
        if nodo.f < fmejor:
            mejor = nodo
            fmejor = nodo.f
            donde = cuenta
        cuenta = cuenta +1
    del Abiertos[donde]
    return Abiertos , mejor

## Esto implementa la busuqeda a estrella
def astar(ini, meta, proble, dlr):
    Abiertos =[Edo(ini, ini,0, dlr[ini][meta], dlr[ini][meta])]
    Cerrados =[]
    listo = False
    while not listo:
        Abiertos , actual = siguiente(Abiertos)
        if actual.nombre == meta:
            listo = True
            Cerrados.append(actual)
        else:
            Cerrados.append(actual)
            Abiertos = expandir(actual , meta , proble , dlr , Abiertos ,Cerrados )
    return Cerrados

## Esto forma el camino a partir de loq ue tiene Cerrados
def getCamino(ini ,Cerrados):
    resp =[]
    actual = Cerrados[ -1].nombre
    listo = False
    while not listo:
        if actual == ini :
            listo = True
            resp.insert(0 , actual)
        else:
            for nodo in Cerrados:
                if nodo.nombre == actual:
                    resp.insert(0 , actual)
                    actual = nodo.padre
                    break
    return resp

## Esta es la funcion principal del programa
def main(ini , meta):
    proble ={ 'A':[ 'B','C'] ,'B':[ 'A','C','E','G'] ,'C':[ 'A','B','D'
    ,'F'] ,'D':['C','F'] ,'E':[ 'B','G','F'] ,'F':[ 'D','E','C'],'G':[ 'B','E']}
    
    dlr ={'A':{'A':0, 'B':20 , 'C':15 , 'D':11 , 'E':22 , 'F':24, 'G':45} ,
          'B':{ 'A':20 , 'B':0 , 'C':6 , 'D':9 , 'E':5 , 'F':8, 'G':30} ,
          'C':{ 'A':15 , 'B':6 , 'C':0 , 'D':5 , 'E':4 , 'F':9, 'G':27} ,
          'D':{ 'A':11 , 'B':9 , 'C':5 , 'D':0 , 'E':9 , 'F':7, 'G':32} ,
          'E':{ 'A':22 , 'B':5 , 'C':4 , 'D':9 , 'E':0 , 'F':4, 'G':25} ,
          'F':{ 'A':24 , 'B':8 , 'C':9 , 'D':7 , 'E':4 , 'F':0, 'G':22},
          'G':{ 'A':45 , 'B':30 , 'C':27 , 'D':32 , 'E':25 , 'F':22, 'G':0}}
    cerrados = astar ( ini , meta , proble , dlr )
    camino = getCamino ( ini , cerrados )
    print ('El camino de la busqueda A* es:')
    print ( camino )

## Este es el punto de entrada al programa
if __name__ == '__main__':
    main ('G','A')
