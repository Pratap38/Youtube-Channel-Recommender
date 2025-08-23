🎬 YouTube Channel Recommender – Data Science Project

🚀 Project Overview

Ever wondered which YouTube channels are best for your interests?
This project is a smart YouTube channel recommendation system that uses NLP and Machine Learning to suggest the most relevant channels based on your query!

Example queries:

"learn Python" → Top educational channels

"funny videos" → Entertaining channels

"data science tutorials" → Recommended channels for learning

📊 Dataset

Source: Kaggle – 2024 YouTube Channels (1 Million+)

Size: ~1 million channels

Key Columns:

Column	Description
channel_id	Unique channel ID
channel_name	Name of the channel
channel_link	URL to channel
description	Channel description
keywords	Keywords associated with channel
subscriber_count	Number of subscribers
total_views	Total views of all videos
total_videos	Total number of videos
join_date	Channel creation date
mean_views_last_30_videos	Average views of last 30 videos
median_views_last_30_videos	Median views of last 30 videos
std_views_last_30_videos	Standard deviation of last 30 videos
videos_per_week	Average weekly uploads
🧹 Data Preprocessing

Text Cleaning:

Lowercase all text

Remove punctuation, special characters, extra spaces

Optional: remove stopwords for better results

Feature Engineering:

Combined channel_name, description, and keywords into a single text column

Selected relevant metadata for recommendation

Vectorization:

Used TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numeric vectors

Generated sparse vectors representing each channel

🤖 Recommendation System

Query Input: User types a topic or interest

Vectorization: Convert query into TF-IDF vector

Similarity Computation: Use cosine similarity to compare query with channel vectors

Top-K Results: Return top channels sorted by similarity

Sample Output:

Channel	Description	Subscribers	Views	Videos	Score
CodeWithHarry	Learn Python, Java, ML...	2M	100M	300	0.89
freeCodeCamp	Programming tutorials...	4M	500M	150	0.85
⚡ Key Features

Fast, similarity-based recommendations

Uses real metadata from 1 million+ channels

Handles large datasets efficiently

Can be extended to include trending, category-based, or personalized suggestions

🛠 Tech Stack

Python – Data manipulation & logic

Pandas – Data handling

Scikit-learn – TF-IDF vectorization & cosine similarity

Pickle – Save/load trained model

📁 Files in Repository

youtube_model.pkl – Trained model with TF-IDF vectors & dataframe

recommendation.ipynb – Step-by-step notebook for preprocessing & training

README.md – Project documentation

🎯 Future Enhancements

Include channel thumbnails & clickable links

Add user feedback loop for personalization

Integrate category-based or trending channel recommendations

Deploy with Streamlit / Web App for interactive usage

👏 Contributing

Pull requests are welcome!

Fork the repo

Train your own model with the dataset

Suggest enhancements for more interactive recommendations

📌 References

Kaggle – YouTube Channels Dataset

Scikit-learn TF-IDF Documentation

Cosine Similarity Theory
