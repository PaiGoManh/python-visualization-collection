import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB_data.csv')

df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')

plt.figure(figsize=(12,6))
sns.boxplot(x='Rated', y='Ratings', data=df)

plt.title("IMDB Ratings by Content Rating", weight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("seaborn_boxplot.png")

plt.show()