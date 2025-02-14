def create_codon_dict(file_path):
    dicofco = {}

    # פתיחת הקובץ עם קידוד UTF-8
    with open(file_path, 'r', encoding='utf-8') as file:
        rows = file.readlines()

    # בדיקה אם הקובץ ריק
    if not rows:
        return {}

    # מעבר על השורות (מדלגים על כותרת)
    for r in rows[1:]:
        # פיצול השורה באופן גמיש (עובד גם אם ההפרדה היא רווחים וגם אם היא טאבים)
        cells = r.strip().split()

        # בדיקה שהשורה מכילה לפחות 2 עמודות
        if len(cells) < 2:
            continue  

        key = cells[0].strip()  # ניקוי רווחים מהמפתח
        value = cells[1].strip()  # לקיחת העמודה השנייה כערך

        # בדיקה שהמפתח מכיל 3 תווים (למניעת שגיאות)
        if len(key) == 3:
            dicofco[key] = value

    return dicofco
