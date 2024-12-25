import os
import cv2 as cv
import face_recognition


class Images:
    def __init__(self, path: str):
        self.image_path = path
        self.images = self.load_images()

    def load_images(self):
        images = []
        dirs = os.listdir(self.image_path)
        names = [i.split(".")[0] for i in dirs]

        for filename, name in zip(dirs, names):
            image_path = os.path.join(self.image_path, filename)
            read_image = face_recognition.load_image_file(image_path)
            image_encode = face_recognition.face_encodings(read_image)
            if image_encode:
                images.append({name: image_encode[0]})
        return images


samples = Images("images").images
webcam = cv.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if not ret:
        break

    face_locations = face_recognition.face_locations(frame)
    if not face_locations:
        continue

    face_encode = face_recognition.face_encodings(frame, face_locations)[0]

    person = "Unknown"
    for sample in samples:
        name, enc = list(sample.items())[0]
        if face_recognition.compare_faces([face_encode], enc)[0]:
            person = name
            break

    for face in face_locations:
        cv.rectangle(frame, (face[3], face[0]), (face[1], face[2]), (255, 0, 0), 3)
        cv.rectangle(frame, (face[3], face[2]), (face[3]+50, face[2]+20), (255, 0, 0), -1)
        cv.putText(frame, person, (face[3] + 10, face[2] + 10), cv.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

    cv.imshow("Face", frame)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
