import os

# הנתיב לתיקיית התוויות
labels_dir = r"C:\Users\eeproj\Desktop\Project\valid_person_with_part_pistol\labels"  # שנה את הנתיב לתיקיית התוויות שלך

# יצירת רשימה של כל הקבצים בתיקיית התוויות
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

# אוסף של תוויות עם ערכים לא חוקיים
invalid_labels = []

# עבור כל קובץ תווית
for label_file in label_files:
    label_path = os.path.join(labels_dir, label_file)

    # פתיחת קובץ התווית
    with open(label_path, 'r') as f:
        lines = f.readlines()

        # עבור כל שורה בתווית
        for line in lines:
            parts = line.strip().split()  # פיצול השורה
            class_label = int(parts[0])  # הכיתוב נמצא תמיד בעמדה הראשונה

            # אם הכיתוב לא 0 ולא 1, תוסיף את השם של הקובץ ואת השורה שיש בה תקלה
            if class_label not in [0, 1]:
                invalid_labels.append((label_file, line))

# הדפסת תוצאות
if invalid_labels:
    print("מצאתי תוויות לא חוקיות:")
    for label_file, line in invalid_labels:
        print(f":file {label_file}, :line {line}")
else:
    print("good")
