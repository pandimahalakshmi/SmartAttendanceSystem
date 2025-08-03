import os
import cv2
import face_recognition
import pickle

dataset_path = "dataset"
encoding_file = "encodings.pkl"

known_encodings = []
known_names = []

print("Scanning dataset folder...")

for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    if not os.path.isdir(person_folder):
        continue

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        if not image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        image = cv2.imread(image_path)
        if image is None:
            continue

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        for encoding in face_encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

data = {"encodings": known_encodings, "names": known_names}

with open(encoding_file, "wb") as f:
    pickle.dump(data, f)

print("Face encoding completed and saved.")
