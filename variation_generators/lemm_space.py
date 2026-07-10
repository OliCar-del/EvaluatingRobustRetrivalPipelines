import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Make sure NLTK packages are downloaded (wordnet, punkt, and stopwords)
import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

def lemmatize_query(query):
    """
    Lemmatize non-stop words in a query.
    """
    if not isinstance(query, str):
        print(f"Warning: Non-string query detected: {query} (type: {type(query)})")
        # Handle the non-string query appropriately, e.g., return None or continue
        return None  # Return None for non-string queries

    # Your existing code to lemmatize the query
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(query)
    lemmatized_query = ' '.join([lemmatizer.lemmatize(w) for w in word_tokens if w.lower() not in stop_words])

    return lemmatized_query

def process_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    
    # Ensure all queries are strings
    df['original_query'] = df['original_query'].astype(str)
    
    # Apply lemmatization to each query
    df['altered_query'] = df['original_query'].apply(lemmatize_query)
    
    # Any queries that returned None should be addressed
    # Here, we replace None with the original query, but you might want to handle this differently
    df['altered_query'].fillna(df['original_query'], inplace=True)
    
    # Save the results to a new CSV file
    df.to_csv(output_csv, index=False)

# Make sure to use the correct path for your CSV file
input_csv_path = r'C:\Users\olica\Downloads\paraphrased_queries_trec2.csv'
output_csv_path = r'C:\Users\olica\Downloads\query_variations_lemm_trecccc.csv'

process_csv(input_csv_path, output_csv_path)