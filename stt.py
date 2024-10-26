import streamlit as st
import pandas as pd
import pickle
st.title ('iris prediction')
st.write('myy first app')
sl=float(st.number_input('enter sepal length'))
sw=float(st.number_input('enter sepal width'))
pl=float(st.number_input('enter petal length'))
pw=float(st.number_input('enter petall width'))
if st.button ('Predict?'):
    st.write('processing')
    st.write('please build your logic here')
    with open('model.pkl','rb') as models:
        pred_model=pickle.load(models)
    predictive_value= pred_model.predict([[sl,sw,pl,pw]])
    st.write(f'predicted value is {predictive_value}')