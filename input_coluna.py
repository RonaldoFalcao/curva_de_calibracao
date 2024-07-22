import streamlit as st

c1, c2= st.columns(2)

a = c1.number_input("Concentração (mg/L)")
b = c2.number_input("Absorbância (adimensional)")

#st.write(a, b)

