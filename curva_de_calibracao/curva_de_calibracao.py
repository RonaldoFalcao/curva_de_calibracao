import streamlit as st
import numpy as np
import matplotlib.pylab as plb
import statsmodels.api as sm
import pandas as pd
import seaborn as sb
from PIL import Image

plb.style.use('default')
plb.rc('axes', titlesize=10)

if 'X' not in st.session_state:
    st.session_state.X = []
if 'Y' not in st.session_state:
    st.session_state.Y = [] 

if 'absorbancia' not in st.session_state:
    st.session_state.absorbancia = []

figura1 = Image.open('figures/ifrnead.jpg') 
figura2 = Image.open('figures/tsi.jpg')  

col1, col2 = st.columns(2, gap = 'large')

with col1:
    st.image(figura1)
with col2:
    st.image(figura2) 
st.divider()

st.title('Calculadora de curva de calibração')
st.subheader('Construa a sua curva de calibração usando uma regressão linear simples (MRLS), a partir de dados de leituras de absorbâncias de soluções da substância X em diferentes concentrações (na unidade de concentração adequada (U.C.)).')
st.write('')
st.subheader('Inserir as concentrações e absorbâncias obtidas das soluções usadas para curva de calibração.')
st.write('')

c1, c2 = st.columns(2)
novoX = c1.number_input("Concentração (U.C.)", key=1, placeholder="Ex: 10.00")
novoY = c2.number_input("Absorbância (adimensional)", key=2, placeholder="Ex: 0.525")
if st.button('Adicionar novo par de dados', key=3):
    st.session_state.X.append(novoX)
    st.session_state.Y.append(novoY)
st.write(pd.DataFrame({
    'Concentrações': st.session_state.X,
    'Absorbâncias': st.session_state.Y,
}))
st.subheader('Agora insira os valores de absorbâncias obtidos das leituras de suas amostras, para encontrar a concentração do analito.')
nova_absorbancia = st.number_input("Absorbância da amostra", key=4, placeholder="Ex: 0.500")
if st.button('Adicionar absorbâncias', key=5):
    st.session_state.absorbancia.append(nova_absorbancia)
st.write(pd.DataFrame({
    'Absorbâncias das amostras': st.session_state.absorbancia,
}))   

x = np.array(st.session_state.X)
y = np.array(st.session_state.Y)

if st.button("Rodar modelo!", key= 6, type="primary"):

    modelo = sm.OLS(y, sm.add_constant(x)).fit()
    print(modelo.summary())
    st.write(modelo.summary())
    
    a, b = np.polyfit(x, y, 1)
   
    y_est = a * x + b
    
    fig1, ax1 = plb.subplots()
    ax1= plb.scatter(x,y)
    ax1= plb.xlabel('Concentração (U.C.)', fontsize=10, labelpad=7)
    ax1= plb.ylabel('Absorbância (adimensional)', fontsize=10, labelpad=7) 

    ax2= plb.plot(x, y_est, '-', color='red')
    st.pyplot(fig1)

    st.subheader(f'Os coeficientes da equação de reta y= ax + b são a = {a:.3f}  e b = {b:.3f}.')
    st.subheader('A concentração média, o desvio-padrão e o coeficiente de variação da amostra são:')
    if len(st.session_state.absorbancia) == 1:
        concentracao = (st.session_state.absorbancia[0]-b)/a
        
        st.subheader(f'Com base em uma única leitura de absorbância, a concentração de seu analito é {concentracao:.2f} U.C.')
    
    elif len(st.session_state.absorbancia) >= 1:
            
        concentracoes = [((absorbancia - b) / a) for absorbancia in st.session_state.absorbancia]

        media_concentracao = np.mean(concentracoes)
        desvio_padrao_amostral = np.std(concentracoes, ddof=1) 
        coeficiente_variacao = (desvio_padrao_amostral / media_concentracao) * 100

        st.subheader(f'A concentração média é {media_concentracao:.2f} U.C.')
        st.subheader(f'O desvio-padrão amostral é {desvio_padrao_amostral:.2f} U.C.')
        st.subheader(f'O coeficiente de variação é {coeficiente_variacao:.2f}%.')
        
else:
    st.write("Inserir os dados de concentração e absorbância.")

st.divider()
st.text('Criado por Ronaldo Falcão Filho - Usando Python com a biblioteca Streamlit.')




