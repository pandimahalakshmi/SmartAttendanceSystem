import cv2
import os

name = input("Enter your name: ").strip()

save_path = f"dataset/{name}"
os.makedirs(save_path, exist_ok=True)

url = 'http://100.84.185.162:8080/video'
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Cannot open camera stream. Check IP and Wi-Fi connection.")
    exit()

print("Camera stream opened. Capturing face images...")

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        cv2.imwrite(f"{save_path}/{count}.jpg", face_img)
        count += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Register Face - Mobile Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if count >= 20:
        print("Collected 20 face images.")
        break

cap.release()
cv2.destroyAllWindows()
