# # Importing the pandas library to handle my dataset
import pandas as pd

# #Loading DT_1 if file is csv
# df = pd.read_csv("artistDf.csv")


# #Display a few rows to determine what to clean
# df.head()

# #remove rows with missing info of artists, track_name and album name
# print(df.dropna(subset=["Genres"], inplace=True))

# # # #Check duplicates
# print(df.drop_duplicates(inplace=True))

# # #Remove unwanted columns
# df = df.drop(["Genres", "NumAlbums", "Group.Solo", "Gender", "X"], axis=1)

# # # check any null data again?
# print (df.isnull().sum())

# # import seaborn to visualize
# import seaborn as sns
# import matplotlib.pyplot as plt

# #check if year indicator yearFA is in the dataset
# df["YearFirstAlbum"] = df["YearFirstAlbum"].astype(int)

# # Group by year and count unique artists
# artist_count_per_year = df.groupby("YearFirstAlbum")["Artist"].nunique().reset_index()
# artist_count_per_year.columns = ["Year", "Artist Count"]

# #filter from 1999
# artist_count_per_year = artist_count_per_year[artist_count_per_year["Year"] >= 1990]

# # Add a column to mark pre- and post-AI
# artist_count_per_year["AI_Era"] = artist_count_per_year["Year"].apply(
#     lambda x: "Pre-AI" if x < 2015 else "Post-AI"
# )

# # Create the plot
# plt.figure(figsize=(12, 6))
# sns.barplot(data=artist_count_per_year, x="Year", y="Artist Count", hue="AI_Era", palette="Set2")

# plt.title("Number of Unique Artists per Year (Pre vs Post AI)")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # filter data set to pre and post AI 
# pre_ai = df[(df['YearFirstAlbum'] >= 2000) & (df["YearFirstAlbum"] < 2015)]  # Data before 2015
# post_ai = df[df['YearFirstAlbum'] >= 2015]  # Data from 2015 onwards

# # #save pre and post AI data
# print(pre_ai.to_csv("pre_ai_dataI.csv", index =False))
# print(post_ai.to_csv("post_ai_dataI.csv", index =False))

# # #Initial analysis and comparison of pre and post-AI data
# plt.figure(figsize=(8, 6))

# # boxplot for Pre-AI vs. Post-AI popularity

# df['AI_Era'] = df['YearFirstAlbum'].apply(lambda x: 'Pre-AI' if x <= 2015 else 'Post-AI')

# plt.figure(figsize=(8, 5))
# sns.boxplot(x='AI_Era', y="Artist", data=df)
# plt.title("Artist discovery Pre- and Post-AI")
# plt.show()


#RiaaSingleCerts
# Importing the pandas library to handle my dataset
import pandas as pd

# #Loading DT_1 if file is csv
df1 = pd.read_csv("riaaSingleCerts_1999-2019.csv")


# #Display a few rows to determine what to clean
df1.head()

# #any null data?
(df1.isnull().sum())

# # #Check duplicates
print(df1.drop_duplicates(inplace=True))

# #Remove unwanted columns
df = df1.drop(["Label", "X"], axis=1)

# # import seaborn to visualize
# import seaborn as sns
# import matplotlib.pyplot as plt


# #Song Attributes
# # Importing the pandas library to handle my dataset
import pandas as pd

# #Loading DT_1 if file is csv
df2 = pd.read_csv("songAttributes_1999-2019.csv")


# #Display a few rows to determine what to clean
df2.head()

# #any null data?
(df2.isnull().sum())

# # #Check duplicates
print(df2.drop_duplicates(inplace=True))

# #Remove unwanted columns
df2 = df2.drop(["TimeSignature", "Explicit"], axis=1)


# # import seaborn to visualize
# import seaborn as sns
# import matplotlib.pyplot as plt

# # sns.boxplot(x=df["popularity"])
# # plt.show()

# Q1 = df['popularity'].quantile(0.25)  # 25th percentile
# Q3 = df['popularity'].quantile(0.75)  # 75th percentile
# IQR = Q3 - Q1  # Calculate Interquartile Range

