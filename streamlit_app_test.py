import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Quete : Streamlit : build and share data apps')

st.write("Data:")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars= pd.read_csv(link)
st.write(df_cars)

st.write("Matrice de correlation:")

viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
								annot=True)								

st.pyplot(viz_correlation.figure, clear_figure=True)


st.write("Répartition des modèles de voitures par continent")
histplot = sns.histplot(data=df_cars, x='continent', stat="count")
st.pyplot(histplot.figure, clear_figure=True)

st.write("Poids / année")
barplotPoids = sns.barplot(data=df_cars, x = 'year', y = 'weightlbs', color = 'blue')
st.pyplot(barplotPoids.figure, clear_figure=True)

st.write("Evolution de la consommation:")
barplotConso = sns.barplot(data=df_cars, x = 'year', y = 'mpg', color = 'blue',)
st.pyplot(barplotConso.figure, clear_figure=True)


st.write("test:")
clist = df_cars["continent"].unique().tolist()

continents = st.multiselect("Select continent", clist)
st.header("You selected: {}".format(", ".join(continents)))

dfs = {continent: df[df["continent"] == continent] for continent in continents}

barplot2 = plt.show()
for continent, df in dfs.items():
    barplotPoids2 = sns.barplot(data=df_cars, x = 'year', y = 'weightlbs', color = 'blue')
st.pyplot(barplotPoids2.figure
          , clear_figure=True
          )

#nbre de voiture par continent
#poids moyen par année (+continent en filtre)
#consommation (mpg miles per gallon) selon l'année (+continent)

#creer repo dans github... mettre les deux fichiers + https://share.streamlit.io/