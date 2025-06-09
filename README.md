# Social Media Sentiment Analysis

This project analyzes public sentiment towards specific topics, products, or events using social media data (e.g., X posts). It uses Natural Language Processing (NLP) with the VADER sentiment analyzer to preprocess text, extract sentiment scores, and visualize trends over time using Matplotlib.

## Features
- **Text Preprocessing**: Removes URLs, mentions, hashtags, and stopwords from text.
- **Sentiment Analysis**: Computes sentiment scores using VADER (positive, negative, neutral).
- **Visualization**: Creates a line plot of average daily sentiment scores.
- **Output**: Saves processed data as a CSV and the sentiment trend plot as a PNG.

## Prerequisites
- Python 3.12 or higher
- Required Python packages:
  - `pandas`
  - `nltk`
  - `matplotlib`
  - `requests`
- X API credentials (optional, for real-time data)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/social-media-sentiment-analysis.git
   cd social-media-sentiment-analysis


Set Up a Virtual Environment (recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install pandas nltk matplotlib requests


Download NLTK Data:The script automatically downloads required NLTK resources (vader_lexicon, stopwords, punkt, punkt_tab). Ensure an internet connection for the first run. Alternatively, manually download:
import nltk
nltk.download(['vader_lexicon', 'stopwords', 'punkt', 'punkt_tab'])



Usage

Configure X API (optional):To analyze real X posts, update mr.py with your X API credentials:
api_key = "your_api_key"
api_secret = "your_api_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

Get credentials from X Developer Portal.

Run the Script:
python mr.py


Output:

Data: output/sentiment_data.csv contains processed text and sentiment scores.
Plot: output/sentiment_trend.png shows the average sentiment trend over time.



Project Structure
social-media-sentiment-analysis/
├── mr.py                   # Main sentiment analysis script
├── output/                 # Output directory (created automatically)
│   ├── sentiment_data.csv  # Processed data
│   ├── sentiment_trend.png # Sentiment trend plot
├── README.md               # Project documentation

Sample Output

CSV (sentiment_data.csv):text,date,cleaned_text,sentiment
"Loving the new phone release! Amazing features #Tech",2025-06-01,"loving new phone release amazing features",0.8402
...


Plot (sentiment_trend.png):A line plot of average sentiment scores (from -1 to +1) over time.

Notes

The script uses sample data by default. Add X API credentials for real-time data.
NLTK data is stored in ~/nltk_data. Update nltk.data.path in mr.py if needed.
Tested with Python 3.12 on macOS.

Troubleshooting

NLTK Errors: If resources are missing, run:import nltk
nltk.download('punkt_tab')


SSL Issues (macOS): Install certificates:/Applications/Python\ 3.12/Install\ Certificates.command


Ensure dependencies are installed in the active Python environment.

License
MIT License. See LICENSE for details.
Contact
For issues or suggestions, open a GitHub issue or contact your-email@example.com.```
