import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IMDB_data.csv")
counts = df['Rated'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    counts.values,
    labels=counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Set3.colors
)

plt.title("Proportion of Movies by Rating Category", weight='bold')
plt.tight_layout()

plt.savefig("matpltlib_pie.png", dpi=150, bbox_inches="tight")
plt.show()