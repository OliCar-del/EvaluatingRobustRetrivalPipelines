import csv
import random

def remove_random_character(query, stats):
    if not query:
        return query
    remove_index = random.randint(0, len(query) - 1)
    if query[remove_index] == ' ':
        stats['spaces_removed'] += 1
    return query[:remove_index] + query[remove_index + 1:], stats

def process_queries(input_csv, output_csv):
    stats = {'spaces_removed': 0, 'total_spaces': 0}
    
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['q_id', 'original_query', 'altered_query']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header for the output CSV
        writer.writeheader()
        
        for row in reader:
            query_id = row['q_id']
            original_query = row['original_query']
            stats['total_spaces'] += original_query.count(' ')
            altered_query, stats = remove_random_character(original_query, stats)
            writer.writerow({'q_id': query_id, 'original_query': original_query, 'altered_query': altered_query})
    
    if stats['total_spaces'] > 0:
        percentage_spaces_removed = (stats['spaces_removed'] / stats['total_spaces']) * 100
    else:
        percentage_spaces_removed = 0

    return percentage_spaces_removed

# Replace 'your_input_file.csv' with the path to your CSV file.
input_csv_filename = 'your_input_file.csv'
output_csv_filename = 'query_variations_del.csv'

percentage_of_spaces_removed = process_queries(r'C:\Users\olica\Downloads\unique_queries_antique.csv', r'C:\Users\olica\Downloads\query_variations_del_space_antique.csv')
print(f"Percentage of spaces removed: {percentage_of_spaces_removed:.2f}%")