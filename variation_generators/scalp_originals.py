import csv

# Dictionary to hold unique original queries and their associated IDs
unique_queries = {}

# Read the CSV file
with open(r'C:\Users\olica\Downloads\variations_antique_labeled.csv', mode='r') as file:
    reader = csv.reader(file)
    
    # Skip the header (if there is one)
    next(reader, None)
    
    for row in reader:
        query_id = row[1]
        original_query = row[4]
        # Check if the original query is not in the dictionary
        if original_query not in unique_queries:
            unique_queries[original_query] = query_id

# Write the unique queries and their IDs to a new CSV file
with open(r'C:\Users\olica\Downloads\unique_queries.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Query ID', 'Original Query'])
    for query, q_id in unique_queries.items():
        writer.writerow([q_id, query])