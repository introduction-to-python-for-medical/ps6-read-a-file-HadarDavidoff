def create_codon_dict(file_path):
    dicofco = {}
    
    # Open the file and read lines
    with open(file_path, 'r') as file:
        rows = file.readlines()
    
    # Loop through each row (starting from 1 if you want to skip header)
    for r in rows[0:]:  # Skipping the first row if it's a header
        cells = r.strip().split('\t')  # Split by tab to get columns
        key = cells[0]  # Assuming the key is in the first column
        value = cells[2]  # Assuming the value is in the third column
        dicofco[key] = value
    
    return dicofco
