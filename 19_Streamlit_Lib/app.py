import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mlt

# Title of App
st.title('Hello Stramlit !!')
# To run ----> stramlit run app.py

st.write('Hey there this is a simple text')

# Creation of a dataframe

df=pd.DataFrame({
    'first column':[1,2,3,4,5],
    'second column':[11,22,33,44,55]
})

st.write(df)

# Linechart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)
