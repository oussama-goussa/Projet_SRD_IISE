import cv2

print("Version OpenCV :", cv2.__version__)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur de capture de la webcam")
        break
    cv2.imshow('Test Webcam', frame)

    if cv2.waitKey(1) == 27:  # Appuyer sur ECHAP pour quitter
        break

cap.release()
cv2.destroyAllWindows()
