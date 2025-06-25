import cv2
import numpy as np

# === קליברציה מהקובץ שלך ===
DIM = (1280, 720)
K = np.array([[988.50208121, 0.0, 683.88362098],
              [0.0, 984.58934001, 362.94940409],
              [0.0, 0.0, 1.0]], dtype=np.float64)

D = np.array([[-4.12064648e-01],
              [1.89443353e-01],
              [-8.98931969e-04],
              [-5.94070417e-06],
              [-3.72769525e-02]], dtype=np.float64)

# === פותח מצלמה USB (index 0 או 1) ===
cap = cv2.VideoCapture(1)  # שנה ל-1 אם זה לא פותח את מצלמת ה-USB

# קבע רזולוציה שתואמת ל-DIM
cap.set(cv2.CAP_PROP_FRAME_WIDTH, DIM[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, DIM[1])

# בנה את מפת ההמרה רק פעם אחת
map1, map2 = cv2.initUndistortRectifyMap(K, D, None, K, DIM, cv2.CV_16SC2)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ לא הצלחתי לקרוא מהמצלמה")
        break

    # ודא שהרזולוציה תואמת
    if frame.shape[1] != DIM[0] or frame.shape[0] != DIM[1]:
        frame = cv2.resize(frame, DIM)

    # תקן את העיוות
    undistorted = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR)

    # הצג את התוצאה
    cv2.imshow("Undistorted (מתוקן)", undistorted)
    cv2.imshow("Original (מקורי)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC כדי לצאת
        break

cap.release()
cv2.destroyAllWindows()
