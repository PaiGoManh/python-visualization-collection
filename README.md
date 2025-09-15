# 🎨 Python Data Visualization Project: IMDB Dataset

## 📖 Project Description
This project showcases **data visualization in Python** using two of the most popular libraries: **Matplotlib** and **Seaborn**.  
The dataset used is an IMDB movie dataset (`IMDB_data.csv`).  

The goal of this project is to practice and demonstrate different visualization techniques by organizing them into separate, clean folders, with each folder containing **Python code** and the **generated plot image**.

---

## 📂 Project Structure

project-root/
│
├── data/
│ └── IMDB_data.csv # IMDB dataset
│
├── notebooks/
│ ├── seaborn/
│ │ ├── barplot/
│ │ │ ├── barplot.py
│ │ │ └── seaborn_barplot.png
│ │ ├── boxplot/
│ │ │ ├── boxplot.py
│ │ │ └── seaborn_boxplot.png
│ │ ├── heatmap/
│ │ │ ├── heatmap.py
│ │ │ └── seaborn_heatmap.png
│ │ ├── kdeplot/
│ │ │ ├── kdeplot.py
│ │ │ └── seaborn_kdeplot.png
│ │ └── pointplot/
│ │ ├── pointplot.py
│ │ └── seaborn_pointplot.png
│ │
│ └── matplotlib/
│ ├── barchart/
│ │ ├── bar.py
│ │ └── plt_bar.png
│ ├── histogram/
│ │ ├── hist.py
│ │ └── plt_hist.png
│ ├── horizontalbar/
│ │ ├── barh.py
│ │ └── plt_barh.png
│ ├── piechart/
│ │ ├── pie.py
│ │ └── plt_pie.png
│ └── stackplot/
│ ├── stackplot.py
│ └── plt_stackplot.png
│
└── README.md



---

## ⚙️ Setup & Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   # 📊 Visualizations Included

## 🔵 Seaborn

- **Bar Plot** – Average IMDB ratings grouped by rating category.  
  ![Seaborn Barplot](notebooks/seaborn/barplot/seaborn_barplot.png)

- **Box Plot** – Distribution of movie ratings across categories.  
  ![Seaborn Boxplot](notebooks/seaborn/boxplot/seaborn_boxplot.png)

- **Heatmap** – Correlations between numeric values (runtime, ratings, rank).  
  ![Seaborn Heatmap](notebooks/seaborn/heatmap/seaborn_heatmap.png)

- **KDE Plot** – Kernel Density Estimate of rating distributions.  
  ![Seaborn KDE Plot](notebooks/seaborn/kdeplot/seaborn_kdeplot.png)

- **Point Plot** – Mean rating per category with confidence intervals.  
  ![Seaborn Pointplot](notebooks/seaborn/pointplot/seaborn_pointplot.png)

---

## 🟠 Matplotlib

- **Bar Chart** – Number of movies per content rating.  
  ![Matplotlib Bar Chart](notebooks/matplotlib/barchart/plt_bar.png)

- **Histogram** – Distribution of IMDB ratings.  
  ![Matplotlib Histogram](notebooks/matplotlib/histogram/plt_hist.png)

- **Horizontal Bar Chart** – Rating categories shown horizontally.  
  ![Horizontal Bar Chart](notebooks/matplotlib/horizontalbar/plt_barh.png)

- **Pie Chart** – Proportion of movies by category.  
  ![Pie Chart](notebooks/matplotlib/piechart/plt_pie.png)

- **Stackplot** – Example stacked area chart (demoing time-series style visualization).  
  ![Stackplot](notebooks/matplotlib/stackplot/plt_stackplot.png)

---

## ✨ Inspiration
This repo was built as a **visualization gallery** and a reference toolkit for working with IMDB data (or any datasets).  
It bridges **Matplotlib’s flexibility** with **Seaborn’s simplicity** for data exploration and presentation.

---

## 👨‍💻 Author
**Your Name**  
GitHub: [@yourusername](https://github.com/yourusername)

---

## 📜 License
This project is licensed under the **MIT License** — feel free to use and adapt it.
   
