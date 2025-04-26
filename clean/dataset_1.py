# Importing the pandas library to handle my dataset
import pandas as pd

#Loading DT_1 if file is csv
df = pd.read_csv("songs_normalize.csv")


#Display a few rows to determine what to clean
df.head()

#any null data?
print (df.isnull().sum())

#remove rows with missing info of artists, track_name and album name
#print(df.dropna(subset=["track_name", "artists", "album_name"], inplace=True))

# check any null data again?
#print (df.isnull().sum())

# #Check duplicates
print(df.drop_duplicates(inplace=True))

#Remove unwanted columns
#df = df.drop("album_name", axis=1)

#Remove unwanted columns
# df.drop("album_name", axis=1, inplace=True)
df.drop("explicit", axis=1, inplace=True)
# df.drop("liveness", axis=1, inplace=True)
# df.drop("key", axis=1, inplace=True)
# df.drop("time_signature", axis=1, inplace=True)

# import seaborn to visualize
import seaborn as sns
import matplotlib.pyplot as plt

# sns.boxplot(x=df["popularity"])
# plt.show()

Q1 = df['popularity'].quantile(0.25)  # 25th percentile
Q3 = df['popularity'].quantile(0.75)  # 75th percentile
IQR = Q3 - Q1  # Calculate Interquartile Range

# Remove values that are too far from the normal range
df = df[(df['popularity'] >= (Q1 - 1.5 * IQR)) & (df['popularity'] <= (Q3 + 1.5 * IQR))]

sns.boxplot(x=df["popularity"])
# plt.show()

# filter data set to pre and post AI 
pre_ai = df[(df['year'] >= 2000) & (df["year"] < 2015)]  # Data before 2015
post_ai = df[df['year'] >= 2015]  # Data from 2015 onwards

#save pre and post AI data
print(pre_ai.to_csv("pre_ai_data_A.csv", index =False))
print(post_ai.to_csv("post_ai_data_A.csv", index =False))

#Initial analysis and comparison of pre and post-AI data
plt.figure(figsize=(8, 6))

# boxplot for Pre-AI vs. Post-AI popularity

df['AI_Era'] = df['year'].apply(lambda x: 'Pre-AI' if x <= 2015 else 'Post-AI')

plt.figure(figsize=(8, 5))
sns.boxplot(x='AI_Era', y='popularity', data=df)
plt.title("Popularity of Songs Pre- and Post-AI")
plt.show()
