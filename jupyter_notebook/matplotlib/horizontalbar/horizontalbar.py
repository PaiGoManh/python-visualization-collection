import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IMDB_data.csv")

counts = df['Rated'].value_counts()

plt.figure(figsize=(8,6))
plt.barh(
    counts.index,        
    counts.values,       
    color="skyblue", 
    edgecolor="black"
)

plt.title("Number of Movies by Rating Category", weight='bold', fontsize=16)
plt.xlabel("Number of Movies", fontsize=12)
plt.ylabel("Content Rating", fontsize=12)
plt.gca().invert_yaxis()  
plt.tight_layout()

plt.savefig("matpltlib_barh.png", dpi=150, bbox_inches="tight")
plt.show()