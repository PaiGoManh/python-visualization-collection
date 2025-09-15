import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB_data.csv')

df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')
df = df.dropna(subset=['Ratings', 'Rated'])

common_ratings = ['G', 'PG', 'PG-13', 'R']
df = df[df['Rated'].isin(common_ratings)]

plt.figure(figsize=(12,6))
sns.kdeplot(data=df, x='Ratings', hue='Rated', fill=True, alpha=0.5, palette='Set2')

plt.title("IMDB Rating Distribution by Content Rating", weight='bold', fontsize=16)
plt.xlabel("IMDB Rating", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.xlim(0, 10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Rating')
plt.tight_layout()

plt.savefig("seaborn_kdeplot", dpi=150, bbox_inches='tight')
plt.show()