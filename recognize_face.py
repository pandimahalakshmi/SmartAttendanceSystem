import cv2
import face_recognition
import pickle
from database import mark_attendance

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

cap = cv2.VideoCapture(1)  # DroidCam camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding, (top, right, bottom, left) in zip(encodings, boxes):
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            matched_idx = matches.index(True)
            name = data["names"][matched_idx]
            mark_attendance(name)

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    cv2.imshow("Face Recognition - Press Q to Quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
