import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.linear_model import LinearRegression

#lets load pickle files- rb-"read binary", wb - "write binary"
model=pickle.load(open("mobilseprice.pkl","rb"))
dt=pickle.load(open("labeldictionary.pkl","rb"))

st.title("Smartphone Price Prediction")

#select drop down for "brand" user can select, use dictionary into pickle file to list the brand
brandname=st.selectbox("Choose your Brand",dt['Brand'])

#send index position
brandindex=dt['Brand'].tolist().index(brandname)

#select model column
modelname=st.selectbox("Choose your Model",dt['Model'])
modelindex=dt['Model'].tolist().index(modelname)

#incremental by 1, next of count year 2012(step=1)
year=st.number_input("Select Year",min_value=2015,max_value=2025,step=1)
original_price=st.number_input("Enter Original Price",min_value=10000,max_value=200000,step=1000)
months=st.number_input("Enter Usage Month",min_value=1,max_value=150,step=1)
#converting into integer-safer side
storage=st.selectbox("Select Storage",[64,128,256,512])
storage=int(storage)

ram=st.selectbox("Select RAM Size",[4,6,8,12,16,18])
ram=int(ram)

battery=st.number_input("Enter Battery health",min_value=0.0,max_value=100.0,step=0.1)
battery=int(battery)

condition=st.selectbox("Select Condition",dt['Condition'])
condnumber=dt['Condition'].tolist().index(condition)

warranty=st.selectbox("Phone is still in Warranty",dt['Warranty'])
warrantynumber=dt['Warranty'].tolist().index(warranty)

color=st.selectbox("Select color",dt['Color'])
colornumber= dt['Color'].tolist().index(color)

if st.button("Predict"):
    data=[[brandindex,modelindex,year,original_price,months,storage,ram,battery,condnumber,warrantynumber,colornumber]]

    res=model.predict(data)[0]
    st.write("Your Resell Value of your phone=",round(res,2))

# streamlit run appmob.py
#stop=ctr C






