def create_codon_dict(file_path):
    dicofco = {}
    
    # פתיחת הקובץ עם קידוד utf-8 כדי למנוע בעיות בתווים מיוחדים
    with open(file_path, 'r', encoding='utf-8') as file:
        rows = file.readlines()
        
    # בדיקה אם הקובץ ריק
    if not rows:
        return {}

    # מעבר על השורות, דילוג על השורה הראשונה (הכותרת)
    for r in rows[1:]:  
        cells = r.strip().split()  # שימוש ב-split() כללי כדי להתמודד עם טאבים או רווחים

        # בדיקה שהשורה מכילה לפחות 2 עמודות
        if len(cells) < 2:
            continue  

        key = cells[0].strip()  # הסרת רווחים מהמפתח
        value = cells[1].strip()  # שימוש בעמודה השנייה כערך (כנראה במקום השלישית)

        dicofco[key] = value

    return dicofco
