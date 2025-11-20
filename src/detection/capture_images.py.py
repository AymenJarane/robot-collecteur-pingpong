import cv2
import os
import numpy as np

# Définition du dossier de sauvegarde
save_dir = r"C:\Users\Aymen\Documents\birse\PJT_PINGPONG_ROBOT\BDD_BALLE"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def capture():
    cap = cv2.VideoCapture(0)  # Ouvrir la caméra une seule fois
    img_counter = 0  # Compteur d'images

    cv2.namedWindow('Détection Balle Ping-Pong')  # Créer une seule fenêtre

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur : Impossible de capturer l'image")
            break

        # Conversion en HSV pour la détection de couleur
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Définition des plages de couleur pour une balle de ping-pong (orange/blanc)
        lower_orange = np.array([5, 150, 150])  
        upper_orange = np.array([25, 255, 255])

        mask = cv2.inRange(hsv, lower_orange, upper_orange)  # Filtrage des pixels dans la plage

        # Détection de contours et de cercles
        blurred = cv2.GaussianBlur(mask, (9, 9), 2)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 50, param1=50, param2=30, minRadius=10, maxRadius=100)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                # Dessiner le cercle détecté
                cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)

                if cv2.waitKey(1) & 0xFF == ord('c'):  # Sauvegarder l'image avec 'c'
                    img_name = os.path.join(save_dir, f"balle_{img_counter}.jpg")
                    roi = frame[i[1] - i[2]:i[1] + i[2], i[0] - i[2]:i[0] + i[2]]  # Extraire la balle
                    if roi.size > 0:
                        cv2.imwrite(img_name, roi)
                        print(f"Image enregistrée : {img_name}")
                        img_counter += 1

        cv2.imshow('Détection Balle Ping-Pong', frame)  # Une seule fenêtre

        if cv2.waitKey(1) == ord('q'):  # Quitter avec 'q'
            break

    cap.release()
    cv2.destroyAllWindows()  # Fermer toutes les fenêtres proprement

capture()
