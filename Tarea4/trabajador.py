class Trabajador:
    def __init__(self , tam):
        self.__info = [0 for x in range(tam)]

    def get_item( self , posicion):
        dato = -1
        try:
            dato = self.__info[posicion]
        except Exception as e:
            print("Error de posicion")
            dato = "Error"
        return dato

    def set_item(self, dato, posicion):
        try:
            self.__info[posicion] = dato
        except Exception as e:
            print("Error de posicion")
