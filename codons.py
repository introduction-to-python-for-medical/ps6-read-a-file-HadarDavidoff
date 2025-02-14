def create_codon_dict(file_path):
    dicofco = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        rows = file.readlines()

    for r in rows[1:]:  # דילוג על הכותרת אם יש אחת
        cells = r.strip().split('\t')  
        if len(cells) < 3:  # בדיקה למניעת שגיאת IndexError
            continue  
        key = cells[0]  
        value = cells[2]  
        dicofco[key] = value
    
    return dicofco
