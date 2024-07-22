import streamlit as st
import numpy as np
import matplotlib.pylab as plb
import statsmodels.api as sm
plb.style.use('default')
plb.rc('axes', titlesize=10)

st.title('Meu primeiro app com Streamlit.')
st.header('Vamos aprender mais sobre essa ferramenta fantástica.')
st.write('Como exemplo inicial criaremos um regressão linear simples (MRLS), a partir de dados de leituras\n de absorbâncias de soluções da substância X em diferentes concentrações.')
st.write('')
st.subheader('Inserir as concentrações e absorbâncias obtidas das 5 soluções usadas para curva de calibração, em mg/L.')
st.write('')

c1, c2= st.columns(2)
conc1 = c1.number_input("Concentração (mg/L)", key=1)
Abs1 = c2.number_input("Absorbância (adimensional)", key=2)
conc2 = c1.number_input('',key=3)
Abs2 = c2.number_input('',key=4)
conc3 = c1.number_input('',key=5)
Abs3 = c2.number_input('',key=6)
conc4 = c1.number_input('',key=7)
Abs4 = c2.number_input('',key=8)
conc5 = c1.number_input('',key=9)
Abs5 = c2.number_input('',key=10)

X = np.array([conc1,conc2,conc3,conc4,conc5])
Y = np.array([Abs1,Abs2,Abs3,Abs4,Abs5])

st.button("Reset", type="primary")
if st.button("Rodar modelo!"):

    modelo = sm.OLS(Y, sm.add_constant(X)).fit()
    print(modelo.summary())
    st.write(modelo.summary())
    
    a, b = np.polyfit(X, Y, 1)
   
    y_est = a * X + b
    
    fig1, ax1 = plb.subplots()
    ax1= plb.scatter(X,Y)
    ax1= plb.xlabel('Concentração (mg/L)', fontsize=10, labelpad=7)
    ax1= plb.ylabel('Absorbância (adimensional)', fontsize=10, labelpad=7) 

    ax2= plb.plot(X, y_est, '-', color='red')
    st.pyplot(fig1)

    st.write(f'A equação que representa a curva de calibração é Abs = {a:.3f}xC + {b:.3f}')
else:
    st.write("Inserir os dados de concentração e absorbância.")










