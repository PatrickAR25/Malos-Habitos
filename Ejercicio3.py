def AreaRectangulo(Largo,Ancho):
    AreaRectanguloTotal = Largo * Ancho
    return AreaRectanguloTotal

def AreaTriangulo(Base, Altura):
    AreaTrianguloTotal = 0.5 * Base * Altura
    return AreaTrianguloTotal

if __name__=="__main__":
    Largo = float(input("Ingrese el Largo del rectangulo: "))
    Ancho = float(input("Ingrese el Ancho del rectangulo: "))
    Base = float(input("Ingrese la Base del Triangulo: "))
    Altura = float(input("Ingrese la Altura del Triangulo: "))
    AreaRectanguloFinal = AreaRectangulo(Largo,Ancho)
    AreaTrianguloFinal = AreaTriangulo(Base, Altura)
    print(f"{Largo} * {Ancho} = {AreaRectanguloFinal}")
    print(f"{Base} * {Altura} = {AreaTrianguloFinal}")




