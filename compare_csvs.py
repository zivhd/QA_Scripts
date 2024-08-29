#!/usr/bin/env python3

import csv
import argparse
from datetime import datetime

def read_csv(filepath):
    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def find_common_headers(header1, header2):
    return list(set(header1) & set(header2))

def filter_columns(data, headers_to_keep):
    header = data[0]
    indices = [header.index(col) for col in headers_to_keep]
    filtered_data = [[row[index] for index in indices] for row in data]
    return [headers_to_keep] + filtered_data

def sort_by_column(data, column_index):
    header = data[0]
    rows = data[1:]
    sorted_rows = sorted(rows, key=lambda x: x[column_index])
    return [header] + sorted_rows

def find_column_index(header_row, column_name):
    return header_row.index(column_name)

def normalize_value(value):
    # Replace 'null' with ''
    if value.strip().lower() == 'null':
        return ''
    
    # Trim leading and trailing whitespaces
    value = value.strip()
    
    # Normalize dates
    try:
        return datetime.strptime(value, '%d %b %Y, %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        pass

    try:
        return datetime.strptime(value, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        pass

    # Normalize decimal points (convert to float and remove trailing zeros)
    try:
        float_value = float(value)
        return str(int(float_value)) if float_value.is_integer() else str(float_value)
    except ValueError:
        return value

def normalize_row(row):
    return [normalize_value(cell) for cell in row]

def compare_csv(file1, file2, sort_column):
    # Read the CSV files
    data1 = read_csv(file1)
    data2 = read_csv(file2)

    # Extract headers and rows
    header1 = data1[0]
    header2 = data2[0]

    # Find common headers
    common_headers = find_common_headers(header1, header2)
    
    if not common_headers:
        print("No common headers found.")
        return False

    # Filter columns to keep only common headers
    filtered_data1 = filter_columns(data1, common_headers)
    filtered_data2 = filter_columns(data2, common_headers)

    # Check if the sort column is in the common headers
    if sort_column not in common_headers:
        print(f"Sort column '{sort_column}' is not in the common headers.")
        return False

    # Find the index of the column to sort by
    column_index = find_column_index(common_headers, sort_column)

    # Normalize and sort the data by the specified column
    normalized_data1 = [normalize_row(row) for row in filtered_data1]
    normalized_data2 = [normalize_row(row) for row in filtered_data2]

    sorted_data1 = sort_by_column(normalized_data1, column_index)
    sorted_data2 = sort_by_column(normalized_data2, column_index)

    # Create dictionaries for easy comparison
    def create_row_dict(data):
        return {tuple(row): i for i, row in enumerate(data)}

    data1_dict = create_row_dict(sorted_data1)
    data2_dict = create_row_dict(sorted_data2)

    all_keys = set(data1_dict.keys()) | set(data2_dict.keys())
    
    differences_found = False

    for key in all_keys:
        if key in data1_dict and key in data2_dict:
            if sorted_data1[data1_dict[key]] != sorted_data2[data2_dict[key]]:
                differences_found = True
                print(f"Difference in row {data1_dict[key]}:")
                print(f"File1: {sorted_data1[data1_dict[key]]}")
                print(f"File2: {sorted_data2[data2_dict[key]]}")
        elif key in data1_dict:
            differences_found = True
            print(f"Row {data1_dict[key]} only in File1:")
            print(f"File1: {sorted_data1[data1_dict[key]]}")
        elif key in data2_dict:
            differences_found = True
            print(f"Row {data2_dict[key]} only in File2:")
            print(f"File2: {sorted_data2[data2_dict[key]]}")

    if not differences_found:
        print("The CSV files are the same.")
    return not differences_found

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two CSV files sorted by a specific column.")
    parser.add_argument("file1", help="Path to the first CSV file")
    parser.add_argument("file2", help="Path to the second CSV file")
    parser.add_argument("sort_column", help="Name of the column to sort by")
    args = parser.parse_args()

    # Compare the CSV files
    are_same = compare_csv(args.file1, args.file2, args.sort_column)

    # Set exit code based on comparison result
    if are_same:
        exit(0)
    else:
        exit(1)
