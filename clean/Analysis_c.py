import pandas as pd
import matplotlib.pyplot as plt

# === Load and clean the dataset ===
df = pd.read_csv("Metadataset2.csv")
df.columns = df.columns.str.lower().str.strip()
df = df.dropna(subset=["artist", "year"])

# Standardize artist names
df["artist"] = df["artist"].astype(str).str.lower().str.strip()

# === Unique artists per year ===
artists_per_year = df.groupby("year")["artist"].nunique()

# === First appearance year for each artist ===
first_year = df.groupby("artist")["year"].min().reset_index()

# === Count of new artists discovered each year ===
first_appearance_count = first_year["year"].value_counts().sort_index()

# === Percent of artists in a year who are new ===
new_artist_percent = (first_appearance_count / artists_per_year) * 100

# === Combine into summary DataFrame ===
artist_discovery_df = pd.DataFrame({
    "unique_artists": artists_per_year,
    "new_artists": first_appearance_count,
    "percent_new": new_artist_percent
}).fillna(0)

# === Plot 1: Unique artists per year ===
plt.figure(figsize=(10, 5))
artist_discovery_df["unique_artists"].plot(marker="o", color="blue")
plt.title("Unique Artists per Year")
plt.ylabel("Artist Count")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Plot 2: Percent of new artists per year ===
plt.figure(figsize=(10, 5))
artist_discovery_df["percent_new"].plot(marker="o", color="green")
plt.title("Percentage of Newly Discovered Artists per Year")
plt.ylabel("Percent (%)")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Summary: Total new artists pre- vs post-AI ===
pre_ai_new = first_year[first_year["year"] < 2015].shape[0]
post_ai_new = first_year[first_year["year"] >= 2015].shape[0]

summary = pd.DataFrame({
    "Period": ["Pre-AI (2000–2014)", "Post-AI (2015–2019)"],
    "New Artists": [pre_ai_new, post_ai_new]
})

print(summary)
