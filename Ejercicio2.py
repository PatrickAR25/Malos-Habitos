
def multiplicacion(termino1, termino2):
    producto = termino1 * termino2
    return producto

def suma(producto, termino3):
    sumatoria = producto + termino3
    return sumatoria

if __name__=="__main__":
    multiplicando = float(input("Ingrese Multiplicando: "))
    multiplicador = float(input("Ingrese Multiplicador: "))
    sumador = float(input("Ingrese Sumando: "))
    multiplica = multiplicacion(multiplicando, multiplicador)
    sumatotal = suma(multiplica, sumador)
    print(f"{multiplicando} * {multiplicador} + {sumador} = {sumatotal}")

