# 🎬 YouTube Channel Recommender – Data Science Project



[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-red)](https://www.kaggle.com/datasets)

---

## 🚀 Project Overview
Welcome to the **YouTube Channel Recommender**!  
A **NLP-based recommendation system** that suggests the most relevant YouTube channels based on user queries.  

> **Examples of queries:**  
> - `"learn Python"` → Top coding channels  
> - `"funny videos"` → Entertaining channels  
> - `"data science tutorials"` → Recommended educational channels  

---

## 📊 Dataset
**Source:** Kaggle – *2024 YouTube Channels (1 Million+)*  

**Key Columns Overview:**  

| Column | Description |
|--------|-------------|
| `channel_id` | Unique ID of the channel |
| `channel_name` | Name of the channel |
| `channel_link` | URL of the channel |
| `description` | Channel description |
| `keywords` | Keywords associated with the channel |
| `subscriber_count` | Number of subscribers |
| `total_views` | Total views |
| `total_videos` | Total videos |
| `join_date` | Channel join date |
| `mean_views_last_30_videos` | Average views of last 30 videos |
| `median_views_last_30_videos` | Median views of last 30 videos |
| `std_views_last_30_videos` | Standard deviation of last 30 videos |
| `videos_per_week` | Average weekly uploads |

> ⚡ **Fun Fact:** Dataset has **1 million+ channels** – perfect for large-scale recommendations!  

---

## 🧹 Data Preprocessing
- **Text Cleaning**  
  - Lowercase conversion  
  - Remove punctuation & special characters  
  - Remove extra spaces  

- **Feature Engineering**  
  - Combined `channel_name`, `description`, `keywords` → **single text column**  
  - Selected relevant metadata for recommendation  

- **Vectorization**  
  - Applied **TF-IDF** to convert text into numeric vectors  
  - Created **sparse vectors** for each channel  

---

## 🤖 Recommendation Logic
- **Query Input:** User types a topic or interest  
- **Vectorize Query:** TF-IDF vector of the query  
- **Compute Cosine Similarity:** Compare query vs all channels  
- **Return Top-K Results:** Sorted by similarity score  

**Sample Output:**

| Channel | Description | Subscribers | Views | Videos | Score |
|---------|------------|------------|-------|-------|-------|
| CodeWithHarry | Learn Python, Java, ML... | 2M | 100M | 300 | 0.89 |
| freeCodeCamp | Programming tutorials... | 4M | 500M | 150 | 0.85 |

---

## 🛠 Tech Stack
- **Python** – Logic & preprocessing  
- **Pandas** – Data handling  
- **Scikit-learn** – TF-IDF & cosine similarity  
- **Pickle** – Save/load trained model  

---

## 💡 Key Features
- Fast **similarity-based recommendations**  
- Handles **1M+ channels efficiently**  
- Easily extendable for **personalized suggestions**  
- Ready for **integration into web apps or dashboards**  

---

## 🌟 Future Enhancements
- Add **thumbnails & clickable links**  
- Implement **category filters**: Coding, Entertainment, Music  
- Include **personalized recommendations based on user behavior**  
- Build **interactive web frontend** (Streamlit / Dash)  

---

## 📁 Repository Structure
```text
youtube_recommender/
│
├─ youtube_model.pkl       # Trained model
├─ recommendation.ipynb    # Data preprocessing & training notebook
├─ README.md               # Project documentation
