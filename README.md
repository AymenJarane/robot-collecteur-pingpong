🏓 Robot Collecteur de Balles de Ping-Pong



Projet PJT — ENSAM

Auteurs : EL Jakani Youssef, Jarane Aymen, Laroussi Amine, Lazar Mohamed

Encadrant : Abdelmajid Cheriffi



📌 Description du projet



Ce projet consiste en la conception et la réalisation d’un robot autonome capable de :



détecter une balle de ping-pong,



se diriger vers elle,



la saisir grâce à un bras robotisé,



puis la rapporter à une position de départ.



Le système combine vision artificielle, traitement d'image, apprentissage automatique, contrôle moteur et cinématique du bras robotique.

Ce dépôt contient le code source, les scripts de détection, le modèle entraîné, les programmes Arduino ainsi que la documentation.



📄 Le rapport complet du projet, avec toutes les explications détaillées, est disponible dans le dossier docs/

Référence : Compte\_Rendu\_PJT\_n°18.pdf



🧠 Architecture générale du robot



Le robot suit une architecture modulaire, composée de 4 sous-systèmes :



🔍 1. Module de perception



Caméra HD (Microsoft LifeCam Studio)



Vision par ordinateur (OpenCV)



CNN pour classification de la balle



Détection :



Couleur (HSV)



Forme (HoughCircles)



Validation par IA



🧭 2. Module de décision



Raspberry Pi 5



Exécution des scripts Python



Communication série UART avec Arduino



Gestion des états (patrouille → détection → saisie → retour)



🚗 3. Module de locomotion



Châssis 2 roues + roue folle



Moteurs DC avec driver ADMH2407ND



Pilotage via Arduino en PWM



🤖 4. Module de manipulation



Bras robotisé 3 DOF (épaule, coude, pince)



Servomoteurs pilotés par Arduino



Cinématique inverse pour atteindre la balle



Calcul des angles (voir rapport section III)



🎯 Fonctionnement du robot



Initialisation (moteurs, caméra, bras)



Balayage de la zone (rotation + analyse visuelle)



Détection de la balle (couleur + forme + IA)



Approche automatique



Saisie avec le bras robotisé



Retour au point A



L'organigramme complet du fonctionnement est visible en page 16 du rapport.



🖥️ Structure du dépôt

robot-collecteur-pingpong/

│

├── README.md

├── LICENSE

├── .gitignore

│

├── src/

│   ├── detection/

│   │   ├── detection\_mixte.py

│   │   ├── capture\_images.py

│   │   ├── entrainement\_modele.py

│   │   ├── model.h5

│   │

│   ├── bras\_robotise/

│   │   └── controle\_bras.ino

│   │

│   └── locomotion/

│       └── moteurs.ino

│

├── docs/

│   ├── Compte\_Rendu\_PJT.pdf

│   ├── schema\_architecture.png

│   ├── organigramme.png

│   └── notes\_techniques.md

│

└── data/

&nbsp;   └── BDD\_BALLE/



🔧 Installation \& Exécution

1️⃣ Installer les dépendances Python

pip install opencv-python numpy tensorflow



2️⃣ Lancer le programme de détection

python src/detection/detection\_mixte.py



3️⃣ Entraîner le modèle CNN (optionnel)

python src/detection/entrainement\_modele.py



4️⃣ Programmer l’Arduino



Ouvrir controle\_bras.ino ou les fichiers moteurs dans l'IDE Arduino, puis téléverser.



🤖 Modèle d’apprentissage



Modèle CNN entraîné sur images capturées via capture\_images.py



Taille d’entrée : 194 × 194 × 3



But : différencier balle / non-balle



Fichier modèle : model.h5



Pour plus de détails, voir l’annexe du rapport (pages 22–24).🏓 Robot Collecteur de Balles de Ping-Pong



Projet PJT — ENSAM

Auteurs : EL Jakani Youssef, Jarane Aymen, Laroussi Amine, Lazar Mohamed

Encadrant : Abdelmajid Cheriffi



📌 Description du projet



Ce projet consiste en la conception et la réalisation d’un robot autonome capable de :



détecter une balle de ping-pong,



se diriger vers elle,



la saisir grâce à un bras robotisé,



puis la rapporter à une position de départ.



Le système combine vision artificielle, traitement d'image, apprentissage automatique, contrôle moteur et cinématique du bras robotique.

Ce dépôt contient le code source, les scripts de détection, le modèle entraîné, les programmes Arduino ainsi que la documentation.



📄 Le rapport complet du projet, avec toutes les explications détaillées, est disponible dans le dossier docs/

Référence : Compte\_Rendu\_PJT\_n°18.pdf



🧠 Architecture générale du robot



Le robot suit une architecture modulaire, composée de 4 sous-systèmes :



🔍 1. Module de perception



Caméra HD (Microsoft LifeCam Studio)



Vision par ordinateur (OpenCV)



CNN pour classification de la balle



Détection :



Couleur (HSV)



Forme (HoughCircles)



Validation par IA



🧭 2. Module de décision



Raspberry Pi 5



Exécution des scripts Python



Communication série UART avec Arduino



Gestion des états (patrouille → détection → saisie → retour)



🚗 3. Module de locomotion



Châssis 2 roues + roue folle



Moteurs DC avec driver ADMH2407ND



Pilotage via Arduino en PWM



🤖 4. Module de manipulation



Bras robotisé 3 DOF (épaule, coude, pince)



Servomoteurs pilotés par Arduino



Cinématique inverse pour atteindre la balle



Calcul des angles (voir rapport section III)



🎯 Fonctionnement du robot



Initialisation (moteurs, caméra, bras)



Balayage de la zone (rotation + analyse visuelle)



Détection de la balle (couleur + forme + IA)



Approche automatique



Saisie avec le bras robotisé



Retour au point A



L'organigramme complet du fonctionnement est visible en page 16 du rapport.



🖥️ Structure du dépôt

robot-collecteur-pingpong/

│

├── README.md

├── LICENSE

├── .gitignore

│

├── src/

│   ├── detection/

│   │   ├── detection\_mixte.py

│   │   ├── capture\_images.py

│   │   ├── entrainement\_modele.py

│   │   ├── model.h5

│   │

│   ├── bras\_robotise/

│   │   └── controle\_bras.ino

│   │

│   └── locomotion/

│       └── moteurs.ino

│

├── docs/

│   ├── Compte\_Rendu\_PJT.pdf

│   ├── schema\_architecture.png

│   ├── organigramme.png

│   └── notes\_techniques.md

│

└── data/

&nbsp;   └── BDD\_BALLE/



🔧 Installation \& Exécution

1️⃣ Installer les dépendances Python

pip install opencv-python numpy tensorflow



2️⃣ Lancer le programme de détection

python src/detection/detection\_mixte.py



3️⃣ Entraîner le modèle CNN (optionnel)

python src/detection/entrainement\_modele.py



4️⃣ Programmer l’Arduino



Ouvrir controle\_bras.ino ou les fichiers moteurs dans l'IDE Arduino, puis téléverser.



🤖 Modèle d’apprentissage



Modèle CNN entraîné sur images capturées via capture\_images.py



Taille d’entrée : 194 × 194 × 3



But : différencier balle / non-balle



Fichier modèle : model.h5



Pour plus de détails, voir l’annexe du rapport (pages 22–24).



🚀 Perspectives d’amélioration



Ajout de SLAM pour navigation autonome



Utilisation d’un lidar ou caméra stéréo



Optimisation de la saisie (pince plus flexible)



Détection multi-objets (YOLOv8)



Collaboration multi-robots



📄 Licence



Projet éducatif open-source.

