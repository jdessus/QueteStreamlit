import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Quete : Streamlit : build and share data apps')

st.write("But de la quête : faire une analyse de corrélation et de distribution grâce à différents graphiques a partir d'un dataset sur les voitures.")

st.header("Data:")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars= pd.read_csv(link)

# Create a list of possible values and multiselect menu with them in it.
continents = df_cars['continent'].unique()
continents_selected = st.multiselect('Choix du (des) continent(s) / pays:', continents
	, default=continents
	)

# Mask to filter dataframe
mask_continents = df_cars['continent'].isin(continents_selected)

df_cars = df_cars[mask_continents]



st.write(df_cars)


st.header("Matrice de correlation:")

viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
								annot=True)								

st.pyplot(viz_correlation.figure, clear_figure=True)

st.write("la matrice de corrélation permet d'évaluer la dépendence entre plusieurs variables en même temps. On voit ici, la forte dépendance entre le poids (Weight) et la puissance de la voiture (hp)")

st.header("\nRépartition des modèles de voitures par continent")
histplot = sns.histplot(data=df_cars, x='continent', stat="count")
st.pyplot(histplot.figure, clear_figure=True)

st.write("Les modèles de voiture des US sont les plus présent dans ce dataset")

st.header("Poids / année")
barplotPoids = sns.barplot(data=df_cars, x = 'year', y = 'weightlbs', color = 'blue')
st.pyplot(barplotPoids.figure, clear_figure=True)

col1, col2 = st.columns(2)

with col1:
	st.header("Evolution de la consommation:")
	barplotConso = sns.barplot(data=df_cars, x = 'year', y = 'mpg', color = 'blue',)
	st.pyplot(barplotConso.figure, clear_figure=True)

with col2:
	st.header("Evolution des chevaux fiscaux:")
	barplotHp= sns.barplot(data=df_cars, x = 'year', y = 'hp', color = 'blue',)
	st.pyplot(barplotHp.figure, clear_figure=True)

