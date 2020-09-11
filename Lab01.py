import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
import time

st.title('Graph Tool')
st.text('Python Version')

animation = st.sidebar.button('Animate')
Graph = st.empty()

if animation:
    x = np.arange(0,np.pi*2, 0.1)
    y = np.sin(x)
    frames = 10
    a = 10
    dif = a/frames
    b = 1
    for i in range(frames):
        plt.plot(x,y)
        plt.plot(x,y*b)
        b += dif
        Graph.pyplot()
        time.sleep(0.5)
        #plt.ylim
        #plt.xlim

Graph2 = st.empty()

imp = np.ones(5)

plt.stem(imp, use_line_collection=True)
        
Graph2.pyplot()
