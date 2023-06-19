import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

#titulo en color naranja
st.markdown('<h2 style="font-size: 18px;">UF6 Actividad Integradora</h2>', unsafe_allow_html=True)
st.markdown('María Fernanda Martínez A01067198')


st.markdown(
    f'<h1 style="color:#F94A25;">Police Incidents Reports from 2018 to 2020 in San Francisco</h1>',
    unsafe_allow_html=True
)

df=pd.read_csv('Police_Department_Incident_Reports.csv')
st.dataframe (df)

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution. :)')

mapa=pd.DataFrame()
mapa['Date']=df['Incident Date']
mapa['Day']=df['Incident Day of Week']
mapa['Incident Year'] = df['Incident Year']
mapa['Police District']=df['Police District']
mapa['Neighborhood']= df['Analysis Neighborhood']
mapa['Incident Category']=df['Incident Category']
mapa['Incident Subcategory']=df['Incident Subcategory']
mapa['Resolution']=df['Resolution']
mapa['lat']=df['Latitude']
mapa['lon']=df['Longitude']
mapa['Report Type']=df['Report Type Description']
mapa=mapa.dropna()

subset_data2 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
    subset_data2 = mapa[mapa['Police District'].isin(police_district_input)]

subset_data1 = subset_data2
neighborhood_input = st.sidebar.multiselect(
'Neighborhood',
subset_data2.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(neighborhood_input) > 0:
    subset_data1 = subset_data2[subset_data2['Neighborhood'].isin(neighborhood_input)]

subset_data = subset_data1
incident_input = st.sidebar.multiselect(
'Incident Category',
subset_data1.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())
if len(incident_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Category'].isin(incident_input)]
            
subset_data

#grafica 1
st.markdown('It is important to mention that any police district can answer to any incident, the neighborhood in which it happened is not related to the police district.')
st.markdown('### **Crime locations in San Francisco:police_car:**') #emoji 'police car'
st.map(subset_data)

#grafica 2
st.markdown('### **Crimes ocurred per day of the week**')
st.bar_chart(subset_data['Day'].value_counts())

#grafica 3 (cambio el tipo de gráfica)
st.markdown('### **Crimes ocurred per date**')
#st.line_chart(subset_data['Date'].value_counts())
st.area_chart(subset_data['Date'].value_counts())

#grafica nueva
st.markdown('### **Total crimes ocurred per year**')
st.bar_chart(subset_data['Incident Year'].value_counts())

#gráfica 4
st.markdown('### **Type of crisis commited**')
st.bar_chart(subset_data['Incident Category'].value_counts())

agree = st.button('Click to see Incident Subcategories')
if agree:
  st.markdown('### **Subtype of crimes committed**')
  st.bar_chart(subset_data['Incident Subcategory'].value_counts())
  
#grafica nueva 2
st.markdown('### **Report Type Description**')
fig2, ax2=plt.subplots()
labels=subset_data['Report Type'].unique()
ax2.pie(subset_data['Report Type'].value_counts(),labels=labels,autopct='%1.1f%%',startangle=20)
st.pyplot(fig2)

#grafica 5 con boton para su visualización
agree = st.button('Click to see Resolution Status')
if agree:
    st.markdown('### **Resolution status**')
    fig1, ax1=plt.subplots()
    labels=subset_data['Resolution'].unique()
    ax1.pie(subset_data['Resolution'].value_counts(),labels=labels,autopct='%1.1f%%',startangle=20)
    st.pyplot(fig1)




