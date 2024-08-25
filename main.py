import csv

def clean_row(row):
    """
    Strip whitespace from keys and values in the row.
    
    Args:
        row (dict): A dictionary representing a row from the CSV file.
    
    Returns:
        dict: The cleaned row with stripped whitespace.
    """
    return {key.strip(): (value.strip() if value else value) for key, value in row.items()}

def read_csv(file_path):
    """
    Read the CSV file and return cleaned rows.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Yields:
        dict: A cleaned row from the CSV file.
    """
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter='|')
        
        # Strip whitespace from the fieldnames
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        
        for row in reader:
            yield clean_row(row)

def display_employee_info(rows, headers):
    """
    Display specific employee information in a formatted manner.
    
    Args:
        rows (iterable): An iterable of cleaned rows from the CSV file.
        headers (list): A list of specific headers to display.
    """
    for row in rows:
        employee_info_parts = []  # Initialize an empty list to hold the info parts
        
        for header in headers:
            # Get the value for the current header, strip whitespace, and format it
            value = row.get(header, '').strip()
            formatted_info = f"{header}: {value}"
            employee_info_parts.append(formatted_info)  # Add the formatted info to the list
        
        # Join all parts with a comma and print the result
        employee_info_string = ", ".join(employee_info_parts)
        print(employee_info_string)

def main():
    """
    Main function to execute the script.
    """
    csv_file_path = 'data.csv'
    desired_headers = ['employee_id', 'employee_first_name_global', 'employee_last_name_global', 'mobile_number']
    
    try:
        employee_rows = read_csv(csv_file_path)
        display_employee_info(employee_rows, desired_headers)
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