# # Remove values that are too far from the normal range
# df = df[(df['popularity'] >= (Q1 - 1.5 * IQR)) & (df['popularity'] <= (Q3 + 1.5 * IQR))]

# sns.boxplot(x=df["popularity"])
# # plt.show()

# # filter data set to pre and post AI 
# pre_ai = df[(df['year'] >= 2000) & (df["year"] < 2015)]  # Data before 2015
# post_ai = df[df['year'] >= 2015]  # Data from 2015 onwards

# #save pre and post AI data
# print(pre_ai.to_csv("pre_ai_data.csv", index =False))
# print(post_ai.to_csv("post_ai_data.csv", index =False))

# #Initial analysis and comparison of pre and post-AI data
# plt.figure(figsize=(8, 6))

# # boxplot for Pre-AI vs. Post-AI popularity

# df['AI_Era'] = df['year'].apply(lambda x: 'Pre-AI' if x <= 2015 else 'Post-AI')

# plt.figure(figsize=(8, 5))
# sns.boxplot(x='AI_Era', y='popularity', data=df)
# plt.title("Popularity of Songs Pre- and Post-AI")
# plt.show()

# #Song Attributes
# # Importing the pandas library to handle my dataset
import pandas as pd

# #Loading DT_1 if file is csv
df3 = pd.read_csv("billboardHot100_1999-2019.csv")


# #Display a few rows to determine what to clean
df3.head()

# # #Check duplicates
print(df3.drop_duplicates(inplace=True))

#Convert to keep only the year in date
df3['Date'] = pd.to_datetime(df3['Date'])

# Extract the year from the 'date' column
df3['year'] = df3['Date'].dt.year

# #Remove unwanted columns
df3 = df3.loc[:, ["Name", "Artists", "year"]]

# #remove rows with missing info of artists, track_name and album name
(df3.dropna(subset=["year"], inplace=True))

df3 = df3.rename(columns={'Artists': 'Artist'})

print(df3.drop_duplicates(subset = ["Artist"] ))


# #any null data?
(df3.isnull().sum())

print(df3.to_csv("bill_data.csv", index =False))

# Merge Data sets
# Standardize
df1["Artist"] = df1["Artist"].astype(str).str.lower().str.strip()
df1["Name"] = df1["Name"].astype(str).str.lower().str.strip()

df2["Artist"] = df2["Artist"].str.lower().str.strip()
df2["Name"] = df2["Name"].str.lower().str.strip()

df3["Artist"] = df3["Artist"].astype(str).str.lower().str.strip()
df3["Name"] = df3["Name"].astype(str).str.lower().str.strip()


# STEP 3: Merge Billboard + Song Attributes
combined_df = pd.merge(df2, df3, on=["Name", "Artist"], how="left")

# Drop rows with no year or duplicate song/artist pairs
combined_df = combined_df.dropna(subset=["year"])
combined_df = combined_df.drop_duplicates(subset=["Name", "Artist"])

# STEP 4: Add AI Period Tag
combined_df["period"] = combined_df["year"].apply(lambda y: "pre_ai" if y < 2016 else "post_ai")

# STEP 5: Save Clean Dataset
combined_df.to_csv("combined_no_riaa_dataset.csv", index=False)

print("✅ Merge complete. File saved as 'combined_no_riaa_dataset.csv'.")
print("Rows:", combined_df.shape[0], "| Columns:", combined_df.shape[1])


# #Merge1
# combined_df = pd.merge(df2, df1, on=["Name", "Artist"], how="left")

# # Save the df
# combined_df.to_csv("combined_dt.csv", index=False)

# #Merge 2
# df4 = pd.read_csv("combined_dt.csv")

# combined_dff = pd.merge(df4, df3, on=["Name", "Artist"], how="left")

# # Save the df
# combined_dff.to_csv("combined_dtF.csv", index=False)


# # STEP 2: Clean 'Name' and 'Artist' fields
# for df in [song_attributes, riaa_data, bill_data]:
#     df["Name"] = df["Name"].str.lower().str.strip()
#     df["Artist"] = df["Artist"].str.lower().str.strip()

