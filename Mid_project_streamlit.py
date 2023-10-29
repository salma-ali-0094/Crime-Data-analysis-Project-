import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import plotly.graph_objects as go

st.set_page_config(layout='wide',
                  page_title = 'Chicago Crime')

st.title('Chicago Crime')
st.header('A 2001 - 2023 Analysis')


tab1, tab2 = st.tabs(['Over all Macros', 'Time series analysis'])
df=pd.read_csv('cleaned_Chicago_crime_3')
num = df.describe()
cat = df.describe(include = 'O')
dataf= df.head(5)

