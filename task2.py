import os
from wordcloud import WordCloud
# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("data/netflix_titles.csv")
# Basic Dataset Information
print("First 5 Rows:")
print(df.head())
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())
# Data Cleaning
# Remove duplicate rows
df.drop_duplicates(inplace=True)
# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
# Remove rows where date_added or duration is missing
df.dropna(subset=["date_added", "duration"], inplace=True)
# Convert date_added to datetime
# Remove leading/trailing spaces
df["date_added"] = df["date_added"].str.strip()
# Convert to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# Dataset information after cleaning
print("\nDataset Shape After Cleaning:")
print(df.shape)
print("\nData Types:")
print(df.dtypes)
# Visualization 1: Movies vs TV Shows
plt.figure(figsize=(6,5))
sns.countplot(
    data=df,
    x="type",
    hue="type",
    palette="Set2",
    legend=False
)
plt.title("Distribution of Movies and TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.tight_layout()
# Save figure
plt.savefig("outputs/content_type.png")
# Display figure
plt.show()
# Visualization 2: Content Added Over the Years
# Extract the year from the date_added column
df["year_added"] = df["date_added"].dt.year
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    x="year_added",
    order=sorted(df["year_added"].dropna().unique()),
    color="steelblue"
)
plt.title("Netflix Content Added Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/yearly_additions.png")
plt.show()
# Visualization 3: Top 10 Countries
# Some rows have multiple countries separated by commas.
# We'll take the first listed country for simplicity.
df["country"] = df["country"].str.split(",").str[0]
# Count the top 10 countries
top_countries = df["country"].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    hue=top_countries.index,
    palette="viridis",
    legend=False
)
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("outputs/top_countries.png")
plt.show()
# Visualization 4: Top 10 Genres
# Split multiple genres and count each genre
genres = (
    df["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)
plt.figure(figsize=(12,6))
sns.barplot(
    x=genres.values,
    y=genres.index,
    hue=genres.index,
    palette="magma",
    legend=False
)
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("outputs/top_genres.png")
plt.show()
# Visualization 5: Content Ratings Distribution
# Get top 10 ratings
ratings = df["rating"].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(
    x=ratings.index,
    y=ratings.values,
    hue=ratings.index,
    palette="coolwarm",
    legend=False
)
plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/ratings_distribution.png")
plt.show()
# Visualization 6: Movie Duration Distribution
# Select only Movies
movies = df[df["type"] == "Movie"].copy()
# Extract duration in minutes
movies["duration_minutes"] = (
    movies["duration"]
    .str.replace(" min", "", regex=False)
    .astype(int)
)
plt.figure(figsize=(10,6))
sns.histplot(
    movies["duration_minutes"],
    bins=30,
    kde=True,
    color="skyblue"
)
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("outputs/movie_duration.png")
plt.show()
# Visualization 7: Correlation Heatmap
# Create a numeric feature for movie duration
df["duration_numeric"] = (
    df["duration"]
    .str.extract(r"(\d+)")
    .astype(float)
)
# Select only numeric columns
numeric_df = df.select_dtypes(include=["number"])
plt.figure(figsize=(8,6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.show()
# Visualization 8: Monthly Content Additions
df["month_added"] = df["date_added"].dt.month_name()
month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]
plt.figure(figsize=(12,6))
sns.countplot(
    data=df,
    x="month_added",
    order=month_order,
    hue="month_added",
    palette="crest",
    legend=False
)
plt.xticks(rotation=45)
plt.title("Netflix Content Added by Month")
plt.xlabel("Month")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("outputs/monthly_additions.png")
plt.show()
# Visualization 9: Top Directors
top_directors = (
    df[df["director"] != "Unknown"]["director"]
    .value_counts()
    .head(15)
)
plt.figure(figsize=(12,7))
sns.barplot(
    x=top_directors.values,
    y=top_directors.index,
    hue=top_directors.index,
    palette="viridis",
    legend=False
)
plt.title("Top 15 Directors on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.tight_layout()
plt.savefig("outputs/top_directors.png")
plt.show()
# Visualization 10: Genre Word Cloud
genres = " ".join(df["listed_in"])
wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(genres)
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Netflix Genres")
plt.tight_layout()
plt.savefig("outputs/genre_wordcloud.png")
plt.show()