# # STEP 3: Merge song attributes + RIAA
# merged_1 = pd.merge(song_attributes, riaa_data, on=["Name", "Artist"], how="left")

# # STEP 4: Merge that with Billboard data
# final_combined = pd.merge(merged_1, bill_data[["Name", "Artist", "year"]], on=["Name", "Artist"], how="left")

# # STEP 5: Save it!
# final_combined.to_csv("combined_dataF_full.csv", index=False)

# # #clean/Analyze
# df5 = pd.read_csv("combined_dataF_full.csv")

# # # #Display a few rows to determine what to clean
# # df5.head()

# # #any null data?
# # print (df5.isnull().sum())

# # # Remove all rows with any null values
# # clean = df5.columns.difference(["X", 'Name', 'Artist', 'RiaaStatus', 'Label'])

# df5= df5.dropna(subset=["year", "Popularity"])
# # Drop auto-generated index columns
# df5 = df5.drop(columns=[col for col in df5.columns if "Unnamed" in col or col == "X"])

# # # #Check duplicates
# print(df5.drop_duplicates(subset=["Name", "Artist"]))
# print (df5.isnull().sum())

# # # filter data set to pre and post AI 
# pre_ai = df5[(df5['year'] >= 2000) & (df5["year"] < 2015)]  # Data before 2015
# post_ai = df5[df5['year'] >= 2015]  # Data from 2015 onwards

# # #save pre and post AI data
# print(pre_ai.to_csv("pre_ai_data_5.csv", index =False))
# print(post_ai.to_csv("post_ai_data_5.csv", index =False))


# # import seaborn to visualize
# import seaborn as snsS
# import matplotlib.pyplot as plt



# import pandas as pd

# # Load merged dataset
# df5 = pd.read_csv("combined_dataF_full.csv")

# # Remove index or placeholder columns
# df5 = df5.drop(columns=[col for col in df.columns if "Unnamed" in col or col == "X"], errors='ignore')

# # Keep only rows with valid year and popularity
# df5= df5.dropna(subset=["year", "Popularity"])

# # Group to avoid duplicate songs (e.g., multiple chart appearances)
# df_grouped = df5.groupby(["Name", "Artist"]).agg({
#     "Popularity": "mean" if "Popularity" in df5.columns else "first",
#     "Valence": "mean" if "Valence" in df5.columns else "first",
#     "Energy": "mean" if "Energy" in df5.columns else "first",
#     "Tempo": "mean" if "Tempo" in df5.columns else "first",
#     "Acousticness": "mean" if "Acousticness" in df5.columns else "first",
#     "Danceability": "mean" if "Danceability" in df5.columns else "first",
#     "Duration": "mean" if "Duration" in df5.columns else "first",
#     "Instrumentalness": "mean" if "Instrumentalness" in df5.columns else "first",
#     "Liveness": "mean" if "Liveness" in df5.columns else "first",
#     "Loudness": "mean" if "Loudness" in df5.columns else "first",
#     "Speechiness": "mean" if "Speechiness" in df5.columns else "first",
#     "Mode": "first" if "Mode" in df5.columns else "first",
#     "Album": "first" if "Album" in df5.columns else "first",
#     "year": "min" if "year" in df5.columns else "first",
#     "RiaaStatus": "first" if "RiaaStatus" in df5.columns else "first",
#     "Label": "first" if "Label" in df5.columns else "first"
# }).reset_index()


# # Add AI period column
# df_grouped["period"] = df_grouped["year"].apply(lambda y: "pre_ai" if y < 2016 else "post_ai")

# # Split by period
# pre_ai = df_grouped[df_grouped["period"] == "pre_ai"]
# post_ai = df_grouped[df_grouped["period"] == "post_ai"]

# # Save clean splits
# pre_ai.to_csv("pre_ai_data_c.csv", index=False)
# post_ai.to_csv("post_ai_data_c.csv", index=False)

# print("Pre-AI shape:", pre_ai.shape)
# print("Post-AI shape:", post_ai.shape)
# print("Final combined shape:", df_grouped.shape)
