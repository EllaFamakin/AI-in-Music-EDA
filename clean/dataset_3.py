# Importing the pandas library to handle my dataset
import pandas as pd

#Loading DT_1 if file is csv
df = pd.read_csv("Billboard_24years_lyrics_spotify.csv")


# #Display a few rows to determine what to clean
df.head()

# #any null data?
#print (df.isnull().sum())

# # check any null data again?
# #print (df.isnull().sum())

# #Remove unwanted columns
df = df.drop(["analysis_url","songurl","url", "lyrics", "uri", "id", "track_href", "time_signature",
              "key", "type"], axis=1)

# # #any null data?
# print (df.isnull().sum())

# # #remove rows with missing info of artists, track_name and album name
print(df.dropna(subset=["duration_ms", "danceability", "energy", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo" ], inplace=True))

# # #any null data?
print (df.isnull().sum())

# # # #Check duplicates
print(df.drop_duplicates(inplace=True))

# # # import seaborn to visualize
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=df["ranking"])
plt.show()

# Q1 = df['popularity'].quantile(0.25)  # 25th percentile
# Q3 = df['popularity'].quantile(0.75)  # 75th percentile
# IQR = Q3 - Q1  # Calculate Interquartile Range

# # # Remove values that are too far from the normal range
# df = df[(df['popularity'] >= (Q1 - 1.5 * IQR)) & (df['popularity'] <= (Q3 + 1.5 * IQR))]

sns.boxplot(x=df["year"])
plt.show()

# # # filter data set to pre and post AI 
pre_ai = df[(df['year'] >= 2000) & (df["year"] < 2015)]  # Data before 2015
post_ai = df[df['year'] >= 2015]  # Data from 2015 onwards

# # #save pre and post AI data
print(pre_ai.to_csv("pre_ai_data_C.csv", index =False))
print(post_ai.to_csv("post_ai_data_C.csv", index =False))

# # #Initial analysis and comparison of pre and post-AI data
plt.figure(figsize=(8, 6))

# boxplot for Pre-AI vs. Post-AI popularity

df['AI_Era'] = df['year'].apply(lambda x: 'Pre-AI' if x <= 2015 else 'Post-AI')

plt.figure(figsize=(8, 5))
sns.boxplot(x='AI_Era', y='ranking', data=df)
plt.title("Ranking of Popular Songs Pre- and Post-AI")
plt.show()

#check if year indicator yearFA is in the dataset
df["year"] = df["year"].astype(int)

# Group by year and count unique artists
artist_count_per_year = df.groupby("year")["band_singer"].nunique().reset_index()
artist_count_per_year.columns = ["Year", "Artist Count"]

#filter from 1999
artist_count_per_year = artist_count_per_year[artist_count_per_year["Year"] >= 1990]

# Add a column to mark pre- and post-AI
artist_count_per_year["AI_Era"] = artist_count_per_year["Year"].apply(
    lambda x: "Pre-AI" if x < 2015 else "Post-AI"
)

# Create the plot
plt.figure(figsize=(12, 6))
sns.barplot(data=artist_count_per_year, x="Year", y="Artist Count", hue="AI_Era", palette="Set2")

plt.title("Number of Unique Artists per Year (Pre vs Post AI)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()