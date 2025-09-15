import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB_data.csv')

df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')

df = df.dropna(subset=['Ratings', 'Rated'])

common_ratings = ['G', 'PG', 'PG-13', 'R', 'NC-17']
df = df[df['Rated'].isin(common_ratings)]

plt.figure(figsize=(12,6))
sns.barplot(x='Rated', y='Ratings', data=df, palette='viridis')

plt.title("Average IMDB Rating by Content Rating", weight='bold', fontsize=16)
plt.xlabel("Content Rating", fontsize=12)
plt.ylabel("Average Rating", fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 10)  
plt.tight_layout()

plt.savefig("seaborn_barplot.png", dpi=150, bbox_inches='tight')
plt.show()
