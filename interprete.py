# Importaciones
import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = ('NUME','SUMA','RESTA','MULT','DIVI','PAR_IZQ','PAR_DER','EOL')

# Reglas para tokens que no implican un valor
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIVI = r'\/'
t_PAR_IZQ = r'\('
t_PAR_DER = r'\)'
t_EOL = r'\n'

# Función para el token NUME que sí implica valor
def t_NUME(t):
    r'[0-9]+\.[0-9]+|[0-9]+'
    t.value = float(t.value)
    return t

# Función para manejar errores léxicos
def t_error(t):
    print('Hubo un error lexico...')
    
# Regla para S -> E EOL
def p_s(p):
    '''
    s : e EOL
    '''
    p[0] = p[1]
    return p[0]

# Reglas para E -> E + T y E -> E - T
def p_e1(p):
    '''
    e : e SUMA t
        | e RESTA t
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]

# Regla para E -> T
def p_e2(p):
    '''
    e : t
    '''
    p[0] = p[1]

# Reglas para T -> T * F y T -> T / F
def p_t1(p):
    '''
    t : t MULT f
        | t DIVI f
    '''
    if p[2] == '*':
        p[0]=p[1]*p[3]
    else:
        p[0]=p[1]/p[3]

# Regla para T -> F
def p_t2(p):
    '''
    t : f
    '''
    p[0] = p[1]
    
# Regla para F -> ( E )
def p_f1(p):
    '''
    f : PAR_IZQ e PAR_DER
    '''
    p[0] = p[2]
    
# Regla para F -> nume
def p_f2(p):
    '''
    f : NUME
    '''
    p[0] = p[1]
    
# Función para manejar errores sintacticos
def p_error(p):
    print('Hubo un error sintactico...')

# Función principal
def interprete(cadena):
    try:
        lexer = lex.lex()
        parser = yacc.yacc()
        cadena = cadena + '\n'
        result = parser.parse(cadena,lexer=lexer)
        if not parser.errorok:
            return 'Hubo un error sintactico con la expresión aritmética...'
        return result
    except lex.LexError:
        return 'Hubo un error léxico con la expresión aritmética...'