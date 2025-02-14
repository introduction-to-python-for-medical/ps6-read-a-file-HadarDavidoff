def create_codon_dict(file_path):
    dicofco = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            rows = file.readlines()

        if not rows:
            print("⚠️ הקובץ ריק!")
            return {}

        for r in rows[1:]:  # דילוג על כותרת
            cells = r.strip().split('\t')  
            if len(cells) < 3:  # בדיקה למניעת גישה מחוץ לטווח
                print(f"⚠️ דילוג על שורה לא תקינה: {r.strip()}")
                continue  
            key = cells[0]  
            value = cells[2]  
            dicofco[key] = value
    
    except Exception as e:
        print(f"❌ שגיאה בקריאת הקובץ: {e}")
        return {}

    return dicofco
