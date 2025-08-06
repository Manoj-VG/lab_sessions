import streamlit as st
import pandas as pd
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("Hi")

df = pd.read_csv("/Users/manojvg/Documents/GitHub/lab_sessions/cars24-car-price.csv")

st.write(df)

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")