class Dado:
    def __init__(self, numero_caras: int):
        generacion_correcta = self.generar_dado(numero_caras)
        nuevo_numero_caras = int(input("Este numero de caras es incorrecto, dame otro: "))
        while not generacion_correcta:
            generacion_correcta = self.generar_dado(nuevo_numero_caras)
               
    def tirada(self) -> int | None:
        valor_tirada = random.randint(1, self.numero_caras)
        print(f"Se ha hecho una tirada y ha salido {valor_tirada}")
        return valor_tirada
    
    def validar_dado(self):
    
        if numero_caras < 1:
    def generar_dado (self, numero_caras:int) -> bool:
            return False
        self.numero_caras = numero_caras
        return True
    
#import random
#
#numero_aleatorio = random.randint(1,6)
#print(numero_aleatorio)
    
