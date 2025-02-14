def create_codon_dict(file_path):
    dicofco = {}

    # פתיחת הקובץ עם קידוד utf-8 כדי למנוע בעיות בתווים מיוחדים
    with open(file_path, 'r', encoding='utf-8') as file:
        rows = file.readlines()

    # בדיקה אם הקובץ ריק
    if not rows:
        return {}

    # מעבר על השורות, דילוג על הכותרת אם קיימת
    for r in rows[1:]:  # דילוג על השורה הראשונה (הכותרת)
        cells = r.strip().split('\t')  # פיצול לפי טאבים

        # לוודא שהשורה תקינה וכוללת לפחות 3 עמודות
        if len(cells) < 3:
            continue  

        key = cells[0].strip()  # ניקוי רווחים מיותרים מהמפתח
        value = cells[1].strip()  # שינוי כדי לוודא שהעמודה הנכונה נבחרת (אולי זה העמודה השנייה ולא השלישית?)

        dicofco[key] = value

    return dicofco
