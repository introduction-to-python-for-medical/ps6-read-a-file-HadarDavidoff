def create_codon_dict(file_path):
    dicofco = {}

    # פתיחת הקובץ עם קידוד utf-8 כדי למנוע בעיות
    with open(file_path, 'r', encoding='utf-8') as file:
        rows = file.readlines()
    
    # בדיקה אם הקובץ ריק
    if not rows:
        print("⚠️ הקובץ ריק!")
        return {}

    # מעבר על השורות, דילוג על הכותרת אם קיימת
    for r in rows[1:]:  # שנה ל־rows[:] אם אין כותרת
        cells = r.strip().split()  # שים לב: `split()` ללא פרמטר מפצל גם רווחים וגם טאבים

        # בדיקה שהשורה מכילה לפחות 3 עמודות
        if len(cells) < 3:
            print(f"⚠️ דילוג על שורה לא תקינה: {r.strip()}")
            continue  

        key = cells[0].strip()  # מסירים רווחים מיותרים מהמפתח
        value = cells[2].strip()  # מסירים רווחים מיותרים מהערך

        dicofco[key] = value

    return dicofco
