import tkinter as tk
import subprocess
import os
import psutil

# משתנה לשמירה על תהליך ה-YOLO והוידאו
yolo_process = None
video_process = None

# פונקציה שתפעיל את הפקודות
def run_commands():
    global yolo_process, video_process
    # נתיב לסקריפט yolov5
    yolov5_path = r"C:\Users\eeproj\Desktop\Project\yolov5"
    # סקריפט פייתון להרצה
    command = "python detect.py --weights runs/train/exp75/weights/best.pt --img 640 --conf 0.4 --source 1"

    # שינוי ספרייה לתיקיית yolov5
    os.chdir(yolov5_path)

    # הרצת הפקודה וביצוע התהליך
    yolo_process = subprocess.Popen(command, shell=True)
    print(f"Yolo process started with PID: {yolo_process.pid}")

    # אם יש תהליך וידאו, נוודא שהוא רץ גם
    video_process = subprocess.Popen(command, shell=True)
    print(f"Video process started with PID: {video_process.pid}")


# פונקציה שתסגור את תהליך ה-YOLO ואת הוידאו
def stop_commands():
    global yolo_process, video_process
    if yolo_process:
        yolo_process.terminate()  # סגירת תהליך ה-YOLO
        print(f"Yolo process with PID {yolo_process.pid} has been terminated.")
        yolo_process = None
    else:
        print("No YOLO process to stop.")

    if video_process:
        try:
            # חיפוש תהליך פייתון עם cmdline שמריץ את detect.py
            found_process = False
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    # וודא שהפקודה לא ריקה וכוללת את detect.py
                    if proc.info['cmdline'] and 'detect.py' in proc.info['cmdline']:
                        print(f"Found process with PID: {proc.info['pid']}")
                        proc.terminate()  # סגירת תהליך הוידאו
                        print(f"Video process with PID {proc.info['pid']} has been terminated.")
                        found_process = True
                        break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # טיפול בשגיאות אפשריות (תהליך לא קיים/אין הרשאות/תהליך זומבי)
                    continue

            if not found_process:
                print("No detect.py process found.")
        except Exception as e:
            print(f"Error while stopping video process: {e}")

        video_process = None
    else:
        print("No video process to stop.")


# יצירת חלון tkinter
root = tk.Tk()
root.title("Yolo GUI")

# יצירת כפתור להרצה
run_button = tk.Button(root, text="הרץ YOLO", command=run_commands)
run_button.pack(pady=20)

# יצירת כפתור לסגירה
stop_button = tk.Button(root, text="עצור YOLO", command=stop_commands)
stop_button.pack(pady=20)

# הרצת הלולאת GUI
root.mainloop()
