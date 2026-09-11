'''
    Proyecto 1 — Calculadora de consola
'''
import sys
import math

def menu():
    print("Selecciona una opcion:")
    print("0) Salir", "1) Suma", "2) Resta", "3) Multiplicacion", "4) Division", \
          "5) Potencia", "6) Modulo", "7) Raiz cuadrada", sep="\n")
    opcion = input()
    return opcion

def calcular(opcion, op1, op2):
    match opcion:
        case 1: return op1 + op2
        case 2: return op1 - op2
        case 3: return op1 * op2
        case 4: return op1 / op2
        case 5: return op1 ** op2
        case 6: return op1 % op2
        case 7: return math.sqrt(op1)
        case _: print("Operacion no valida.")

def calculadora(opcion):
    op1 = float()
    op2 = float()
    if (opcion != 7):
        op1 = float(input("Ingrese el primer numero: "))
        op2 = float(input("Ingrese el segundo numero: "))
    else: 
        op1 = float(input("Ingrese el operador: "))

    if (opcion == 4 and op2 == 0):
        print("La division etre cero no esta definidad")
        return
    elif (opcion == 6):
        op1 = int(op1)
        op2 = int(op2)
    resultado = calcular(opcion, op1, op2)
    print(f"El resultado es: {resultado}\n")


def main():
    print("\n**************  Bienvenido a la calculadora  *****************\n")
    while (True):
        opcion = int(menu())
        if (opcion == 0):
            sys.exit()
        calculadora(opcion)
    

if __name__ == "__main__":
    main()