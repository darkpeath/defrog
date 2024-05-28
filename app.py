"""
main page
"""

import pandas as pd
import streamlit as st

st.set_page_config(page_title='DEFROG')

st.text("Welcome to DEFROG.")

data = pd.DataFrame([
    ['a1', 1, 'tom'],
    ['a2', 5, 'bob'],
    ['b2', 7, 'tom'],
    ['a5', 3, 'alice'],
    ['a7', 4, 'bob'],
    ['c3', 5, 'tom'],
    ['b4', 2, 'alice'],
], columns=['id', 'value', 'name'])

if st.checkbox('filter'):
    option = st.selectbox('name', data['name'])
    data = data[data['name'] == option]

st.dataframe(data, hide_index=True)
