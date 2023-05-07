
class Registro:
    __hora = ''
    __variable_temperatura = ''
    __variable_humedad = ''
    __variable_atmosferica = ''

    def __init__(self,x = 'hora', y = 'temperatura', z = 'humedad', w = 'atmosferica'):
        self.__hora = int(x)
        self.__variable_temperatura = float(y)
        self.__variable_humedad = float(z)
        self.__variable_atmosferica = float(w)

    def mostrardatos(self):
       print(" {}               {}              {}                {}".format(self.__hora,self.__variable_temperatura,self.__variable_humedad,self.__variable_atmosferica))

    def gethora(self):
        return self.__hora
    def gettemperatura(self):
        return self.__variable_temperatura

    def gethumedad(self):
        return self.__variable_humedad

    def getpresion(self):
        return self.__variable_atmosferica
