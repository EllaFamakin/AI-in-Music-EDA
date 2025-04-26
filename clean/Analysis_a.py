import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your final dataset
df = pd.read_csv("Metadataset2.csv")

# Drop rows missing key values
df = df.dropna(subset=["Popularity", "year", "period"])

# === AVERAGE POPULARITY BY YEAR ===
yearly_popularity = df.groupby("year")["Popularity"].mean().reset_index()

# === POPULARITY BY PERIOD (for boxplot + stats) ===
boxplot_data = df[["Popularity", "period"]]
summary_stats = df.groupby("period")["Popularity"].agg(["count", "mean", "median", "std", "min", "max"]).round(2)

# === LINE PLOT: Year vs Avg Popularity ===
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_popularity, x="year", y="Popularity", marker="o", color="blue")
plt.title("Average Popularity by Year (2000–2019)")
plt.xlabel("Year")
plt.ylabel("Average Popularity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === BOXPLOT: Popularity Distribution by Period ===
plt.figure(figsize=(8, 6))
sns.boxplot(data=boxplot_data, x="period", y="Popularity", palette="Set2")
plt.title("Popularity Distribution: Pre-AI vs Post-AI")
plt.xlabel("Period")
plt.ylabel("Popularity")
plt.tight_layout()
plt.show()

# === View Summary Statistics ===
print(summary_stats)
