from Registro import Registro
import csv
class Listabi:
    __listabi = [[]]

    def __init__(self):
        self.__listabi  = [[None for _ in range(23)] for _ in range(31)]
    def cargadatos(self):
        i = 0
        archivo = open('Registro.csv')
        reader = csv.reader(archivo,delimiter=(','))
        for fila in reader:
            if int(fila[0]) == 23:
                i = i+1
            else:
                hora = int(fila[0])
                temperatura = fila[1]
                humedad = fila[2]
                presion = fila[3]
                self.__listabi[i][hora] = Registro(hora, temperatura, humedad, presion)

    def mayorymenortemp(self):
        tempemax = max(Registro.gettemperatura() for Registro in sum(self.__listabi,[]))
        tempmin = min(Registro.gettemperatura() for Registro in sum(self.__listabi,[]))
        diamax=0
        horamax=0
        diamin=0
        horamin=0
        for dia in range(30):
            for hora in range (23):
                if self.__listabi[dia][hora].gettemperatura() == tempemax:
                    diamax = dia
                    horamax = hora
                if self.__listabi[dia][hora].gettemperatura() == tempmin:
                    diamin = dia
                    horamin = hora
        print("_________temperatura_____________")
        print("el dia:{} a la hora:{}:00 se  registro una temperatura maxima de: {}".format(diamax+1,horamax+1,tempemax))
        print("el dia:{} a la hora:{}:00 se  registro una temperatura minima de: {}".format(diamin+1,horamin+1,tempmin))
        print("__________humedad____________")

    def mayorymenorhume(self):
        humemax = max(Registro.gethumedad() for Registro in sum(self.__listabi,[]))
        humemin = min(Registro.gethumedad() for Registro in sum(self.__listabi,[]))
        diamax=0
        horamax=0
        diamin=0
        horamin=0
        for dia in range(30):
            for hora in range (23):
                if self.__listabi[dia][hora].gethumedad() == humemax:
                    diamax = dia
                    horamax = hora
                if self.__listabi[dia][hora].gethumedad() == humemin:
                    diamin = dia
                    horamin = hora

        print("el dia:{} a la hora:{}:00 se  registro la humedad maxima de: {}".format(diamax+1,horamax+1,humemax))
        print("el dia:{} a la hora:{}:00 se  registro la humedad minima de: {}".format(diamin+1,horamin+1,humemin))
        print("_________presion atmosferica___________")

    def mayorymenorpresion(self):
        presionmax = max(Registro.getpresion() for Registro in sum(self.__listabi,[]))
        presionmin = min(Registro.getpresion() for Registro in sum(self.__listabi,[]))
        diamax=0
        horamax=0
        diamin=0
        horamin=0
        for dia in range(30):
            for hora in range (23):
                if self.__listabi[dia][hora].getpresion() == presionmax:
                    diamax = dia
                    horamax = hora
                if self.__listabi[dia][hora].getpresion() == presionmin:
                    diamin = dia
                    horamin = hora

        print("el dia:{} a la hora:{}:00 se  registro una presion atmosferica maxima de: {}".format(diamax+1,horamax+1,presionmax))
        print("el dia:{} a la hora:{}:00 se  registro una presion atmosferica minima de: {}".format(diamin+1,horamin+1,presionmin))
        print("______________________________")
    def promedios(self):
        for hora in range(23):
            temperatura_promedio = 0
            for dia in range(30):
                temperatura_promedio += self.__listabi[dia][hora].gettemperatura()
            print("la temperatura promedio mensual que se registro a las: {}:00 es de:{}°".format(hora,(round(temperatura_promedio/24))))

    def mostrarlistapordia(self):
        dia = int(input('ingresa el dia a conocer sus registros climaticos por hora\n'))
        print("""hora          Temperatura         Humedad             presion """)
        for hora in range(23):
            listaa = self.__listabi[dia][hora]
            listaa.mostrardatos()


