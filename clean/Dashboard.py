import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# streamlit_dashboard_template.py
# Load your dataset
@st.cache_data

def load_data():
    df = pd.read_csv("Metadataset_with_genre.csv")
    df.columns = df.columns.str.lower().str.strip()
    return df

df = load_data()

# Apply dark background style
plt.style.use("dark_background")
sns.set_style("whitegrid")
plt.rcParams.update({
    "axes.facecolor": "#0E1117",
    "figure.facecolor": "#0E1117",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "text.color": "white",
    "grid.color": "#333333",
})

#1. Title & Intro

st.title("The AI Revolution in Music 🎧")
st.subheader("Streaming, Recommendations, and Listener Trends")
st.markdown(" ")
st.markdown("""
This dashboard explores how AI has influenced music trends, artist discovery, and engagement between **2000–2019** since its adaptation into streaming platforms.
The Data is split into:
- **Pre-AI** (2000–2015)
- **Post-AI** (2016–2019) --> AI emergence
""")

st.markdown(" ")
st.markdown(" ")

# 2. Dataset Overview
st.header("📰 Dataset Overview")
st.write("The music streaming revolution did not just change how we listen" \
        " — it changed what we listen to, and how music succeeds."
            " This dataset captures nearly two decades (2000–2019) of music trends"
            "during the critical shift from traditional discovery to AI-driven personalization."
            " Split into Pre-AI and Post-AI periods, the data reveals how artificial intelligence"
            "began to reshape engagement, genre popularity, and artist discovery long before it became a " \
            "mainstream headline.")
st.markdown("Explore the foundation behind the findings!")
st.markdown(" ")
with st.expander("**Basic Statistics:**"):
     st.write(df.describe())

st.markdown(" ")
st.markdown(" ")

with st.expander("**Song Count by Period:**"):
    st.markdown(" ")
    period_counts = df["period"].value_counts()
    st.bar_chart(period_counts)

st.markdown(" ")
st.markdown(" ")

with st.expander("**Song Count per Year:**"):
    st.markdown(" ")
    st.line_chart(df["year"].value_counts().sort_index())

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

st.write ("Streaming Platforms became a thing in the late 1990s," \
          " taking the entire music industry by a storm and creating better prospects"
          " and versatility for both current and aspiring artists. Especially aspiring artists who did not have enough means to break into the industry." \
          " For this exploration, three metrics are designed using research questions that would help measure, view and visualize the influence AI in the" \
          " earlier years of its integration into streaming platforms")

st.markdown(" ")

# 3. RQ1: Engagement Trends
st.header("🌟 Engagement with music over the years")
df_rq1 = df.dropna(subset=["popularity", "year", "period"])
yearly_popularity = df_rq1.groupby("year")["popularity"].mean().reset_index()
boxplot_data = df_rq1[["popularity", "period"]]
summary_stats = df_rq1.groupby("period")["popularity"].agg(["count", "mean", "median", "std", "min", "max"]).round(2)

fig1, ax1 = plt.subplots()
sns.lineplot(data=yearly_popularity, x="year", y="popularity", marker="o", color="cyan", ax=ax1)
ax1.set_title("Average Popularity by Year")
ax1.set_xlabel("Year")
ax1.set_ylabel("Popularity")
ax1.tick_params(colors="white")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.boxplot(data=boxplot_data, x="period", y="popularity", palette="pastel", ax=ax2)
ax2.set_title("Popularity by Period")
ax2.set_xlabel("Period")
ax2.set_ylabel("Popularity")
st.pyplot(fig2)

st.write("### Summary Of Statistics")
st.dataframe(summary_stats)

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

#  4. RQ2: Genre & Feature Trends
st.header("🎧 Genre & Song Feature Shifts (RQ2)")

st.markdown(" ")
st.markdown(" ")

# Genre Popularity by Period 
if "genre" in df.columns:
    genre_popularity = df.groupby(["genre", "period"]).size().unstack(fill_value=0)
    genre_popularity = genre_popularity.sort_values(by="post_ai", ascending=False).head(10)

    fig_genre, ax_genre = plt.subplots(figsize=(10, 6))
    genre_popularity.plot(kind="bar", ax=ax_genre, colormap="Pastel1")
    ax_genre.set_title("Top 10 Genres by Period")
    ax_genre.set_ylabel("Song Count")
    ax_genre.set_xlabel("Genre")
    ax_genre.tick_params(axis='x', rotation=45)
    st.pyplot(fig_genre)

st.markdown(" ")
st.markdown(" ")

# Feature Comparison and trend
colors = ["red", "gray"]
song_features = ["danceability", "energy", "valence", "tempo", "acousticness",
                 "instrumentalness", "liveness", "speechiness", "loudness", "duration"]
df[song_features] = df[song_features].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=song_features)

scaler = MinMaxScaler()
normalized = pd.DataFrame(scaler.fit_transform(df[song_features]), columns=song_features)
normalized["period"] = df["period"].values
feature_means = normalized.groupby("period").mean().T.round(3)

fig3, ax3 = plt.subplots()
feature_means.plot(kind="bar", ax=ax3, figsize=(12, 6), color=colors)
ax3.set_title("Normalized Song Features: Pre-AI vs Post-AI")
ax3.set_ylabel("Normalized Average")
ax3.set_xlabel("Feature")
ax3.tick_params(axis='x', rotation=45)
st.pyplot(fig3)
    
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

# 5. RQ3: Artist Discovery 
st.header("🚀 Artist Discovery Over Time (RQ3)")

first_appearances = df.groupby("artist")["year"].min().reset_index()
first_years = first_appearances["year"].value_counts().sort_index()
artists_per_year = df.groupby("year")["artist"].nunique()
new_artist_percent = (first_years / artists_per_year) * 100

fig4, ax4 = plt.subplots()
artists_per_year.plot(marker="o", color="darkred", ax=ax4)
ax4.set_title("Unique Artists Per Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Artist Count")
st.pyplot(fig4)

fig5, ax5 = plt.subplots()
new_artist_percent.plot(marker="o", color="skyblue", ax=ax5)
ax5.set_title("% of Newly Discovered Artists Per Year")
ax5.set_xlabel("Year")
ax5.set_ylabel("Percent (%)")
st.pyplot(fig5)

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

# 6. Data Cleaning 
st.header("Data Cleaning Notes")
with st.expander("What cleaning was done?"):
    st.markdown("""
    - Dropped null values in essential columns (e.g., year, popularity)
    - Removed irrelevant columns like RIAA certification
    - Grouped by song + artist to remove duplicate entries
    - Merged genre info from available datasets
    """)

st.markdown("---")
st.caption("Created by Daniella Famakin • Fisk University, 2025")
