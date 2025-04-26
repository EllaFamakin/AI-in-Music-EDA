import pandas as pd
#Make a meta data set
d= pd.read_csv("combined_no_riaa_dataset.csv")
# filter data set to pre and post AI 
pre = d[(d['year'] >= 2000) & (d["year"] < 2015)]. copy() # Data before 2015
post = d[d['year'] >= 2015].copy()  # Data from 2015 onwards


# Step 1: Load all relevant pre and Post-AI datasets
pre_a = pd.read_csv("pre_ai_data_1.csv")
pre_b = pd.read_csv("pre_ai_data_2.csv")
pre_c = pd.read_csv("pre_ai_data_3.csv")


# Step 2: Load all relevant post-AI datasets
post_a = pd.read_csv("post_ai_data_1.csv")
post_b = pd.read_csv("post_ai_data_2.csv")
post_c = pd.read_csv("post_ai_data_3.csv")



# Step 3: Tag periods
for df in [pre_a, pre_b, pre_c,pre]:
    df["period"] = "pre_ai"
for df in [post_a, post_b, post_c, post]:
    df["period"] = "post_ai"

# Step 4: Combine all
combined_df = pd.concat(
    [pre_a, pre_b, pre_c, pre, post_a, post_b, post_c, post],
    ignore_index=True
)

# Step 5: Drop irrelevant columns
combined_df = combined_df.drop(columns=[col for col in combined_df.columns if "Unnamed" in col or col == "X"], errors='ignore')

# Step 6: Drop rows missing year or popularity
combined_df = combined_df.dropna(subset=["year", "Popularity"])

# Step 7: Group by song + artist (to remove duplicate versions)
grouped_df = combined_df.groupby(["Name", "Artist"]).agg({
    "Popularity": "mean",
    "Valence": "mean" if "Valence" in combined_df.columns else "first",
    "Energy": "mean" if "Energy" in combined_df.columns else "first",
    "Tempo": "mean" if "Tempo" in combined_df.columns else "first",
    "Acousticness": "mean" if "Acousticness" in combined_df.columns else "first",
    "Danceability": "mean" if "Danceability" in combined_df.columns else "first",
    "Duration": "mean" if "Duration" in combined_df.columns else "first",
    "Instrumentalness": "mean" if "Instrumentalness" in combined_df.columns else "first",
    "Liveness": "mean" if "Liveness" in combined_df.columns else "first",
    "Loudness": "mean" if "Loudness" in combined_df.columns else "first",
    "Speechiness": "mean" if "Speechiness" in combined_df.columns else "first",
    "Mode": "first" if "Mode" in combined_df.columns else "first",
    "Album": "first" if "Album" in combined_df.columns else "first",
    "year": "min",
    "period": "first"
}).reset_index()

print(grouped_df.to_csv("Metadataset2.csv", index =False))

#diagnostic code
# print("grouped_df columns:", grouped_df.columns.tolist())
# print("pre_a columns:", pre_a.columns.tolist())
# print("post_a columns:", post_a.columns.tolist())

genre_pool = pd.concat([pre_a, post_a], ignore_index=True)
genre_pool.rename(columns={"song": "Name", "artist": "Artist"}, inplace=True)

# === STEP 4: Standardize Text Columns ===
for df in [grouped_df, genre_pool]:
    df["Name"] = df["Name"].astype(str).str.lower().str.strip()
    df["Artist"] = df["Artist"].astype(str).str.lower().str.strip()

# === STEP 5: Keep Only Genre Info from Source ===
genre_info = genre_pool[["Name", "Artist", "genre", "popularity"]].dropna()

# === STEP 6: Merge Genre Into Final Dataset ===
meta_with_genre = grouped_df.merge(genre_info, on=["Name", "Artist"], how="left")

# === STEP 7 (Optional): Save the Merged Dataset ===
meta_with_genre.to_csv("Metadataset_4.csv", index=False)
print("✅ Genre merged! File saved as Metadataset_with_genre.csv")

