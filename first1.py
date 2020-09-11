import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

#He agregado un nuevo comentario

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
slider1 = st.sidebar.slider("amplitud",min_value=0, max_value=10, value=1, step=1)
frecuencia = st.sidebar.number_input("frecuencia", min_value=0.0, max_value=20.0, value=1.0, step=0.1)

user = st.sidebar.selectbox("Selecciona una funcion",["coseno","seno"], index=0)
user2 = st.sidebar.selectbox("Selecciona una funcion2",["coseno","seno"], index=0)

if user=="coseno":
    x = np.arange(0, 2*np.pi, 0.0001)
    y = slider1*np.cos(x*frecuencia)
    ax2.plot(x,y)

if user=="seno":
    x = np.arange(0, 2*np.pi, 0.0001)
    y = slider1*np.sin(x*frecuencia)
    ax2.plot(x,y)

if user2 == "seno":
    x = np.arange(0, 2*np.pi, 0.0001)
    y = slider1*np.sin(x*frecuencia)
    ax1.clear()
    ax1.plot(x,y)

if user2 == "coseno":
    x = np.arange(0, 2*np.pi, 0.0001)
    y = slider1*np.cos(x*frecuencia)
    ax1.clear()
    ax1.plot(x,y)

st.pyplot()



fig, ax = plt.subplots()

max_x = 5
max_rand = 10
min_x = 0
min_rand = 0

x = np.arange(min_x, max_x)
ax.set_ylim(min_rand, max_rand)
line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
the_plot = st.pyplot(plt)

def init():  # give a clean slate to start
    line.set_ydata([np.nan] * len(x))

def animate(i):  # update the y values (every 1000ms)
    line.set_ydata(np.random.randint(0, max_rand, max_x))
    the_plot.pyplot(plt)

init()
for i in range(100):
    animate(i)
    time.sleep(1)