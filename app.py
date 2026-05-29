
import streamlit as st


st.set_page_config(
    page_title="Palettier | Your Colors, Curated",
    layout="wide"  
)


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right, darkblue, royalblue);
        background-attachment: fixed;
        padding: 3rem;
    }

    h1 {
        font-family: 'Playfair Display', serif;
        font-size: 4rem !important;
        text-align: center;
        color: #fffaf0;
        margin-bottom: 0.3rem;
    }

    .fancy-subtext {
        font-size: 1.5rem;
        text-align: center;
        color: #ffe;
        font-style: italic;
        margin-bottom: 3rem;
    }

    .centered-text {
        max-width: 800px;
        margin: auto;
        font-size: 1.2rem;
        line-height: 1.8;
        text-align: center;
        color: #f5f5f5;
    }

    div.stButton > button {
        background-color: #f5d742;
        color: black;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #ff1493;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1>Palettier</h1>", unsafe_allow_html=True)
st.markdown("<div class='fancy-subtext'>Your Colors, Curated.</div>", unsafe_allow_html=True)

st.markdown("""
<div class="centered-text">
    Palettier reveals the <strong>colors that make you glow</strong> — not just suit you.  
    <br><br>
    Through subtle undertones and precise analysis, we craft a palette that:
    <ul style="text-align: left; display: inline-block;">
        <li><strong>Flatters effortlessly</strong> – No more guessing what works</li>
        <li><strong>Boosts confidence</strong> – Wear shades that feel <em>like you</em></li>
        <li><strong>Feels bespoke</strong> – Like a couture dress for your complexion</li>
    </ul>
    <em>"Your Colors, Curated."</em>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Begin Your Color Journey"):
        st.switch_page("pages/analysis.py")

st.markdown("---")
