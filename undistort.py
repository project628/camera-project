import cv2
import numpy as np
import glob
import os

# גודל התמונות ששימשו לקליברציה
DIM = (1280, 720)

K = np.array([[988.50208121, 0.0, 683.88362098],
              [0.0, 984.58934001, 362.94940409],
              [0.0, 0.0, 1.0]])

D = np.array([[-4.12064648e-01],
              [1.89443353e-01],
              [-8.98931969e-04],
              [-5.94070417e-06],
              [-3.72769525e-02]])

# תיקייה שבה נמצאות התמונות
image_dir = r"C:\Users\eeproj\Desktop\Project\download YOLOV5\photo"
output_dir = os.path.join(image_dir, "undistorted")
os.makedirs(output_dir, exist_ok=True)

images = glob.glob(os.path.join(image_dir, "*.jpg"))  # אפשר גם להוסיף *.png וכו'

for img_path in images:
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ לא ניתן לטעון: {img_path}")
        continue

    h, w = img.shape[:2]
    if (w, h) != DIM:
        print(f"⚠️ מידות שונות ({w}x{h}) מהמידות המקוריות {DIM}, התיקון עלול להיות לא מדויק")

    map1, map2 = cv2.initUndistortRectifyMap(K, D, None, K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    out_path = os.path.join(output_dir, "undistorted_" + os.path.basename(img_path))
    cv2.imwrite(out_path, undistorted_img)
    print(f"✅ נשמר: {out_path}")

print("🎉 סיום! כל התמונות תוקנו ונשמרו בתיקייה 'undistorted'.")
