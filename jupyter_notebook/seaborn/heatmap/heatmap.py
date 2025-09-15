import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("IMDB_data.csv")

df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')

if 'Runtime' in df.columns:
    df['Runtime'] = df['Runtime'].astype(str).str.replace(' min', '', regex=False)
    df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')

numeric_df = df.select_dtypes(include=['number'])

corr = numeric_df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(
    corr,
    annot=True,          
    fmt=".2f",           
    cmap="coolwarm",     
    vmin=-1, vmax=1,     
    cbar_kws={"shrink": 0.8}
)

plt.title("Correlation Heatmap of IMDB Dataset", weight='bold', fontsize=16)
plt.tight_layout()

plt.savefig("seaborn_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()

