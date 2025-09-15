import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2000, 2010)                
g = np.random.randint(1,5, len(x))      
pg = np.random.randint(5,15, len(x))     
r = np.random.randint(10,25, len(x))     

plt.figure(figsize=(10,6))
plt.stackplot(x, g, pg, r,
              labels=["G","PG","R"], 
              colors=["lightgreen","skyblue","salmon"])

plt.title("Stacked Area Plot Example (Movie Counts by Rating)", weight='bold')
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.legend(loc="upper left")
plt.tight_layout()

plt.savefig("plt_stackplot.png", dpi=150, bbox_inches="tight")
plt.show()