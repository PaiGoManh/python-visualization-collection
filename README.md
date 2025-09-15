# 🎨 Python Data Visualization Project: IMDB Dataset

## 📖 Project Description
This project showcases **data visualization in Python** using two of the most popular libraries: **Matplotlib** and **Seaborn**.  
The dataset used is an IMDB movie dataset (`IMDB_data.csv`).  

The goal of this project is to practice and demonstrate different visualization techniques by organizing them into separate, clean folders, with each folder containing **Python code** and the **generated plot image**.

---

## 📂 Project Structure

```text
project-root/
│
├── data/
│   └── IMDB_data.csv            # IMDB dataset
│
├── notebooks/
│   ├── seaborn/                 # Seaborn visualizations
│   │   ├── barplot/
│   │   │   ├── barplot.py
│   │   │   └── seaborn_barplot.png
│   │   ├── boxplot/
│   │   │   ├── boxplot.py
│   │   │   └── seaborn_boxplot.png
│   │   ├── heatmap/
│   │   │   ├── heatmap.py
│   │   │   └── seaborn_heatmap.png
│   │   ├── kdeplot/
│   │   │   ├── kdeplot.py
│   │   │   └── seaborn_kdeplot.png
│   │   └── pointplot/
│   │       ├── pointplot.py
│   │       └── seaborn_pointplot.png
│   │
│   └── matplotlib/              # Matplotlib visualizations
│       ├── barchart/
│       │   ├── bar.py
│       │   └── plt_bar.png
│       ├── histogram/
│       │   ├── hist.py
│       │   └── plt_hist.png
│       ├── horizontalbar/
│       │   ├── barh.py
│       │   └── plt_barh.png
│       ├── piechart/
│       │   ├── pie.py
│       │   └── plt_pie.png
│       └── stackplot/
│           ├── stackplot.py
│           └── plt_stackplot.png
│
└── README.md


---

## ⚙️ Setup & Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/PaiGoManh/python-visualization-collection.git
   cd python-visualization-collection
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   # 📊 Visualizations Included

## 🔵 Seaborn

- **Bar Plot** – Average IMDB ratings grouped by rating category.  

- **Box Plot** – Distribution of movie ratings across categories.  

- **Heatmap** – Correlations between numeric values (runtime, ratings, rank).  

- **KDE Plot** – Kernel Density Estimate of rating distributions.  

- **Point Plot** – Mean rating per category with confidence intervals.  

---

## 🟠 Matplotlib

- **Bar Chart** – Number of movies per content rating.  

- **Histogram** – Distribution of IMDB ratings.  

- **Horizontal Bar Chart** – Rating categories shown horizontally.  

- **Pie Chart** – Proportion of movies by category.  

- **Stackplot** – Example stacked area chart (demoing time-series style visualization).  

---

## ✨ Inspiration
This repo was built as a **visualization gallery** and a reference toolkit for working with IMDB data (or any datasets).  
It bridges **Matplotlib’s flexibility** with **Seaborn’s simplicity** for data exploration and presentation.

---

## 👨‍💻 Author
**Your Name**  
GitHub: [@Paigomanh](https://github.com/PaiGoManh)

---

## 📜 License
This project is licensed under the **MIT License** — feel free to use and adapt it.
   
