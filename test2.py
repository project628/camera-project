import cv2
import numpy as np
import glob
import os

# הגדרות לוח השחמט
CHECKERBOARD = (8, 6)
square_size = 1.0

# נקודות 3D בעולם
objp = np.zeros((CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
objp *= square_size

objpoints = []  # נקודות בעולם
imgpoints = []  # נקודות בתמונה

# נתיב לתיקיית התמונות
image_dir = r"C:\Users\eeproj\Desktop\Project\download YOLOV5\photo"
images = glob.glob(os.path.join(image_dir, "*.jpg"))  # או "*.png"

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)
        cv2.drawChessboardCorners(img, CHECKERBOARD, corners, ret)
        cv2.imshow('Corners', img)
        cv2.waitKey(200)
    else:
        print(f"⚠️ לא נמצאו פינות בתמונה: {fname}")

cv2.destroyAllWindows()

# קליברציה
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None
)

# הדפסה
print("Camera matrix:\n", camera_matrix)
print("\nDistortion coefficients:\n", dist_coeffs)

# שמירת הפלט
np.savez("calibration_data.npz", camera_matrix=camera_matrix, dist_coeffs=dist_coeffs)
print("✅ קובץ הקליברציה calibration_data.npz נשמר בתקייה הנוכחית.")
