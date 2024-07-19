import streamlit as st
import numpy as np
import matplotlib.pylab as plb
import statsmodels.api as sm
import pandas as pd
import seaborn as sb

plb.style.use('default')
plb.rc('axes', titlesize=10)

if 'X' not in st.session_state:
    st.session_state.X = []
if 'Y' not in st.session_state:
    st.session_state.Y = [] 
    
col1, col2 = st.columns(2, gap = 'large')

with col1:

    st.image("C:/Users/Ronaldo/Documents/ifrnead.jpg")

with col2:

    st.image("C:/Users/Ronaldo/Documents/tsi.jpg")
st.divider()

st.title('Calculadora de curva de calibração')
st.subheader('Como exemplo inicial criaremos um regressão linear simples (MRLS), a partir de dados de leituras de absorbâncias de soluções da substância X em diferentes concentrações.')
st.write('')
st.subheader('Inserir as concentrações e absorbâncias obtidas das soluções usadas para curva de calibração.')
st.write('')

c1, c2 = st.columns(2)
novoX = c1.number_input("Concentração (mg/L)", key=1)
novoY = c2.number_input("Absorbância (adimensional)", key=2)
if st.button('Adicionar novo par de dados'):
    st.session_state.X.append(novoX)
    st.session_state.Y.append(novoY)
st.write(pd.DataFrame({
    'Concentrações': st.session_state.X,
    'Absorbâncias': st.session_state.Y,
}))

x = np.array(st.session_state.X)
y = np.array(st.session_state.Y)
st.button("Reset", type="primary")
if st.button("Rodar modelo!"):

    modelo = sm.OLS(y, sm.add_constant(x)).fit()
    print(modelo.summary())
    st.write(modelo.summary())
    
    a, b = np.polyfit(x, y, 1)
   
    y_est = a * x + b
    
    fig1, ax1 = plb.subplots()
    ax1= plb.scatter(x,y)
    ax1= plb.xlabel('Concentração (mg/L)', fontsize=10, labelpad=7)
    ax1= plb.ylabel('Absorbância (adimensional)', fontsize=10, labelpad=7) 

    ax2= plb.plot(x, y_est, '-', color='red')
    st.pyplot(fig1)

    st.subheader(f'A equação que representa a curva de calibração é Abs = {a:.3f}xC + {b:.3f}')
else:
    st.write("Inserir os dados de concentração e absorbância.")

st.divider()
st.text('Criado por Ronaldo Falcão Filho - Usando Python com a biblioteca Streamlit.')




