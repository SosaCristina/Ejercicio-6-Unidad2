from ClaseViajeroFrecuente import ViajeroFrecuente
import csv
from ManejadorViajero import Manejador

if __name__=="__main__":

    objeto=Manejador()
    objeto.TestLista()
    print("VIAJERO CON MAYOR CANTIDAD DE MILLAS")
    objeto.mayor()
    print("_______________________________________________________")
    print("ACUMULAR MILLAS")
    print ("Ingrese numero de viajero que desee acumular millas")
    numero=int (input())
    indice=int
    indice=0
    indice=objeto.buscar(numero)
    objeto.acumular(indice)
    print("_______________________________________________________")
    print("CANJEAR MILLAS")
    print ("Ingrese numero de viajero que desee canjear millas")
    num=int (input())
    indice= objeto.buscar(num)
    objeto.canjear(indice)
