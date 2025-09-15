
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IMDB_data.csv")

df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')

ratings = df['Ratings'].dropna()

plt.figure(figsize=(8,6))
plt.hist(
    ratings, 
    bins=15,                     
    color="skyblue", 
    edgecolor="black",
    alpha=0.8
)

plt.title("Distribution of IMDB Ratings", weight='bold', fontsize=16)
plt.xlabel("IMDB Rating", fontsize=12)
plt.ylabel("Number of Movies", fontsize=12)
plt.xlim(0, 10)  
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig("plt_hist.png", dpi=150, bbox_inches="tight")
plt.show()