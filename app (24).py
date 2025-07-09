
import streamlit as st
import pandas as pd
import joblib
import random

# 🎯 Load model, encoder and data
model = joblib.load("mood_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
songs_df = pd.read_csv("songs.csv")

st.set_page_config(page_title="🎵 Mood-Based Song Recommender", layout="centered")
st.title("🎧 Mood-Based Song Recommender")
st.markdown("Select your current mood to get a song suggestion! 💫")

# 🧠 Mood options from encoder
mood_options = list(label_encoder.classes_)
selected_mood = st.selectbox("How are you feeling today? 😊", mood_options)

if st.button("Recommend Me a Song 🎶"):
    # 🔍 Filter songs by mood
    filtered_songs = songs_df[songs_df['mood'] == selected_mood]
    if not filtered_songs.empty:
        song = filtered_songs.sample(1).iloc[0]
        st.success(f"**{song['track_name']}** by *{song['artist']}*")
    else:
        st.warning("No songs found for this mood. Try another!")
