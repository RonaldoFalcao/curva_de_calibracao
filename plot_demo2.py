import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

p = st.slider("propabilidade de sucesso (p).", min_value=0.0, max_value=1.0, value=0.0, step=0.05)
binom_dist = np.random.binomial(1, p, 1000)

list_of_means = []
for i in range(0, 1000):
     list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means)
st.pyplot(fig1)

