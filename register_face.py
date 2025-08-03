import cv2
import os

name = input("Enter Roll Number or Name: ")
save_path = os.path.join("dataset", name)

if not os.path.exists(save_path):
    os.makedirs(save_path)

cap = cv2.VideoCapture(1)  # DroidCam is usually camera index 1

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Register Face - Press S to Save, Q to Quit", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        img_path = os.path.join(save_path, f"{name}_{count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Saved: {img_path}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
