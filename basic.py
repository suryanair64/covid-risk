#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


# In[4]:


st.title("Covid Risk Prediction")


# In[5]:


pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)


# In[11]:


Name = st.text_input("Name:")
Age= st.number_input("Age(ABOVE 18):")
Sex= st.text_input("Sex(MALE 1 & FEMALE 0):")
BMI=st.number_input("BMI:")
st.header("CLINICAL INFORMATION")
st.write("TYPE 1 IF YOU ARE CURRENTLY SUFFERING FROM ANY OF THESE CORMOBIDITIES ")
Diabetes=st.number_input("Diabetes:")
Cardio_Vascular_Diseases=st.number_input("Cardio Vascular Diseases:")
Sickle_cell_diesases=st.number_input("Sickle cell diesases:")
Immuno_deficiency_diseases=st.number_input("Immuno deficiency diseases:")
Down_syndrome=st.number_input("Down syndrome:")
Cancer=st.number_input("Cancer:")
Chronic_Respiratory_disease=st.number_input("Chronic Respiratory disease:")
Hypertension=st.number_input("Hypertension:")
st.header("VACCINATION STATUS")
st.write("TYPE 1 IF YOU HAVE NOT VACCINATED")
Vaccinated=st.number_input("Not Vaccinated:")
submit = st.button("Predict Risk")


# In[14]:


if submit:
        prediction = classifier.predict([[Age,Sex,BMI,Diabetes,Cardio_Vascular_Diseases,Sickle_cell_diesases,Immuno_deficiency_diseases,Down_syndrome,Cancer,Chronic_Respiratory_disease,Hypertension,Vaccinated]])
        if prediction == 0:
            st.write(Name,'You are under Low risk of affecting Corona.Recommended preventive measures include social distancing, wearing face masks in public, ventilation and air-filtering, hand washing,covering mouth when sneezing or coughing, disinfecting surfaces, and monitoring and self-isolation for people exposed or symptomatic')
        else:
            st.write(Name," we are really sorry to say but it seems like You are under High risk of affecting Corona. Recommended preventive measures include social distancing, wearing face masks in public, ventilation and air-filtering, hand washing,covering mouth when sneezing or coughing, disinfecting surfaces, and monitoring and self-isolation for people exposed or symptomatic")

