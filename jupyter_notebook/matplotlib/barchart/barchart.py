import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IMDB_data.csv")

counts = df['Rated'].value_counts()

plt.figure(figsize=(8,6))
plt.bar(counts.index, counts.values, color="teal", edgecolor="black")

plt.title("Number of Movies by Rating Category", weight='bold')
plt.xlabel("Content Rating")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("matpltlib_bar.png", dpi=150, bbox_inches="tight")
plt.show()