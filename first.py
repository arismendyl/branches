import streamlit as st
import numpy as np
import matplotlib.pyplot as plot


st.title("Hello world")

st.header("Header")

st.subheader("Subheader")

st.text("this is text")

op = st.selectbox("Select a function", ["seno","coseno"], index=0)
amp = st.number_input("amplitud", min_value=1, max_value=20, value= 1, step =1)
v1 = st.slider("frecuencia", min_value=1, max_value=20, value= 5, step =1)

if op=="seno":
    time = np.arange(0, 5*np.pi, 0.001)
    amplitude = amp*np.sin(v1*time)
    name = "Sine wave"
    yname = "Amplitude = sin(time)"
elif op=="coseno":
    time = np.arange(0, 5*np.pi, 0.001)
    amplitude = amp*np.cos(v1*time)
    name = "Cosine wave"
    yname = "Amplitude = cos(time)"

# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(time, amplitude)

# Give a title for the sine wave plot

plot.title(name)

# Give x axis label for the sine wave plot

plot.xlabel('Time')

# Give y axis label for the sine wave plot

plot.ylabel(yname)
plot.grid(True, which='both') 
plot.axhline(y=0, color='k')
st.pyplot()