


import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
#iniciar o código com streamlit
st.title('Distribuição Binomial')
#receber os valores de n, p e x
n = st.number_input('Valor de n:', min_value=0, max_value=1000)
p = st.number_input('Valor de p:', min_value=0.0, max_value=1.0)
x = st.number_input('Valor de x:', min_value=0, max_value=n)
#calcular a probabilidade de P(X=x) e P(X<=x)
probabilidade_p = binom.pmf(x, n, p)
probabilidade_p_ = binom.cdf(x, n, p)
#retornar o resultado em gráfico da distribuição binomial
x_values = np.arange(0, n+1)
y_values = binom.pmf(x_values, n, p)
fig, ax = plt.subplots()
ax.bar(x_values, y_values)
ax.set_xlabel('X')
ax.set_ylabel('P(X)')
st.pyplot(fig)
#mostrar o resultado
st.write(f'P(X={x}) = {probabilidade_p}')
st.write(f'P(X<={x}) = {probabilidade_p_}')

#executar o programa via linha de comando

