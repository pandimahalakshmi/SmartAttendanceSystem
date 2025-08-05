import cv2

url = 'http://100.84.185.162:8080/video'  # Use your IP
cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('IP Webcam Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
