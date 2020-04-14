def sumar():
    a = float(input('Ingrese primer número: '))
    b = float(input('Ingrese segundo número: '))
    print(f'\nLa suma es: {a+b}')

def restar():
    a = float(input('Ingrese primer número: '))
    b = float(input('Ingrese segundo número: '))
    print(f'\nLa resta es: {a-b}')

def multiplicar():
    a = float(input('Ingrese primer número: '))
    b = float(input('Ingrese segundo número: '))
    print(f'\nLa multiplicación es: {a*b}')

def dividir():
    a = float(input('Ingrese primer número: '))
    b = float(input('Ingrese segundo número: '))
    print(f'\nLa división es: {a/b}')

sw = True
while sw:
    menu = '''
    ========= Calculadora ========
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir
    '''    
    print(menu)
    
    opcion = int(input('Elija una opción: '))

    if opcion is 1:
        sumar()
    elif opcion is 2:
        restar()
    elif opcion is 3:
        multiplicar()
    elif opcion is 4:
        dividir()
    elif opcion is 5:
        print('Programa finalizado....')
        sw = False
    else:
        print('Opción inválida, intente nuevamente')
