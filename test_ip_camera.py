import cv2

# Replace with the exact IP shown in your phone's app
url = 'http://100.84.185.162:8080/video'

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Mobile Camera - IP Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
