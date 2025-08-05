import cv2

url = 'http://100.84.185.162:8080/video'  # Your phone's IP
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Cannot open camera stream. Check IP and Wi-Fi connection.")
    exit()

print("Camera stream opened.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Mobile Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
