# Pequeño Intérprete

## Descripción

Implementar un pequeño intérprete en el lenguaje de programación de Python, el cual pueda realizar expresiones matemáticas simples, las cuales son la suma, resta, multiplicación, división y el uso de paréntesis dentro de la expresión.

La siguiente gramática aumentada está definida de la siguiente manera:

$$
𝐺 = \{\{𝑛𝑢𝑚𝑒, +, −, ∗, /, (, ), \$, 𝑒𝑜𝑙\}, \{𝑆, 𝐸, 𝑇 , 𝐹\}, 𝑆, 𝑃 \}
$$

La siguiente expresión seria de la siguiente manera:

$$
𝑃 = \{𝑆 → 𝐸 𝑒𝑜𝑙 𝐸 → 𝐸 + 𝑇 |𝐸 − 𝑇 |𝑇 𝑇 → 𝑇 ∗ 𝐹|𝑇 /𝐹|𝐹 𝐹 → (𝐸)|𝑛𝑢𝑚𝑒\}
$$

## Tokens

Los tokens que se usan para reconocer las cadenas son los siguientes:

```python
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
```

## Ejecución

Para ejecutar el programa se debe ejecutar el siguiente comando:

```bash
python3 interprete.py
```

## Ejemplos

Entrada

```bash
(2.34/3.2)*15
```

Salida

```bash
10.96875
```

Entrada

```bash
(4.32*2.43)/(1+2)
```

Salida

```bash
3.4992000000000005
```

Entrada

```bash
3^2
```

Salida

```bash
Hubo un error lexico...
```

Entrada

```bash
*3
```

Salida

```bash
Hubo un error sintactico...
```

## Streamlit

Se puede acceder a la aplicación web en el siguiente [enlace](https://marioteran56-parser-app-nub83r.streamlit.app/).

