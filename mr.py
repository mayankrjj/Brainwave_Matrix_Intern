import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

# Set NLTK data path explicitly
nltk.data.path.append('/Users/mohitrajput/nltk_data')

# Download required NLTK data with error handling
required_resources = ['vader_lexicon', 'stopwords', 'punkt', 'punkt_tab']
for resource in required_resources:
    try:
        nltk.data.find(resource)
        print(f"{resource} is already available.")
    except LookupError:
        print(f"Downloading {resource}...")
        try:
            nltk.download(resource, quiet=True)
        except Exception as e:
            print(f"Failed to download {resource}: {e}")
            exit(1)

# Sample data (for demonstration; replace with real X API data)
sample_data = [
    {"text": "Loving the new phone release! Amazing features #Tech", "date": "2025-06-01"},
    {"text": "This product is a total letdown. Poor battery life. #Tech", "date": "2025-06-02"},
    {"text": "Excited for the tech event! Can't wait to see what's new.", "date": "2025-06-03"},
    {"text": "The new update is buggy and frustrating #Tech", "date": "2025-06-04"},
    {"text": "Best gadget ever! Highly recommend it. #Tech", "date": "2025-06-05"},
]


# Function to fetch X posts (requires API credentials)
def fetch_x_posts(query, api_key, api_secret, access_token, access_token_secret):
    # Placeholder for X API v2 authentication and request
    url = "https://api.x.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"query": query, "max_results": 100}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.RequestException as e:
        print(f"Error fetching X data: {e}")
        return []


# Text preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove URLs, mentions, hashtags, and special characters
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|\#\w+|[^\w\s]', '', text)
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)


# Analyze sentiment
def analyze_sentiment(texts):
    sia = SentimentIntensityAnalyzer()
    sentiments = []
    for text in texts:
        score = sia.polarity_scores(text)
        sentiments.append(score['compound'])
    return sentiments


# Main function
def main():
    # Use sample data or fetch real data (uncomment and configure API credentials)
    # api_key = "your_api_key"
    # api_secret = "your_api_secret"
    # access_token = "your_access_token"
    # access_token_secret = "your_access_token_secret"
    # posts = fetch_x_posts("tech", api_key, api_secret, access_token, access_token_secret)
    posts = sample_data

    # Create DataFrame
    df = pd.DataFrame(posts)
    if df.empty:
        print("No data retrieved. Using sample data.")
        df = pd.DataFrame(sample_data)

    # Preprocess text
    try:
        df['cleaned_text'] = df['text'].apply(preprocess_text)
    except Exception as e:
        print(f"Error in text preprocessing: {e}")
        exit(1)

    # Analyze sentiment
    try:
        df['sentiment'] = analyze_sentiment(df['cleaned_text'])
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        exit(1)

    # Convert dates
    df['date'] = pd.to_datetime(df['date'])

    # Group by date for trend analysis
    daily_sentiment = df.groupby(df['date'].dt.date)['sentiment'].mean().reset_index()

    # Visualize sentiment trends with Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(daily_sentiment['date'], daily_sentiment['sentiment'], marker='o', color='#1f77b4', linestyle='-',
             linewidth=2)
    plt.title('Sentiment Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Sentiment Score')
    plt.grid(True)
    plt.xticks(rotation=45)

    # Save plot
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(os.path.join(output_dir, 'sentiment_trend.png'))
    plt.close()

    # Save processed data
    df.to_csv(os.path.join(output_dir, 'sentiment_data.csv'), index=False)
    print("Sentiment analysis complete. Check 'output' directory for results.")


if __name__ == "__main__":
    main()
