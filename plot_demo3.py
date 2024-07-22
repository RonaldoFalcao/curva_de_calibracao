import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pylab as plb
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
from statsmodels.graphics.gofplots import ProbPlot
plb.style.use('default')
plb.rc('axes', titlesize=10)

st.title('Meu primeiro app com Streamlit.')
st.header('Vamos aprender mais sobre essa ferramenta fantástica.')
st.write('Como exemplo inicial criaremos um regressão linear simples (MRLS), a partir de dados de leituras\n de absorbâncias de soluções da substância X em diferentes concentrações.')
st.write('')
st.subheader('Inserir as concentrações das 5 soluções usadas para curva de calibração, em mg/L.')
st.write('')
number1 = st.number_input(label='C (mg/L)', key=1, value=None, placeholder="Concentração 1 ")
st.write("A concentração é ", number1,"mg/L.")
number2 = st.number_input(label='C (mg/L)',key=2, value=None, placeholder="Concentração 1 ")
st.write("A concentração é ", number2,"mg/L.")
number3 = st.number_input(label='C (mg/L)',key=3, value=None, placeholder="Concentração 1 ")
st.write("A concentração é ", number3,"mg/L.")
number4 = st.number_input(label='C (mg/L)',key=4, value=None, placeholder="Concentração 1 ")
st.write("A concentração é ", number4,"mg/L.")
number5 = st.number_input(label='C (mg/L)',key=5, value=None, placeholder="Concentração 1 ")
st.write("A concentração é ", number5,"mg/L.")
st.write('')
st.subheader('Inserir as absorbâncias lidas de cada solução.')
st.write('')
number6 = st.number_input(label='Abs',key=6, value=None, placeholder="Absorbância 1 ")
st.write("A absorbância 1 é ", number6)
number7 = st.number_input(label='Abs',key=7, value=None, placeholder="Absorbância 2 ")
st.write("A absorbância 2 é ", number7)
number8 = st.number_input(label='Abs',key=8, value=None, placeholder="Absorbância 3 ")
st.write("A absorbância 3 é ", number8)
number9 = st.number_input(label='Abs',key=9, value=None, placeholder="Absorbância 4 ")
st.write("A absorbância 4 é ", number9)
number10 = st.number_input(label='Abs',key=10, value=None, placeholder="Absorbância 5 ")
st.write("A absorbância 5 é ", number10)

X = np.array([number1,number2,number3,number4,number5])
Y = np.array([number6,number7,number8,number9,number10])
st.button("Reset", type="primary")
if st.button("Rodar modelo!"):

    modelo = sm.OLS(Y, sm.add_constant(X)).fit()
    print(modelo.summary())
    st.write(modelo.summary())

    fig1, ax1 = plb.subplots()
    ax1= plb.figure(figsize=(8, 4))
    ax1= plb.scatter(X,Y)
    st.pyplot(fig1)
    fig2, ax2 = plb.subplots()
    ax2 = plb.plot(X, modelo.predict(), color="r")
    plb.xlabel("Patrocínio (Milhões de Meticais)")
    plb.ylabel("Receita (Mil Milhões de Meticais)")
    st.pyplot(ax2)
    #fig1, ax1 = plb.subplots()
    #ax1= plb.figure(figsize=(8, 4))
    #ax1 = plb.scatter(X,Y)
    #st.pyplot(fig1)
    #fig2, ax2 = plb.subplots()
    #ax2 = plb.plot(X, modelo.predict(), color="r")
    #st.pyplot(ax2)
else:
    st.write("Inserir os dados de concentração e absorbância.")









