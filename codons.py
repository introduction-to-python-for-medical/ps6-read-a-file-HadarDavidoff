def create_codon_dict(file_path):
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        rows = file.readlines()
    
    for row in rows:
        row_cells = row.strip().split('\t')
        if len(row_cells) < 3:
            continue
        codon = row_cells[0].strip()
        amino_acid = row_cells[2].strip()
        dictionary[codon] = amino_acid

    return dictionary
