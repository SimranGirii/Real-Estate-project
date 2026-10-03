import streamlit as st
import pickle
from pathlib import Path

import ui_theme

# Page configuration (moved to the top: it must come before other Streamlit calls)
st.set_page_config(page_title="Real Estate App", page_icon="🏠", layout="wide")
ui_theme.apply_theme()

# Locate the application directory
BASE_DIR = Path(__file__).resolve().parent

# Locate the saved ML pipeline
pipeline_path = BASE_DIR / "pipeline.pkl"

# ---- Hero ----
# (The original had two stacked titles. Both texts are kept: the app name is the
#  title, "Real Estate Price Prediction" is the tagline.)
st.title("🏠 Real Estate App")
st.subheader("Real Estate Price Prediction")
st.write("Use the pages in the sidebar: **Price Predictor**, **Analytics** and **Recommender**.")



# ---- What each page does ----

# First row
col_predict, col_analytics = st.columns(2, gap="large")

with col_predict:
    with st.container(key="tile-predictor"):
        ui_theme.card_title("Price Predictor")
        ui_theme.tile_text(
            "Describe a flat or house and get an estimated price range in crore rupees."
        )

with col_analytics:
    with st.container(key="tile-analytics"):
        ui_theme.card_title("Analytics")
        ui_theme.tile_text(
            "Explore property prices, area trends, BHK distributions, maps and other visualizations."
        )

# Space between rows
st.write("")

# Second row - full width
with st.container(key="tile-recommender"):
    ui_theme.card_title("Apartment Recommender")
    ui_theme.tile_text(
        "Find apartments based on location and property features using our recommendation system."
    )