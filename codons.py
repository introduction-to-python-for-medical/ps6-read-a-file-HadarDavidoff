def create_codon_dict(file_path):
    dicofco = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        rows = file.readlines()
    
    # בדיקה אם הקובץ ריק
    if not rows:
        print("⚠️ הקובץ ריק!")
        return {}

    # מעבר על השורות, תוך דילוג על כותרת אם יש
    for r in rows[1:]:  # שינוי ל-rows[1:] כדי לדלג על כותרת
        cells = r.strip().split('\t')  # חלוקה לפי טאב

        # בדיקה שהשורה מכילה לפחות 3 עמודות כדי למנוע שגיאת IndexError
        if len(cells) < 3:
            print(f"⚠️ דילוג על שורה לא תקינה: {r.strip()}")
            continue  

        key = cells[0]  
        value = cells[2]  
        dicofco[key] = value
    
    return dicofco
