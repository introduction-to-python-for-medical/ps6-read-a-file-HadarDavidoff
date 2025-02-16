def create_codon_dict(file_path): 
    file = open(file_path,'r')
    rows = file.readlines()
    file.close()  
    dictionary = {}
    for row in rows:
        row_cells = row.strip().split('\t') 
        codon = row_cells[0]
        amino_acid = row_cells[2]
        dictionary[codon] = amino_acid
    return dictionary
