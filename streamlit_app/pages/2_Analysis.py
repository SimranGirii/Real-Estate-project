import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parents[1]

st.set_page_config(page_title="Analysis Pipeline")
st.title("Analytics")

#Geomap
new_df = pd.read_csv('notebooks/data_viz1.csv')

group_df = new_df.groupby('sector')[[
    'price','price_per_sqft', 'built_up_area', 'latitude', 'longitude'
    ]].mean().reset_index()

fig = px.scatter_mapbox(group_df,
                     lat="latitude",
                     lon="longitude",
                     color="price_per_sqft",
                     size='built_up_area',
                     color_continuous_scale=px.colors.cyclical.IceFire,
                     zoom=10,
                     mapbox_style="open-street-map",
                     width=1200,
                     height=700,
                     hover_name="sector")

st.plotly_chart(fig, use_container_width=True)


# WordCloud
st.subheader("Property Features WordCloud")

feature_text_path = BASE_DIR / "feature_text.pkl"

with open(feature_text_path, "rb") as file:
    feature_text = pickle.load(file)

wordcloud = WordCloud(
    width=800,
    height=500,
    background_color="white",
    stopwords=set(["s"]),
    min_font_size=10
).generate(feature_text)

fig_wc, ax = plt.subplots(figsize=(10, 6))

ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")

st.pyplot(fig_wc)

#scatterplot
st.subheader("Area VS Price")

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
        fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price",
        color="bedRoom", title="Area Vs Price")
        st.plotly_chart(fig1, use_container_width=True)

else:
        fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price",
        color="bedRoom",
        title="Area Vs Price")

        st.plotly_chart(fig1, use_container_width=True)

fig1 = px.scatter(new_df, x="built_up_area", y="price", color="bedRoom", title = "Area Vs Price")

#piechart
st.subheader("BHK PieChart")

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

        fig2 = px.pie(new_df, names='bedRoom')

        st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

#Boxplot
st.subheader('Side by Side BHK price comparision')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


# Distplot
st.subheader('Side by Side Distplot for Property Type')

fig4, ax = plt.subplots(figsize=(10, 4))

sns.histplot(
    new_df[new_df['property_type'] == 'house']['price'],
    kde=True,
    stat='density',
    label='House',
    ax=ax
)

sns.histplot(
    new_df[new_df['property_type'] == 'flat']['price'],
    kde=True,
    stat='density',
    label='Flat',
    ax=ax
)

ax.legend()

st.pyplot(fig4)