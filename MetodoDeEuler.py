"""
Proyecto final de python
Elaborado por: Jose Fernando Ramirez Bravo
Para la materia de ecuaciones diferenciales
Fecha: 11/10/2023
"""
import numpy as np
import matplotlib.pyplot as plt


def menu():
    print("==================================================================")
    print("            Calculadora de Ecuaciones diferenciales               ")
    print("==================================================================")
    print("Seleccione el método:")
    print("1. Metodo de Euler")
    print("2. Metodo de Runge-Kutta")
    print("3. Metodo de Euler Modificado")
    print("4. Comparar los tres métodos")
    print("5. Salir")


def f(x, y):
    return x + y


def validar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")


def Euler():
    print("Haz elegido la opción Euler")
    x = validar_numero("Ingrese el valor inicial de x: ")
    y = validar_numero("Ingrese el valor inicial de y: ")
    h = validar_numero("Ingrese el tamaño del paso (h): ")
    n = int(validar_numero("Ingrese el número de pasos (n): "))
    valor_x = [x]
    valor_y = [y]

    print("\nResultados:")
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h

        valor_x.append(x)
        valor_y.append(y)
        print(f"Y({valor_x[-1]:.2f}) = {valor_y[-1]:.2f}")

    equacion_label = "Método de Euler"
    plt.plot(valor_x, valor_y, label=equacion_label, marker='o', linestyle='-', markersize=4)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    for i in range(len(valor_x)):
        plt.annotate(f'({valor_x[i]:.2f}, {valor_y[i]:.2f})', (valor_x[i], valor_y[i]), textcoords="offset points",
                     xytext=(0, 10), ha='center')

    plt.show()
    return valor_x, valor_y


def Rk():
    print("Haz elegido la opción Runge-Kutta")
    x = validar_numero("Ingrese el valor inicial de x: ")
    y = validar_numero("Ingrese el valor inicial de y: ")
    h = validar_numero("Ingrese el tamaño del paso (h): ")
    n = int(validar_numero("Ingrese el número de pasos (n): "))

    valor_x = [x]
    valor_y = [y]

    print("\nResultados:")
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + (h / 2) * k1)
        k3 = f(x + h / 2, y + (h / 2) * k2)
        k4 = f(x + h / 2, y + h * k3)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h

        valor_x.append(x)
        valor_y.append(y)
        print(f"Y({valor_x[-1]:.2f}) = {valor_y[-1]:.2f}")

    equacion_label = "Método de Runge-Kutta"
    plt.plot(valor_x, valor_y, label=equacion_label, marker='o', linestyle='-', markersize=4)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    for i in range(len(valor_x)):
        plt.annotate(f'({valor_x[i]:.2f}, {valor_y[i]:.2f})', (valor_x[i], valor_y[i]), textcoords="offset points",
                     xytext=(0, 10), ha='center')

    plt.show()

    return valor_x, valor_y


def EulerMod():
    print("Haz elegido la opción Euler Modificado")
    x = validar_numero("Ingrese el valor inicial de x: ")
    y = validar_numero("Ingrese el valor inicial de y: ")
    h = validar_numero("Ingrese el tamaño del paso (h): ")
    n = int(validar_numero("Ingrese el número de pasos (n): "))

    valor_x = [x]
    valor_y = [y]

    print("\nResultados:")
    for i in range(n):
        y0 = y + h * f(x, y)
        y = y + (h / 2) * (f(x, y) + f(x + h, y0))
        x = x + h

        valor_x.append(x)
        valor_y.append(y)
        print(f"Y({valor_x[-1]:.2f}) = {valor_y[-1]:.2f}")

    equacion_label = "Método de Euler Modificado"
    plt.plot(valor_x, valor_y, label=equacion_label, marker='o', linestyle='-', markersize=4)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    for i in range(len(valor_x)):
        plt.annotate(f'({valor_x[i]:.2f}, {valor_y[i]:.2f})', (valor_x[i], valor_y[i]), textcoords="offset points",
                     xytext=(0, 10), ha='center')

    plt.show()

    return valor_x, valor_y


while True:
    menu()
    opcion = input("Seleccione el método a evaluar: ")
    if opcion == "1":
        x_euler, y_euler = Euler()
    elif opcion == "2":
        x_rk, y_rk = Rk()
    elif opcion == "3":
        x_euler_mod, y_euler_mod = EulerMod()
    elif opcion == "4":
        if 'x_euler' in locals() and 'y_euler' in locals() and 'x_rk' in locals() and 'y_rk' in locals() and \
                'x_euler_mod' in locals() and 'y_euler_mod' in locals():
            plt.figure(figsize=(10, 6))
            plt.plot(x_euler, y_euler, label="Euler", marker='o', linestyle='-', markersize=4)
            plt.plot(x_rk, y_rk, label="Runge-Kutta", marker='o', linestyle='-', markersize=4)
            plt.plot(x_euler_mod, y_euler_mod, label="Euler Modificado", marker='o', linestyle='-', markersize=4)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("¡Debes ejecutar al menos uno de los métodos primero!")
    elif opcion == "5":
        print("¡Adiós!")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")


"""
ZONA DE PRUEBAS *IGNORAR CODIGO*
import numpy as np

n = 10
x = 0
y = 1
x1 = 1
h = (x1-x)/n
for x in range(n):
    f = x + y
    y = y + h * f
    x = x + h
    print(x,y)

n = 10
x = 0
y = 1
x1 = 1
h = (x1 - x) / n

# Crear listas para almacenar los valores de x e y
x_values = [x]
y_values = [y]

for i in range(n):
    f = x + y
    y = y + h * f
    x = x + h

    # Agregar los valores a las listas
    x_values.append(x)
    y_values.append(y)

# Visualizar los resultados usando Matplotlib
plt.plot(x_values, y_values, 'o', '-')
plt.title('Integración Numérica')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
"""