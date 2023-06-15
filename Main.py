from ply.lex import lex
from ply.yacc import yacc
import Fuenza as F

# Definir las palabras clave y tokens
keywords = {
    'show': 'GRAFICAR',
    'window_size': 'WINDOW_SIZE',
    'exit': 'EXIT',
    'room_size': 'ROOM_SIZE',
    'backround_color': 'BK_COLOR',
    'room_color': 'ROOM_COLOR',
    'room_units': 'ROOM_UNITS',
    'item_chance': 'ITEM_CHANCE',
    'boss_chance': 'BOSS_CHANCE',
    'passage_width': 'PASSAGE_WIDTH'
}

tokens = [
    'ID',
    'NUMBER',
] + list(keywords.values())


# Expresiones regulares para los tokens
t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_error(t):
    print(f'Error: Carácter inesperado "{t.value[0]}"')
    t.lexer.skip(1)

lexer = lex()

# Reglas de sintaxis
def p_statement_function(p):
    '''
    statement : GRAFICAR
              | WINDOW_SIZE NUMBER NUMBER
              | EXIT
              | ROOM_SIZE NUMBER NUMBER
              | BK_COLOR NUMBER NUMBER NUMBER
              | ROOM_COLOR NUMBER NUMBER NUMBER
              | ROOM_UNITS NUMBER
              | ITEM_CHANCE NUMBER
              | BOSS_CHANCE NUMBER
              | PASSAGE_WIDTH NUMBER
            
    '''
    if p[1] == 'show':

        gen = F.gen()
        if not gen:
            F.grafico()

    elif p[1] == 'window_size':
        # Acciones para la palabra clave "window_size"
        width = p[2]
        height = p[3]
        F.cambio_ventana(width,height)
        print(f'Se estableció el tamaño de la ventana: {width}x{height}')
    elif p[1] == 'exit':
        # Acciones para la palabra clave "exit"
        print('Saliendo del programa...')
        raise SystemExit
    elif p[1] == 'room_size':
        width = p[2]
        height = p[3]
        F.cambiox(width)
        F.cambioy(height)
        print(f'Se estableció el tamaño de las piezas: {width}x{height}')
    elif p[1] == 'backround_color':
        r = p[2]
        g = p[3]
        b = p[4]
        F.fondo(r,g,b)
        print(f'Se estableció el color para el fondo: {r},{g},{b}')
    elif p[1] == 'room_color':
        r = p[2]
        g = p[3]
        b = p[4]
        F.habitacion(r,g,b)
        print(f'Se estableció el color para las habitaciones: {r},{g},{b}')
    elif p[1] == 'room_units':
        n = p[2]
        
        F.cantidad(n)
        print(f'Se estableció el numero de habitaciones a: {n}')
    elif p[1] == 'item_chance':
        n = p[2]
        if 0 <= n <= 1:
            temp = F.probit(n)
            if temp == True:
                print(f'Se estableció la probabilidad de ítem: {n}')
        else:
            print('Error: La probabilidad de ítem debe estar entre 0 y 1')
    elif p[1] == 'boss_chance':
        n = p[2]

        if 0 <= n <= 1:
            temp = F.probbo(n)
            if temp == True:
                print(f'Se estableció la probabilidad de boss: {n}')
        else:
            print('Error: La probabilidad de ítem debe estar entre 0 y 1')
    elif p[1] == 'passage_width':
        n = p[2]
        F.grosor_pasillos(n)
        print(f'Se estableció el ancho de los pasillos: {n}')
def p_error(p):
    if p:
        print(f'Error de sintaxis en el token "{p.value}"')
    else:
        print('Error de sintaxis al finalizar la entrada')

parser = yacc()

# Bucle de ejecución continua
while True:
    input_text = input('> ')

    lexer.input(input_text)
    parser.parse(input_text, lexer=lexer)