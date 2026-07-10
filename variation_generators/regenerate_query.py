import openai
import csv

# Initialize the OpenAI API client
openai.api_key = 'REDACTED'  # Replace with your actual API key

def get_paraphrase(query):
    """Gets a paraphrased query using the ChatGPT-4 API."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Paraphrase the following query and provide a query that conveys the same meaning. The query must be grammatically correct and clearly written: {query}"}
        ]
    )
    return response.choices[0].message['content'].strip()

def main():
    # Input and output CSV filenames
    input_filename = r'C:\Users\olica\Downloads\unique_queries_antique.csv'
    output_filename = r'C:\Users\olica\Downloads\paraphrased_queries_antique.csv'

    # Lists to store read data and generated paraphrases
    queries_with_ids = []

    # Read input CSV
    with open(input_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            query_id, original_query = row
            queries_with_ids.append({'id': query_id, 'query': original_query})

    # CSV file setup for output
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'original_query', 'paraphrased_query']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()

        # Iterate over each query, get its paraphrase, and write to the CSV
        for item in queries_with_ids:
            paraphrased = get_paraphrase(item['query'])
            writer.writerow({'id': item['id'], 'original_query': item['query'], 'paraphrased_query': paraphrased})

if __name__ == '__main__':
    main()