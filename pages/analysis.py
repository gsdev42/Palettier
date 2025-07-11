import streamlit as st
import pandas as pd
import joblib
import sys
import os
import logging

from model.color_model import ColorSeasonModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    model = ColorSeasonModel.load_model("model.pkl")
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()


st.set_page_config(
    page_title="Color Analysis",
    page_icon="🔍",
    layout="centered"
)

st.title("Color Season Analysis")
st.write("Tell us about your natural coloring:")

with st.form("analysis_form"):
    col1, col2 = st.columns(2)

    with col1:
        undertone = st.selectbox(
            "Skin undertone",
            ['warm', 'cool', 'neutral-warm', 'neutral-cool'],
            help="Warm = golden/yellow, Cool = pink/blue"
        )

        saturation = st.selectbox(
            "Color saturation",
            ['bright', 'muted'],
            help="Bright = clear/vivid, Muted = soft/grayish"
        )

    with col2:
        hair_color = st.selectbox(
            "Natural hair color",
            ['golden_blonde', 'ash_blonde', 'auburn', 'black', 'red', 
             'light_brown', 'dark_brown', 'medium_brown', 'ash_brown', 'light_blonde']
        )

        eye_color = st.selectbox(
            "Eye color",
            ['brown', 'blue', 'green', 'gray', 'hazel']
        )

    submitted = st.form_submit_button("Analyze My Colors")


if submitted:
  
    user_input = {
        'undertone': undertone,
        'hair_color': hair_color, 
        'eye_color': eye_color,
        'saturation': saturation
    }

    try:
   
        season = model.predict(user_input)

     
        st.success(f"### Your color season is: {season}")

        # Season descriptions
        season_descriptions = {
                    "True Spring": "Warm and bright colors that mirror spring's fresh blooms",
                    "True Summer": "Cool and muted tones like a summer beach at dusk",
                    "Soft Autumn": "Muted and warm colors, reminiscent of autumn leaves",
                    "True Winter": "Cool and bright colors, like a winter landscape",
                    "Light Summer": "Light and cool colors reminiscent of a summer morning",
                    "Bright Spring": "Warm and vibrant colors full of energy",
                    "True Autumn": "Rich, warm earth tones like autumn foliage",
                    "Dark Winter": "Deep, cool colors with high contrast",
                    "Light Spring": "Light, warm colors with a delicate brightness",
                    "Bright Winter": "Clear, cool colors with high intensity",
                    "Dark Autumn": "Deep, warm colors with rich saturation",
                    "Soft Summer": "Soft, cool colors with muted elegance"
                }

        st.write(season_descriptions.get(season, "Season description coming soon!"))
        st.balloons()

    except Exception as e:
        st.error(f"Error during analysis: {str(e)}")

st.divider()
if st.button("← Back to Home"):
    st.switch_page("app.py")