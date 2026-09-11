'''
    Programa que implementa una calculadora con operaciones basicas.
'''
import sys

def menu():
    print("Selecciona una opcion:")
    print("0) Salir", "1) Sumar", "2) Restar", "3) Multiplicar", "4) Dividir", sep="\n")
    opc = input()
    return opc

def calcular(opcion, op1, op2):
    match opcion:
        case 1: return op1 + op2
        case 2: return op1 - op2
        case 3: return op1 * op2
        case 4: return op1 / op2
        case _: 
            print("Operacion no valida.")
            return -1

def calculadora():
    opcion = int(menu())
    if (opcion == 0):
        sys.exit()
    op1 = int(input("Ingresa el primer operando: "))
    op2 = int(input("Ingresa el segundo operando: "))
    resultado = calcular(opcion, op1, op2)
    print(f"El resultado es: {resultado}\n")

def main():
    print("*********Bienvenido a la calculadora***********")
    while (True):
        calculadora()

if __name__ == "__main__":
    main()
