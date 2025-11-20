import cv2
import numpy as np
from tensorflow.keras.models import load_model

# === Paramètres ===
MODEL_PATH = r"C:\Users\Aymen\Documents\birse\PJT_PINGPONG_ROBOT\Programmes\model.h5"
IMAGE_DIM = 194  # Taille attendue par le modèle
FOCAL_LENGTH = 585
KNOWN_DIAMETER = 40  # 

# Charger le modèle
model = load_model(MODEL_PATH)

def detect_red_triangles(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    red_only = cv2.bitwise_and(frame, frame, mask=red_mask)
    gray = cv2.cvtColor(red_only, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        epsilon = 0.04 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        if len(approx) == 3 and cv2.contourArea(cnt) > 500:
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)
            cv2.putText(frame, 'Triangle Rouge', tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def detect_green_squares(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    green_only = cv2.bitwise_and(frame, frame, mask=green_mask)
    gray = cv2.cvtColor(green_only, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        epsilon = 0.04 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        if len(approx) == 4 and cv2.contourArea(cnt) > 500 and cv2.isContourConvex(approx):
            cv2.drawContours(frame, [approx], 0, (0, 255, 255), 3)
            cv2.putText(frame, 'Carre+ Vert', tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

def detect_ping_pong_ball(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([5, 150, 150])
    upper_orange = np.array([25, 255, 255])
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    blurred = cv2.GaussianBlur(mask, (9, 9), 2)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 50, param1=50, param2=30, minRadius=10, maxRadius=100)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            x, y, radius = i[0], i[1], i[2]
            diameter_pixels = radius * 2
            distance = (KNOWN_DIAMETER * FOCAL_LENGTH) / diameter_pixels if diameter_pixels > 0 else 0

            roi = frame[max(0, y - radius):min(y + radius, frame.shape[0]),
                        max(0, x - radius):min(x + radius, frame.shape[1])]

            if roi.size > 0:
                roi_resized = cv2.resize(roi, (IMAGE_DIM, IMAGE_DIM))
                roi_resized = roi_resized.astype("float32") / 255.0
                img_array = np.expand_dims(roi_resized, axis=0)

                prediction = model.predict(img_array, verbose=0)
                predicted_class = np.argmax(prediction)

                if predicted_class == 0 and prediction[0][0] >= 0.9:
                    cv2.circle(frame, (x, y), radius, (255, 0, 0), 2)
                    cv2.putText(frame, f"X: {x}  Y: {y}", (x + 35, y - radius + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)
                    cv2.putText(frame, f"Diam: {diameter_pixels}px", (x + 35, y - radius + 35), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)
                    cv2.putText(frame, f"Dist: {distance:.2f} mm", (x + 35, y - radius + 55), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0,0), 2)
                    cv2.putText(frame, "Balle de Ping-Pong", (x + 35, y - radius), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Détection Mixte')

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur : Impossible de capturer l'image")
            break

        detect_red_triangles(frame)
        detect_green_squares(frame)
        detect_ping_pong_ball(frame)

        cv2.imshow('Détection Mixte', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()
