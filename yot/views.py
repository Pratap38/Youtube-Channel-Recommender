from django.shortcuts import render
import pickle
import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity

# Load trained model
with open("yot/youtube_recommendation_model.pkl", "rb") as f:
    saved_model = pickle.load(f)

vectorizer = saved_model["vectorizer"]
tfidf_matrix = saved_model["tfidf_matrix"]
df = saved_model["dataframe"]

# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

# Recommendation function
def recommend_channels(query, df, vectorizer, tfidf_matrix, top_k=5):
    query_vec = vectorizer.transform([clean_text(query)])
    similarity = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarity.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        # Make sure all text fields are strings
        description = str(df.iloc[idx].get("description", ""))
        channel = str(df.iloc[idx].get("channel_name", "Unknown"))
        subscribers = df.iloc[idx].get("Subscribers", "N/A")
        views = df.iloc[idx].get("total_views", "N/A")
        videos = df.iloc[idx].get("total_videos", "N/A")

        results.append({
            "channel": channel,
            "description": description[:200] + "...",
            "subscribers": subscribers,
            "views": views,
            "videos": videos,
            "score": round(similarity[idx], 3)
        })
    return results


# Django view
def home(request):
    recommendations = []
    query = ""

    # Use GET because your form uses method="get"
    query = request.GET.get("query", "").strip()
    if query:
        recommendations = recommend_channels(query, df, vectorizer, tfidf_matrix, top_k=5)

    return render(request, "home.html", {
        "recommendations": recommendations,
        "query": query
    })
