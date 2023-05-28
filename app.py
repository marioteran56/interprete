import streamlit as st
from interprete import interprete

st.title('Pequeño Interprete')
st.subheader('Tercer Parcial')
st.markdown('''
Implementar un pequeño intérprete en el lenguaje de programación de Python, el cual pueda realizar expresiones matemáticas simples, las cuales son la suma, resta, multiplicación, división y el uso de paréntesis dentro de la expresión.

La siguiente gramática aumentada está definida de la siguiente manera:

$$
𝐺 = \{\{𝑛𝑢𝑚𝑒, +, −, ∗, /, (, ), \$, 𝑒𝑜𝑙\}, \{𝑆, 𝐸, 𝑇 , 𝐹\}, 𝑆, 𝑃 \}
$$

La siguiente expresión seria de la siguiente manera:

$$
𝑃 = \{𝑆 → 𝐸 𝑒𝑜𝑙 𝐸 → 𝐸 + 𝑇 |𝐸 − 𝑇 |𝑇 𝑇 → 𝑇 ∗ 𝐹|𝑇 /𝐹|𝐹 𝐹 → (𝐸)|𝑛𝑢𝑚𝑒\}
$$
''')

st.header('Interprete')
cadena = st.text_input('Ingrese una expresión aritmética:')

if st.button('Ingresar'):
    resultado = interprete(cadena)
    st.text(f'Resultado: {resultado}')

    