# 📺 Netflix Data Cleaning & Exploratory Data Analysis

> A Data Science project completed as part of the **SkillCraft Technology Data Science Internship – Task 2**.

## 📌 Project Overview

This project focuses on **Data Cleaning** and **Exploratory Data Analysis (EDA)** using the **Netflix Movies and TV Shows** dataset. The objective is to clean the dataset, analyze its contents, identify trends, and present meaningful insights through visualizations.

---

## 🎯 Objectives

- Clean and preprocess the dataset.
- Handle missing values and duplicate records.
- Perform exploratory data analysis (EDA).
- Visualize important trends and patterns.
- Extract meaningful business insights from the data.

---

## 📂 Dataset

**Dataset:** Netflix Movies and TV Shows

The dataset contains information about Netflix content, including:

- Content Type
- Title
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Genre

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- WordCloud

---

## 🧹 Data Cleaning Performed

- Removed duplicate records
- Handled missing values
- Cleaned the `date_added` column
- Converted dates to datetime format
- Extracted Year and Month from dates
- Converted movie duration into numeric values
- Standardized country information

---

## 📊 Exploratory Data Analysis

The following visualizations were created:

1. Distribution of Movies vs TV Shows
2. Netflix Content Added Over the Years
3. Top 10 Countries Producing Netflix Content
4. Top 10 Netflix Genres
5. Content Ratings Distribution
6. Movie Duration Distribution
7. Correlation Heatmap
8. Monthly Content Additions
9. Top 15 Directors
10. Genre Word Cloud

---

## 📈 Key Insights

- 🎬 Netflix hosts significantly more **Movies** than **TV Shows**.
- 📈 Content additions increased rapidly after **2016**.
- 🌍 The **United States** contributes the largest number of Netflix titles, followed by **India**.
- 🎭 **International Movies**, **Dramas**, and **Comedies** are the most common genres.
- ⭐ **TV-MA** and **TV-14** are the most frequently assigned ratings.
- ⏱️ Most Netflix movies have a runtime between **80–120 minutes**.
- 📅 Netflix consistently adds new content throughout the year, with some months showing higher activity.

---

## 📁 Project Structure

```
SCT_DS_2/
│
├── data/
│   └── netflix_titles.csv
│
├── outputs/
│   ├── content_type.png
│   ├── yearly_additions.png
│   ├── top_countries.png
│   ├── top_genres.png
│   ├── ratings_distribution.png
│   ├── movie_duration.png
│   ├── correlation_heatmap.png
│   ├── monthly_additions.png
│   ├── top_directors.png
│   └── genre_wordcloud.png
│
├── task2.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/SCT_DS_2.git
```

### 2. Navigate to the project

```bash
cd SCT_DS_2
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python task2.py
```

All generated visualizations will be saved inside the **outputs** folder.

---

## 📌 Future Improvements

- Develop an interactive Streamlit dashboard.
- Perform sentiment analysis on content descriptions.
- Build a recommendation system using the dataset.
- Add interactive visualizations with Plotly.

---

## 👨‍💻 Author

**Vinayak D**

- GitHub: https://github.com/vinayak-30-debug
- LinkedIn: www.linkedin.com/in/vinayakdasarla


---

## ⭐ Acknowledgements

- **SkillCraft Technology** for providing the internship task.
- **Kaggle** for the Netflix Movies and TV Shows dataset.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub!