from ControladorListaBi import Listabi
from Registro import Registro
def test():
    opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
    while opc != 0:
        if opc == 1:
            regcorecto = Registro('12', '25', '100', '90')
            print("""
            Hora:{}
            Temperatura:{}
            Humedad:{}
            Presion atmosferica:{}""".format(regcorecto.gethora(), regcorecto.gettemperatura(), regcorecto.gethumedad(),
                                             regcorecto.getpresion()))
            regcorecto.mostrardatos()
        if opc == 2:
            reincorrecto = Registro('doce', 'vinticinco', 'cien', 'noventa')
            print("""
                        Hora:{}
                        Temperatura:{}
                        Humedad:{}
                        Presion atmosferica:{}""".format(reincorrecto.gethora(), reincorrecto.gettemperatura(),
                                                         reincorrecto.gethumedad(), reincorrecto.getpresion()))
            reincorrecto.mostrardatos()
        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))



if __name__=='__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        test()
    print("_______main________")
    lista = Listabi()
    lista.cargadatos()
    print("ingrese 1 para ver datos del dia y hora que registran una maxima y minima respecto a la temperatura humedad y presion atmosferica")
    print("ingrese 2 para ver la temperatura promedio mensual por cada hora")
    print("ingrese 3 para ver la temperatura, humedad y precion atmosferica de un dia especifico")
    print("ingrese 0 para salir")
    b = int(input("ingrese la opcion a eleguir\n"))
    while b != 0:
          if b ==1:
             lista.mayorymenortemp()
             lista.mayorymenorhume()
             lista.mayorymenorpresion()

          if b == 2:
              lista.promedios()

          if b == 3:
              lista.mostrarlistapordia()
          print("ingrese 1 para ver datos del dia y hora que registran una maxima y minima respecto a la temperatura humedad y presion atmosferica")
          print("ingrese 2 para ver la temperatura promedio mensual por cada hora")
          print("ingrese 3 para ver la temperatura, humedad y precion atmosferica de un dia especifico")
          print("ingrese 0 para salir")
          b = int(input("ingrese la opcion a eleguir\n"))


