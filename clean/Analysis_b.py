import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("Metadataset2.csv")
df.columns = df.columns.str.lower().str.strip()
df = df.dropna(subset=["popularity", "year", "period"])

# Define song features to compare
song_features = ["danceability", "energy", "valence", "tempo", "acousticness",
                 "instrumentalness", "liveness", "speechiness", "loudness", "duration"]

# Ensure features are numeric
df[song_features] = df[song_features].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=song_features)

# Normalize all features using MinMaxScaler
scaler = MinMaxScaler()
normalized_features = pd.DataFrame(
    scaler.fit_transform(df[song_features]),
    columns=song_features
)
normalized_features["period"] = df["period"].values

# Group by period and compute mean of each feature
feature_means = normalized_features.groupby("period").mean().T.round(3)

# Plot grouped bar chart
feature_means.plot(kind="bar", figsize=(12, 6), colormap="Set1")
plt.title("Normalized Song Feature Values by Period (Pre-AI vs Post-AI)")
plt.ylabel("Normalized Average (0–1)")
plt.xlabel("Song Feature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Genre analysis
# === Load Data ===
df = pd.read_csv("Metadataset_with_genre.csv")
df.columns = df.columns.str.lower().str.strip()

# Drop rows missing genre/popularity/period
df = df.dropna(subset=["genre", "popularity", "period"])

# Standardize genre labels
df["genre"] = df["genre"].astype(str).str.lower().str.strip()

# === Focus on Top Genres ===
top_genres = df["genre"].value_counts().nlargest(6).index.tolist()
df_top = df[df["genre"].isin(top_genres)]

# === 1. Stacked Bar Chart: Genre Count per Period ===
genre_counts = df_top.groupby(["genre", "period"]).size().unstack(fill_value=0)
genre_counts.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="Pastel1")
plt.title("Number of Songs by Genre (Pre-AI vs Post-AI)")
plt.xlabel("Genre")
plt.ylabel("Song Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 2. Grouped Bar Chart: Popularity per Genre by Period ===
genre_popularity = df_top.groupby(["genre", "period"])["popularity"].mean().unstack().round(1)
genre_popularity.plot(kind="bar", figsize=(10, 6), colormap="Set2")
plt.title("Average Popularity by Genre (Pre-AI vs Post-AI)")
plt.xlabel("Genre")
plt.ylabel("Average Popularity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

